# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:39:24 2017

@author: A
"""

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

NN=1024

signal = np.zeros(NN)
signal = 10
signal = signal + np.random.randn(NN)
selected = []
for i in range(int(np.ceil(NN/10))):
    while True:
        index = np.random.choice(NN)
        if index not in selected:
            selected.append(index)
            signal[index] = signal[index] + 10 * np.random.random() - 5
            break
fft_signal = np.fft.fft(signal)
plt.figure(1)
plt.plot(signal)
plt.figure(2)
plt.plot(np.abs(fft_signal))


fft_signal[10:] = 0. + 0.j
recovered_signal =np.real( np.fft.ifft(fft_signal))
plt.figure(3)
plt.plot(recovered_signal)

plt.show()

print(np.mean(signal),recovered_signal[0])