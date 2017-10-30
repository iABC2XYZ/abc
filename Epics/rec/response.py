import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Rec.dat')
response = np.zeros((10, 14))
for i in range(14):
    for j in range(10):
        res_fit = np.polyfit(data[:, i], data[:, 14 + j], 1)
        response[j, i] = res_fit[0]
print(response)




