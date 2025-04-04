import math

import matplotlib.pyplot as plt


def plot_all_spectrograms(data_list):
    """
    Plot all spectrograms in a list.
    :param data_list:
    :return:
    """
    n = len(data_list)
    cols = 2
    rows = math.ceil(n / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(16, 4 * rows))
    axes = axes.flatten()  # to access axes[i] linearly

    for i, (S, peaks, title) in enumerate(data_list):
        ax = axes[i]
        ax.imshow(S, aspect='auto', origin='lower', cmap='viridis')
        if peaks.any():
            y_vals, x_vals = zip(*peaks)
            ax.scatter(x_vals, y_vals, color='red', s=10)
        ax.set_title(title)
        ax.set_xlabel("Time Frame")
        ax.set_ylabel("Frequency Bin")

    # Hide any extra empty subplots
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()


def show_peaks_on_spectrogram(S, peaks, title="Spectrogram with Peaks"):
    """
    Show the spectrogram with peaks highlighted.
    :param S:
    :param peaks:
    :param title:
    :return:
    """
    plt.figure(figsize=(12, 5))
    plt.imshow(S, aspect='auto', origin='lower', cmap='viridis')
    y_vals, x_vals = zip(*peaks)
    plt.scatter(x_vals, y_vals, color='red', s=10)
    plt.title(title)
    plt.xlabel("Time Frame")
    plt.ylabel("Frequency Bin")
    plt.colorbar()
    plt.tight_layout()
    plt.show()

