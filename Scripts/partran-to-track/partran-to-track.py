#!/bin/env python
# -*- coding: utf-8 -*-
#
#------------------------------------------------------------------------------
# partran-to-track.py
# Author: ostiguy@fnal.gov
#
# usage: partran-to-track.py <partran_file>  <track_file> 
# note: usally <partran_file> =  part_rfq.dst"
#              <track_file>   =  read_dis.dat"
#
#------------------------------------------------------------------------------
#
# Synopsis:
# ---------
#
# Read a PARTRAN/TraceWin *.dst file
#  - optionally translates it to ascii format
#  - optionally translates it to TRACKv39 format.
#
# The lattices functions and emittances are computed.
# Phase space plots are generated.
#
#
# PARTRAN *.dst files are binary files.
# According to the TraceWin documentation, the format is as follows:
#
#  char    125
#  char    100
#  int     Np
#  double  Ib(A)
#  double  freq(MHz)
#  char    0
#  Np × [6× double (x(cm),x'(rad),y(cm),y'(rad), phi(rad),Energy(MeV))]
#  double  mc2(MeV)
#
#-------------------------------------------------------------------------------
#
# The TRACKv39 distribution is a fortran binary file
# The format is implicitly defined by the following code
# fragment:
#
# if (iwrite_dis.eq.1) then
#    open(1, file='read_dis.dat', status='unknown' & ,access='SEQUENTIAL',form='UNFORMATTED')
#    write(1) Wtmp,nqtot
#    write(1) (npat(ird),ird=1,nqtot)
#    write(1) (qq (ird),ird=1,nqtot)
#    do iq = 1,nqtot
#       do i = 0,npat(iq)
#          write(1) x(i,iq) , xx(i,iq) , y(i,iq) , yy (i,iq),
#   &               csi(i,iq)/harm0, bb (i,iq) , spin(i,iq)
#       enddo
#    enddo
#    close(1)
#    endif
#
#    x(i,iq) cm 
#   xx(i,iq) rad 
#    y(i,iq) cm 
#   yy(i,iq) cm 
#  csi(i,iq) rad
#   bb(i,iq) relative velocity ( beta in version < 1.38; beta*gamma v >= 1.38 ) 
#  spin(i,iq)  1.0d0 if particle is within acceptance, -1.0d0 otherwise 
#
#  note that the loop over i runs from 0 to npat(iq) that is, over
#  npat(iq)+1 particles 
#-----------------------------------------------------------------------------

import sys
import getopt
import struct
import numpy

from math import sqrt as sqrt
from math import pi as pi

import numpy as np
import matplotlib.pyplot as plt
from   matplotlib.ticker import NullFormatter
from   mpl_toolkits.axes_grid1 import make_axes_locatable

partran_file = "part_rfq.dst"
track_file   = "read_dis.dat"
quiet        = False
showplots    = False
ascii        = False

def usage(cmd):
    global partran_file
    global track_file

    print "usage: "
    print "%s [-h] [-p] [-a] [-i  <input_file>] [-o <output_file>]" % cmd 
    print " -h: help"   
    print " -q: quiet"   
    print " -p, --show_plots : show plots"   
    print " -a, --ascii      : ascii "   
    print " -i input_file: specify partran  *.dst file [default: %s ]" % partran_file    
    print " -o input_file: specify TRACKv39 distribution file [default: %s ]" % track_file     
    return

def scatter_plot( xdata, ydata, title):

    # start with a rectangular Figure
    #plt.figure(1, figsize=(8,8))

    axScatter = plt.axes()
    axScatter.grid(True)
    #axScatter.set_aspect(1.0)
 
    divider = make_axes_locatable(axScatter)
    axHistx = divider.append_axes("top",   size="100%", pad=0.15, sharex=axScatter)
    axHisty = divider.append_axes("right", size="100%", pad=0.15, sharey=axScatter)
 
    plt.setp(axHistx.get_xticklabels() + axHisty.get_yticklabels(), visible=False)

    # the scatter plot:

    line = axScatter.scatter(xdata, ydata, s=1)

    xmax, xmin = np.max(xdata),  np.min(xdata) 
    ymax, ymin = np.max(ydata),  np.min(ydata)

    xbinwidth = (xmax-xmin)/100.0 
    ybinwidth = (ymax-ymin)/100.0 

    xbins = np.arange(xmin-xbinwidth/2.0, xmax + xbinwidth/2.0, xbinwidth)
    ybins = np.arange(ymin-ybinwidth/2.0, ymax + ybinwidth/2.0, ybinwidth)
    axHistx.hist(xdata, bins=xbins, normed=True, histtype='step')
    axHisty.hist(ydata, bins=ybins, orientation='horizontal', normed=True, histtype='step')

    #for tl in axHistx.get_xticklabels():
    #    tl.set_visible(False)

    #for tl in axHisty.get_yticklabels():
    #    tl.set_visible(False)

    plt.draw()
    plt.show()

    return


def main():

    global partran_file
    global track_file
    global quiet
    global showplots
    global ascii
    
    
    try:
        opts,args = getopt.getopt( sys.argv[1:], "haqpi:o:", ["help", "ascii", "quiet", "show-plots", "input=", "output="] )
    except  getopt.GetoptError, err:
        print str(err)
        usage(sys.argv[0])
        sys.exit(2)

    for o, a in opts:
        if o == "-h" :
            usage(sys.argv[0])
            sys.exit()
        elif o in ("-i", "--input"):
            partran_file = a
        elif o in ("-o", "--output"):
            track_file = a
        elif o in ("-q", "--quiet"):
            quiet = True
        elif o in ("-a", "--ascii"):
            ascii = True
        elif o in ("-p", "--show-plots"):
            showplots = True
        else:
            assert False, "unhandled option"

    f = open(partran_file, 'rb')

    data = struct.unpack("<B", f.read(1))
    data = struct.unpack("<B", f.read(1))

    data = struct.unpack("<i", f.read(4) )
    np = int(data[0])

    data = struct.unpack("<d", f.read(8) )
    ib   = float(data[0])

    data  = struct.unpack("<d", f.read(8))
    fbase = float(data[0])

    data = struct.unpack("<B", f.read(1))

    # read particle state data 

    partran_dist = numpy.arange(6*np, dtype='float64').reshape(6,np)

    for i in range(np) :
        data = f.read(48)
        data = struct.unpack("<dddddd", data )
        partran_dist[0,i] =  data[0]     
        partran_dist[1,i] =  data[1]     
        partran_dist[2,i] =  data[2]     
        partran_dist[3,i] =  data[3]     
        partran_dist[4,i] =  data[4]     
        partran_dist[5,i] =  data[5]     

    data = struct.unpack("<d", f.read(8))
    m0c2 = data[0]

    Wav =  partran_dist[5,:].mean()

    c = 2.998e8 # speed of light in m/s

    lmbda = c/(fbase*1.0e6)* 1000 # wavelength in vacuum, in mm

    gma     = Wav/ m0c2 + 1 
    betgma =  sqrt(gma*gma -1)
    beta   =  betgma/gma

    if (not quiet ) :
        print '# Wav [MeV] = %7.4f'  % Wav 
        print '# gma       = %7.4f'  % gma
        print '# beta      = %7.4f'  % beta
        print '# betgma    = %7.4f\n'% betgma

        print '# no of pseudo-particles   = %7i'     % np 
        print '# peak beam current  [mA ] = %7.4f'   % ib
        print '# base frequency     [MHz] = %7.4f'   % fbase
        print '# particle mass [MeV/c**2] = %7.4f\n' % m0c2

    xcov = numpy.cov(partran_dist[0,:],partran_dist[1,:] )
    ycov = numpy.cov(partran_dist[2,:],partran_dist[3,:] )
    zcov = numpy.cov(partran_dist[4,:],partran_dist[5,:] )

    if (not quiet ) :
        print '# Partran distribution:'
        print '# ---------------------'

        print '# (sqrt<(x-xav)2     >  )  [cm  ] = %7.4f' % sqrt(xcov[0,0]) 
        print '# (sqrt<(y-yav)2     >  )  [cm  ] = %7.4f' % sqrt(ycov[0,0]) 
        print '# (sqrt<(phi-phiav)2 >  )  [rad ] = %7.4f' % sqrt(zcov[0,0]) 

        print '# (sqrt<(xp-xpav)2   >  )  [rad ] = %7.4f' % sqrt(xcov[1,1]) 
        print '# (sqrt<(yp-ypav)2   >  )  [rad ] = %7.4f' % sqrt(ycov[1,1]) 
        print '# (sqrt<(dW-dWav)2   >  )  [MeV ] = %7.4f' % sqrt(zcov[1,1]) 

    (xmin,xmax)     = ( partran_dist[0,:].min(), partran_dist[0,:].max() )
    (xpmin,xpmax)   = ( partran_dist[1,:].min(), partran_dist[1,:].max() )
    (ymin,ymax)     = ( partran_dist[2,:].min(), partran_dist[2,:].max() )
    (ypmin,ypmax)   = ( partran_dist[3,:].min(), partran_dist[3,:].max() )
    (phimin,phimax) = ( partran_dist[4,:].min(), partran_dist[4,:].max() )
    (dWmin,dWmax)   = ( partran_dist[5,:].min()-Wav, partran_dist[5,:].max()-Wav )


    if (not quiet ) :
        print '# (xmin,   xmax )  [cm ] = (%7.4f, %7.4f)  [sigmas, sigmas]  =  (%7.4f, %7.4f)'   % (xmin, xmax,
                                                                                          xmin/sqrt(xcov[0,0]), xmax/sqrt(xcov[0,0]) ) 
        print '# (xpmin,  xpmax)  [rad] = (%7.4f, %7.4f)  [sigmas, sigmas]  =  (%7.4f, %7.4f)'   % (xpmin, xpmax,
                                                                                          xpmin/sqrt(xcov[1,1]), xpmax/sqrt(xcov[1,1]) ) 
        print '# (ymin,   ymax )  [cm ] = (%7.4f, %7.4f)  [sigmas, sigmas]  =  (%7.4f, %7.4f)'   % (ymin, ymax,
                                                                                          ymin/sqrt(ycov[0,0]), ymax/sqrt(ycov[0,0]) )
        print '# (ypmin,  ypmax)  [rad] = (%7.4f, %7.4f)  [sigmas, sigmas]  =  (%7.4f, %7.4f)'   % (ypmin, ypmax,
                                                                                          ypmin/sqrt(ycov[1,1]), ypmax/sqrt(ycov[1,1]) ) 
        print '# (phimin, phimax) [rad] = (%7.4f, %7.4f)  [sigmas, sigmas]  =  (%7.4f, %7.4f)'   % (phimin, phimax,
                                                                                          phimin/sqrt(zcov[0,0]), phimax/sqrt(zcov[0,0]) ) 
        print '# (dWmin,   dWmax) [MeV] = (%7.4f, %7.4f)  [sigmas, sigmas]  =  (%7.4f, %7.4f)\n' % (dWmin, dWmax,
                                                                                          dWmin/sqrt(zcov[1,1]),  dWmax/sqrt(zcov[1,1]) ) 


    epsx  = sqrt( xcov[0,0]*xcov[1,1] - xcov[0,1]*xcov[1,0] )
    epsnx = epsx*betgma

    bx   =   xcov[0,0]/epsx
    ax   =  -xcov[0,1]/epsx

    epsy  = sqrt( ycov[0,0]*ycov[1,1] - ycov[0,1]*ycov[1,0] )
    epsny = epsy*betgma

    by   =   ycov[0,0]/epsy
    ay   =  -ycov[0,1]/epsy

    epsz  = sqrt( zcov[0,0]*zcov[1,1] - zcov[0,1]*zcov[1,0] )
    epsz_degMeV  = epsz * (360/(2*pi)) 
    epsnz =  epsz_degMeV * lmbda / 360.0 * (1.0/m0c2)

    bz   =   zcov[0,0]/epsz
    az   =  -zcov[0,1]/epsz
    az   =  -az # note the sign change due to the fact that dz = -dphi*(lambda*beta)/(2*pi)

    if (not quiet ) :
        print '# Normalized Emittances'
        print '# ---------------------'

        print '# epsnx [cm-rad ] = %7.4e   epsnx [mm-mrad ] = %7.4f'%  (epsnx,         epsnx*10*1000)  
        print '# epsny [cm-rad ] = %7.4e   epsny [mm-mrad ] = %7.4f'%  (epsny,         epsny*10*1000)  
        print '# epsnz [deg-MeV] = %7.4e   epsnz [mm-mrad ] = %7.4f\n'%  (epsz_degMeV,   epsnz*1000)  

        print '# twiss parameters'
        print '# ----------------'

        print '# ax = %7.4f   bx  [cm/rad]  = %7.4f bx  [mm/mrad] = %7.4f'% (ax, bx, bx*0.01)
        print '# ay = %7.4f   by  [cm/rad]  = %7.4f by  [mm/mrad] = %7.4f'% (ay, by, by*0.01)
        print '# az = %7.4f   bz  [rad/MeV] = %7.4f bz  [mm/mrad] = %7.4f\n'% (az, bz, bz * lmbda * m0c2 * betgma**3/(2*pi)*0.001)  
    
    #-------------------------------------------------------------
    # NOTE: Wtmp is in keV/u 
    # u = unified atomic mass unit
    # 1 u = mu = 1/12 m(12C)
    # 1 u = 931.494 028(23) MeV/c**2
    # For H- ion
    # proton   mass  = 938.272 013 MeV/c**2 = 1.00727 u
    # electron mass  = 0.511       MeV/c**2 = 5.49 e-4
    # Total = 1.00837
    #-------------------------------------------------------------

    u     = 931.494028 # MeV/c**2
    Amass = m0c2/u
    Wtmp  = Wav*1000/Amass # keV/u 
     
    nqtot  = 1 # total no of  species in the beam 
    harm0  = 1 # harmonic w/r to base frequency 

    npat = numpy.zeros(nqtot, dtype='int32' )  # integer
    qq   = numpy.zeros(nqtot, dtype='float64') # double ?

    npat[0] = np
    qq[0]   = -1.0  

    g0   = 1.0 + Wav/m0c2    
    bg0  = sqrt(g0*g0-1.0) # normalized momentum

    trackfile = open(track_file, "wb")

    if ascii:
        print '#' 
        print '# TRACKv39 Particle Distribution'
        print '#'
        print '#%18s %19s %19s %19s %19s %19s %19s'% ('x [cm]', 'xp [cm]', 'y [cm]', 'yp [cm]', 'psi [rad]', 'beta*gamma', 'spin')
        print '#' 
        print '# number of particles : %8d'%  (npat[0]+1)
        print '# charge [e]          : %8f'%  (qq[0])
        print '#'
        print "% 16.5f % 12d" %  (Wtmp, nqtot)
        print "% 12d " % npat[0]
        print "% 12d " % qq[0]
    else:
        data = struct.pack('=IdiI', 12, Wtmp, nqtot, 12)
        trackfile.write(data)
        data = struct.pack('=IiI', 4, npat[0], 4)
        trackfile.write(data)
        data = struct.pack('=IdI', 8, qq[0], 8)
        trackfile.write(data)

    if ascii:
        print "% 16.12e % 16.12e % 16.12e % 16.12e % 16.12e % 16.12e % 16.12e" % (0.0, 0.0, 0.0, 0.0, 0.0, bg0, 0.0)
    else:
        data = struct.pack('=IdddddddI', 56, 0.0, 0.0, 0.0, 0.0, 0.0, bg0, 0.0, 56)
        trackfile.write(data)

    for iq in range(nqtot) :
        for i in range(npat[iq]) :
            x    = partran_dist[0,i] 
            xp   = partran_dist[1,i] 
            y    = partran_dist[2,i] 
            yp   = partran_dist[3,i] 
            csi  = partran_dist[4,i]/harm0
            g    = 1.0 + partran_dist[5,i]/m0c2    
            bg   = sqrt(g*g-1.0) # normalized momentum
            spin = 0.0
            if ascii:
                print "% 16.12e % 16.12e % 16.12e % 16.12e % 16.12e % 16.12e % 16.12e" % (x,xp,y,yp,csi,bg,spin)
            else:
                data = struct.pack('=IdddddddI', 56, x,xp,y,yp,csi,bg,spin, 56)
                trackfile.write(data)
                
    trackfile.close()  

    if showplots: 
        scatter_plot( partran_dist[0,:], partran_dist[1,:], 'x - x'   )
        scatter_plot( partran_dist[2,:], partran_dist[3,:], 'y - y'   )
        scatter_plot( partran_dist[4,:], partran_dist[5,:], 'phi - dW')

    if (not quiet ) :
        print 'All done.'

#---------------------------------------------------------------------------------

if __name__ == "__main__" :
    main()
