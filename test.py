import numpy as np

data = np.random.randn(1000)
print(np.fft.fft(data))
print(np.fft.fftfreq(1000) * 200)
