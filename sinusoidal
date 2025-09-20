import numpy as np
import matplotlib.pyplot as plt

fs = 8000          # Sampling frequency (Hz)
f = 440            # Signal frequency (Hz)
duration = 0.5     # seconds
L = 5              # Window length for moving average

t = np.arange(0, duration, 1/fs)

x = np.sin(2 * np.pi * f * t)

noise_strength = 0.5
x_noisy = x + noise_strength * np.random.randn(len(t))

def moving_average(signal, L):
    kernel = np.ones(L) / L
    return np.convolve(signal, kernel, mode='same')

y = moving_average(x_noisy, L)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title("Original Sinusoidal Signal (440 Hz)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 2)
plt.plot(t, x_noisy)
plt.title(f"Noisy Signal (Noise Strength = {noise_strength})")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(3, 1, 3)
plt.plot(t, y, color='orange')
plt.title(f"Smoothed Signal (Moving Average, L={L})")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
