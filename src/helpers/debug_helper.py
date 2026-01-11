import matplotlib.pyplot as plt
import numpy as np


def plot_fft(fft_data, fft_freq, freq, data_len, name="fft_graph") -> None:
    plt.figure(figsize=(12, 5))

    # Calculate magnitude spectrum
    magnitude = np.abs(fft_data)

    # Plot only positive frequencies (first half)
    positive_freq_idx = fft_freq >= 0
    plt.plot(fft_freq[positive_freq_idx], magnitude[positive_freq_idx])

    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")
    plt.title(
        f"Fourier Transform - Frequency Resolution ~ {freq / data_len:.2f} Hz (N={data_len})"
    )
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"{name}.png", dpi=100)
    plt.close()
