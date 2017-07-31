import numpy as np
import matplotlib.pyplot as plt

signal = np.zeros(1024)
signal = 10
signal = signal + np.random.randn(1024)
selected = []
for i in range(100):
    while True:
        index = np.random.choice(1024)
        if index not in selected:
            selected.append(index)
            signal[index] = signal[index] + 10 * np.random.random() - 5
            break
fft_signal = np.fft.fft(signal)
plt.figure(1)
plt.plot(signal)
plt.figure(2)
plt.plot(np.log(fft_signal))
fft_signal[1:] = 0. + 0.j
recovered_signal = np.fft.ifft(fft_signal)
plt.figure(3)
plt.plot(recovered_signal)
plt.show()


