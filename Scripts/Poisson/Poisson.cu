#include "cuda_runtime.h"
#include <stdio.h>
#include <assert.h>
#include <iostream>
#include <fstream>
using namespace std;

inline
cudaError_t checkCuda(cudaError_t result)
{
#if defined(DEBUG) || defined(_DEBUG)
	if (result != cudaSuccess) {
		cerr<<"CUDA Runtime Error:"<<cudaGetErrorString(result)<<endl;
		assert(result == cudaSuccess);
	}
#endif
	return result;
}

bool InitCUDA()
{
	int count;

	cudaGetDeviceCount(&count);
	if (count == 0) {
		cerr << "There is no device." << endl;
		return false;
	}

	int iX;
	for (iX = 0; iX < count; iX++) {
		cudaDeviceProp prop;
		if (cudaGetDeviceProperties(&prop, iX) == cudaSuccess) {
			if (prop.major >= 1) {
				break;
			}
		}
	}

	if (iX == count) {
		cerr << "There is no device supporting CUDA 1.x." << endl;
		return false;
	}

	cudaSetDevice(iX);

	return true;
}

const int gXSize = 32, gYSize = 32, gZSize = 32;
const int gXSizeBlock = 8, gYSizeBlock = 8, gZSizeBlock = 16;
const int gSizeBlock = gXSize*gYSize*gZSize / (gXSizeBlock*gYSizeBlock*gZSizeBlock);

void CheckResults(double &error, double &maxError, double *result, double *reference,int length)
{
	maxError = 0.0;
	error = 0.0;
	for (int iNum = 0; iNum < length; ++iNum) {
		double o1Temp = result[iNum];
		double o2Temp = reference[iNum];
		error += (o1Temp - o2Temp)*(o1Temp - o2Temp);
		if (fabs(o1Temp - o2Temp) > maxError) maxError = fabs(o1Temp - o2Temp);
	}
	error = sqrt(error / (length));
}

__device__ unsigned int countBlock = 0;

__global__ void FDMCUDA(double *charge, double *potential,double interval)
{
	volatile __shared__ double sPotential[gZSizeBlock + 2][gYSizeBlock][gXSizeBlock];
	double omega = 1.0 / 6.0;
	double parameter = interval*interval/8.854187817e-12;
	int xThread = threadIdx.x;
	int yThread = threadIdx.y;
	int zThread = threadIdx.z;
	int zShared = threadIdx.z+1;
	int zSharedUp = blockDim.z + 1;
	int xGlobal = blockIdx.x*(blockDim.x - 2) + xThread;
	int yGlobal = blockIdx.y*(blockDim.y - 2) + yThread;
	int zGlobal = blockIdx.z*blockDim.z + zThread;
	int globalIdx = zGlobal * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	//int globalIdx = xGlobal * gYSize * gZSize + yGlobal * gZSize + zGlobal;
	int bottomIdx = (zGlobal + gZSize - 2) % (gZSize - 1)*gXSize * gYSize + yGlobal * gXSize + xGlobal;
	int topIdx = (zGlobal + blockDim.z) % (gZSize - 1)*gXSize * gYSize + yGlobal * gXSize + xGlobal;
	double chargeLocal = charge[globalIdx];
	int xRemainder = xThread % (blockDim.x - 1);
	int yRemainder = yThread % (blockDim.y - 1);
	int zRemainder = zThread % (blockDim.z - 1);
	bool isSection = zThread == 0 && xRemainder != 0 && yRemainder != 0;
	bool isSurface = (xThread % (blockDim.x - 3) == 1 || yThread % (blockDim.y - 3) == 1 || zRemainder == 0) && xRemainder != 0 && yRemainder != 0;
	bool isShell = (xRemainder == 0 && yRemainder != 0) || (yRemainder == 0 && xRemainder != 0);

	sPotential[zShared][yThread][xThread] = potential[globalIdx];
	if (isSection)
	{
		sPotential[0][yThread][xThread] = potential[bottomIdx];
		sPotential[zSharedUp][yThread][xThread] = potential[topIdx];
	}
	__syncthreads();
	
	double potentialLocal = sPotential[zShared][yThread][xThread];

	if (xRemainder*yRemainder!=0)
	{
		potentialLocal = (sPotential[zShared + 1][yThread][xThread] + sPotential[zShared - 1][yThread][xThread] + sPotential[zShared][yThread + 1][xThread] + sPotential[zShared][yThread - 1][xThread] + sPotential[zShared][yThread][xThread + 1] + sPotential[zShared][yThread][xThread - 1] - parameter*chargeLocal)/6.0;
	}
	__syncthreads();
	for (int i = 0; i < 1; ++i)
	{
		//potentialLocal = (sPotential[zShared + 1][yThread][xThread] + sPotential[zShared - 1][yThread][xThread] + sPotential[zShared][yThread + 1][xThread] + sPotential[zShared][yThread - 1][xThread] + sPotential[zShared][yThread][xThread + 1] + sPotential[zShared][yThread][xThread - 1] - parameter*chargeLocal) / 6.0;


		/*
		sPotential[zShared][yThread][xThread] = potentialLocal;
		if (isSurface)
		{
			potential[globalIdx] = potentialLocal;
		}
		__threadfence();
		if (isShell)
		{
			sPotential[zShared][yThread][xThread] = potential[globalIdx];
		}
		if (isSection)
		{
			sPotential[0][yThread][xThread] = potential[bottomIdx];
			sPotential[zSharedUp][yThread][xThread] = potential[topIdx];
		}
		__syncthreads();
		if (xRemainder*yRemainder != 0)
		{
			potentialLocal = (sPotential[zShared + 1][yThread][xThread] + sPotential[zShared - 1][yThread][xThread] + sPotential[zShared][yThread + 1][xThread] + sPotential[zShared][yThread - 1][xThread] + sPotential[zShared][yThread][xThread + 1] + sPotential[zShared][yThread][xThread - 1] - parameter*chargeLocal) / 6.0;
		}
		__syncthreads();

		*/
		/*if (zGlobal == 0 || zGlobal == 31){
			potentialLocal = 0;
		}*/
		
	}
	
	if (xRemainder*yRemainder != 0)
	{
		potential[globalIdx] = (sPotential[zShared - 1][yThread][xThread] - 3.06559e+014) / 6.0;
	}
	
}

__global__ void FDM2CUDA(double *charge, double *potential, double *potential2, double *error, double interval)
{
	__shared__ double sError[gZSizeBlock*gYSizeBlock*gXSizeBlock];
	double omega = 1.0 / 6.0;
	double parameter = interval*interval / 8.854187817e-12;
	int xThread = threadIdx.x;
	int yThread = threadIdx.y;
	int zThread = threadIdx.z;
	int idThread = zThread*blockDim.x*blockDim.y + yThread*blockDim.x + xThread;
	int xGlobal = blockIdx.x*blockDim.x + xThread;
	int yGlobal = blockIdx.y*blockDim.y + yThread;
	int zGlobal = blockIdx.z*blockDim.z + zThread;
	int blockSize = gridDim.x*gridDim.y*gridDim.z;
	int globalIdx = zGlobal * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	double chargeLocal = charge[globalIdx];
	int xFront = globalIdx - 1;
	int xNext = globalIdx + 1;
	int yFront = globalIdx - gXSize;
	int yNext = globalIdx + gXSize;;
	int zFront = (zGlobal + gZSize - 2) % (gZSize - 1) * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	int zNext = (zGlobal % (gZSize - 1) + 1) * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	bool notShell = (xGlobal != 0 && xGlobal != gXSize - 1 && yGlobal != 0 && yGlobal != gYSize - 1);

	double potentialLocal = 0.0;
	double potentialOld = 0.0;

	/*for (int i = 0; i < 1; ++i){
		if (notShell){
			potentialLocal = potential[xFront];
			potentialLocal += potential[xNext];
			potentialLocal += potential[yFront];
			potentialLocal += potential[yNext];
			potentialLocal += potential[zFront];
			potentialLocal += potential[zNext];
			potentialLocal = (potentialLocal - parameter*chargeLocal) / 6.0;
		}
		__syncthreads();
		if (isFirst){
			atomicInc(&countBlock, blockSize);
			while (countBlock != 0){}
		}
		__syncthreads();
		potential[globalIdx] = potentialLocal;
		__syncthreads();
		if (isFirst){
			atomicInc(&countBlock, blockSize);
			while (countBlock != 0){}
		}
		__syncthreads();
	}*/

	if (notShell){
		potentialOld = potential[globalIdx];
		potentialLocal = potentialOld + omega*(potential[xFront] + potential[xNext] + potential[yFront] + potential[yNext] + potential[zFront] + potential[zNext] - 6 * potentialOld - parameter*chargeLocal);
	}
	//sPotential[zThread][yThread][xThread] = potentialLocal;
	potential2[globalIdx] = potentialLocal;
	if (potentialLocal == 0.0){
		sError[idThread] = 0.0;
	}
	else{
		sError[idThread] = fabs((potentialLocal - potentialOld) / potentialLocal);
	}
	__syncthreads();
	for (unsigned int iNum = (blockDim.x * blockDim.y * blockDim.z) / 2; iNum > 0; iNum >>= 1){
		if (idThread < iNum){
			sError[idThread] += sError[idThread + iNum];
		}
		__syncthreads();
	}
	if (idThread == 0){
		error[blockIdx.z*gridDim.x*gridDim.y + blockIdx.y*gridDim.x + blockIdx.x] = sError[idThread] / (gZSizeBlock*gYSizeBlock*gXSizeBlock);
	}
}

__global__ void FDM3CUDA(double *charge, double *potential, double *error, double interval){
	__shared__ double sError[gZSizeBlock*gYSizeBlock*gXSizeBlock];
	double omega = 1.86/ 6.0;
	double parameter = interval*interval / 8.854187817e-12;
	int xThread = threadIdx.x;
	int yThread = threadIdx.y;
	int zThread = threadIdx.z;
	int idThread = zThread*blockDim.x*blockDim.y + yThread*blockDim.x + xThread;
	int xGlobal = blockIdx.x*blockDim.x + xThread;
	int yGlobal = blockIdx.y*blockDim.y + yThread;
	//int zGlobal = blockIdx.z*blockDim.z + zThread;
	int zGlobal = (blockIdx.z*blockDim.z + zThread) * 2 + (xGlobal + yGlobal)%2;
	int blockSize = gridDim.x*gridDim.y*gridDim.z;
	int globalIdx = zGlobal * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	double chargeLocal = -charge[globalIdx];
	int xFront = globalIdx - 1;
	int xNext = globalIdx + 1;
	int yFront = globalIdx - gXSize;
	int yNext = globalIdx + gXSize;;
	int zFront = (zGlobal + gZSize - 2) % (gZSize - 1) * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	int zNext = (zGlobal % (gZSize - 1) + 1) * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	bool notShell = (xGlobal != 0 && xGlobal != gXSize - 1 && yGlobal != 0 && yGlobal != gYSize - 1 && zGlobal != gZSize - 1);
	//bool notShell = (xGlobal != 0 && xGlobal != gXSize - 1 && yGlobal != 0 && yGlobal != gYSize - 1 && zGlobal != gZSize - 1 && zGlobal != 0);

	double potentialLocal = 0.0;
	double potentialOld = 0.0;

	if (notShell){
		potentialOld = potential[globalIdx];
		//potentialLocal = (potential[xFront] + potential[xNext] + potential[yFront] + potential[yNext] + potential[zFront] + potential[zNext] - parameter*chargeLocal) / 6.0;

		potentialLocal = potentialOld + omega*(potential[xFront] + potential[xNext] + potential[yFront] + potential[yNext] + potential[zFront] + potential[zNext] - 6*potentialOld - parameter*chargeLocal);
		potential[globalIdx] = potentialLocal;
	}
	if (zGlobal == 0){
		potential[(gZSize - 1) * gXSize * gYSize + yGlobal * gXSize + xGlobal] = potentialLocal;
	}
	if (potentialLocal == 0.0){
		sError[idThread] = 0.0;
	}
	else{
		sError[idThread] = fabs((potentialLocal - potentialOld) / potentialLocal);
	}
	__syncthreads();
	for (unsigned int iNum = (blockDim.x * blockDim.y * blockDim.z) / 2; iNum > 0; iNum >>= 1){
		if (idThread < iNum){
			sError[idThread] += sError[idThread + iNum];
		}
		__syncthreads();
	}
	if (idThread == 0){
		error[blockIdx.z*gridDim.x*gridDim.y + blockIdx.y*gridDim.x + blockIdx.x] = sError[idThread] / (gZSizeBlock*gYSizeBlock*gXSizeBlock);
	}
}

__global__ void FDM4CUDA(double *charge, double *potential, double *error, double interval){
	__shared__ double sError[gZSizeBlock*gYSizeBlock*gXSizeBlock];
	double omega = 1.86 / 6.0;
	double parameter = interval*interval / 8.854187817e-12;
	int xThread = threadIdx.x;
	int yThread = threadIdx.y;
	int zThread = threadIdx.z;
	int idThread = zThread*blockDim.x*blockDim.y + yThread*blockDim.x + xThread;
	int xGlobal = blockIdx.x*blockDim.x + xThread;
	int yGlobal = blockIdx.y*blockDim.y + yThread;
	//int zGlobal = blockIdx.z*blockDim.z + zThread;
	int zGlobal = (blockIdx.z*blockDim.z + zThread) * 2 + (xGlobal + yGlobal+1) % 2;
	int blockSize = gridDim.x*gridDim.y*gridDim.z;
	int globalIdx = zGlobal * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	double chargeLocal = -charge[globalIdx];
	int xFront = globalIdx - 1;
	int xNext = globalIdx + 1;
	int yFront = globalIdx - gXSize;
	int yNext = globalIdx + gXSize;;
	int zFront = (zGlobal + gZSize - 2) % (gZSize - 1) * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	int zNext = (zGlobal % (gZSize - 1) + 1) * gXSize * gYSize + yGlobal * gXSize + xGlobal;
	bool notShell = (xGlobal != 0 && xGlobal != gXSize - 1 && yGlobal != 0 && yGlobal != gYSize - 1 && zGlobal != gZSize - 1);
	//bool notShell = (xGlobal != 0 && xGlobal != gXSize - 1 && yGlobal != 0 && yGlobal != gYSize - 1 && zGlobal != gZSize - 1 && zGlobal != 0);
	double potentialLocal = 0.0;
	double potentialOld = 0.0;

	if (notShell){
		potentialOld = potential[globalIdx];
		//potentialLocal = (potential[xFront] + potential[xNext] + potential[yFront] + potential[yNext] + potential[zFront] + potential[zNext] - parameter*chargeLocal) / 6.0;

		potentialLocal = potentialOld + omega*(potential[xFront] + potential[xNext] + potential[yFront] + potential[yNext] + potential[zFront] + potential[zNext] - 6 * potentialOld - parameter*chargeLocal);
		potential[globalIdx] = potentialLocal;
	}
	if (zGlobal == 0){
		potential[(gZSize - 1) * gXSize * gYSize + yGlobal * gXSize + xGlobal] = potentialLocal;
	}
	if (potentialLocal == 0.0){
		sError[idThread] = 0.0;
	}
	else{
		sError[idThread] = fabs((potentialLocal - potentialOld) / potentialLocal);
	}
	__syncthreads();
	for (unsigned int iNum = (blockDim.x * blockDim.y * blockDim.z) / 2; iNum > 0; iNum >>= 1){
		if (idThread < iNum){
			sError[idThread] += sError[idThread + iNum];
		}
		__syncthreads();
	}
	if (idThread == 0){
		error[blockIdx.z*gridDim.x*gridDim.y + blockIdx.y*gridDim.x + blockIdx.x] = sError[idThread] / (gZSizeBlock*gYSizeBlock*gXSizeBlock);
	}
}


__global__ void AvgCUDA(double *avg, double *array){
	__shared__ double sData[gSizeBlock/2];
	unsigned int idThread = threadIdx.x;
	sData[idThread] = array[idThread] + array[idThread + blockDim.x];
	for (unsigned int iNum = blockDim.x / 2; iNum > 0; iNum >>= 1){
		if (idThread < iNum){
			sData[idThread] += sData[idThread + iNum];
		}
		__syncthreads();
	}
	if (idThread == 0){
		*avg = sData[idThread] / (2 * blockDim.x);
	}
}

void InitInput(double *potential)
{
	int iPoten = 0;
	for (int iZ = 0; iZ < gZSize; ++iZ){
		for (int iY = 0; iY < gYSize; ++iY){
			for (int iX = 0; iX < gXSize; ++iX){
				if (iX*iY == 0 || iX == 31 || iY==31){
					potential[iZ*gXSize*gYSize + iY*gXSize + iX] = 0.0;
				}
				else{
					potential[iZ*gXSize*gYSize + iY*gXSize + iX] = 0.0;	
					//potential[iZ*gXSize*gYSize + iY*gXSize + iX] = (double)iPoten;
					++iPoten;
				}
			}
		}
	}
}

int main()
{
	if (!InitCUDA()) return 0;
	if (((gXSize - 2) % (gXSizeBlock - 2) != 0) || ((gYSize - 2) % (gYSizeBlock - 2) != 0) || (gZSize % gZSizeBlock != 0)) {
		cerr<<"Size error!"<<endl;
		exit(1);
	}

	double *oCharge = new double[gXSize*gYSize*gZSize];
	double *oPotential = new double[gXSize*gYSize*gZSize];
	double oInterval = 1.;

	fstream oFile("qGrid.txt", ios::in);
	if (oFile.fail()) {
		cout << "Error opening the input file!" << endl;
		exit(1);
	}
	int iNum = 0;
	while (!oFile.eof()&&iNum<32768) 
	{
		oFile >> oCharge[iNum];
		oFile >> oCharge[iNum];
		oFile >> oCharge[iNum];
		oFile >> oCharge[iNum];
		//oCharge[iNum] = (double)iNum;
	//	oCharge[iNum] = 0;
		++iNum;
	}
	oFile.close();

	//InitInput(oCharge);
	//oCharge[10 * gXSize*gYSize + 10 * gXSize + 10] = 100;
	InitInput(oPotential);

	int bytes = gXSize*gYSize*gZSize * sizeof(double);
	int iCount = 0;
	double oError=1;
	double *dCharge, *dPotential, *d2Potential, *dErrorBlock, *dError;
	checkCuda(cudaMalloc((void**)&dCharge, bytes));
	checkCuda(cudaMalloc((void**)&dPotential, bytes));
	checkCuda(cudaMalloc((void**)&d2Potential, bytes));
	//checkCuda(cudaMalloc((void**)&dErrorBlock, gSizeBlock*sizeof(double)));
	checkCuda(cudaMalloc((void**)&dErrorBlock, gSizeBlock*sizeof(double)/2));
	checkCuda(cudaMalloc((void**)&dError, sizeof(double)));
	float timeCUDA;
	cudaEvent_t startEvent, stopEvent;
	checkCuda(cudaEventCreate(&startEvent));
	checkCuda(cudaEventCreate(&stopEvent));

	//double error, maxError;

	checkCuda(cudaMemcpy(dCharge, oCharge, bytes, cudaMemcpyHostToDevice));
	checkCuda(cudaMemcpy(dPotential, oPotential, bytes, cudaMemcpyHostToDevice));

	dim3 grid((gXSize-2) / (gXSizeBlock-2), (gYSize-2) / (gYSizeBlock-2), gZSize / gZSizeBlock);
	//dim3 grid2(gXSize / gXSizeBlock, gYSize / gYSizeBlock, gZSize / gZSizeBlock);
	dim3 grid2(gXSize / gXSizeBlock, gYSize / gYSizeBlock, gZSize / (2 * gZSizeBlock));
	dim3 block(gXSizeBlock, gYSizeBlock, gZSizeBlock);

	checkCuda(cudaEventRecord(startEvent, 0));
	//FDMCUDA << <grid, block >> >(dCharge, dPotential,oInterval);
	while (oError > 1e-7&&iCount<5000){
		FDM3CUDA << <grid2, block >> >(dCharge, dPotential, dErrorBlock, oInterval);
		//FDM4CUDA << <grid2, block >> >(dCharge, d2Potential, dPotential, dErrorBlock, oInterval);
		FDM4CUDA << <grid2, block >> >(dCharge, dPotential, dErrorBlock, oInterval);
		AvgCUDA << <1, gSizeBlock / 2 >> >(dError, dErrorBlock);
		checkCuda(cudaMemcpy(&oError, dError, sizeof(double), cudaMemcpyDeviceToHost));
		++iCount;
		cout << iCount << ":\t" << oError << endl;
	}
	checkCuda(cudaEventRecord(stopEvent, 0));
	checkCuda(cudaEventSynchronize(stopEvent));
	checkCuda(cudaEventElapsedTime(&timeCUDA, startEvent, stopEvent));

	checkCuda(cudaMemcpy(oPotential, dPotential, bytes, cudaMemcpyDeviceToHost));

	cout << "Count:" << iCount << endl;
	cout << "Time:" << timeCUDA << "ms" << endl;

	oFile.open("output.txt", ios::out);
	for (int iZ=0; iZ < gZSize; ++iZ){
		for (int iY=0; iY < gYSize; ++iY){
			for (int iX=0; iX < gXSize; ++iX){
				oFile << iX << "\t" << iY << "\t" << iZ << "\t" << oPotential[iZ*gXSize*gYSize + iY*gXSize + iX] << endl;
			}
		}
	}
	oFile.close();

	checkCuda(cudaEventDestroy(startEvent));
	checkCuda(cudaEventDestroy(stopEvent));

	checkCuda(cudaFree(dCharge));
	checkCuda(cudaFree(dPotential));
	checkCuda(cudaFree(dError));
	checkCuda(cudaFree(dErrorBlock));

	delete[] oCharge;
	delete[] oPotential;

	system("pause");
}