import numpy as np
import librosa
import hashlib

from scipy.ndimage import maximum_filter


def get_fingerprints(file_path, sr=22050):
    y, sr = librosa.load(file_path, sr=sr, mono=True)
    S = np.abs(librosa.stft(y))
    freqs, times = librosa.core.piptrack(S=S, sr=sr)

    fingerprints = []
    for t in range(0, times.shape[1], 5):  # ✅ correct: loop over time frames
        freq_indices = np.where(freqs[:, t] > np.median(freqs[:, t]))
        for idx in freq_indices[0]:
            freq = int(freqs[idx, t])
            time = t
            if freq > 0:
                hash_str = f"{freq}|{time}"
                fingerprint = hashlib.sha1(hash_str.encode()).hexdigest()[0:20]
                fingerprints.append((fingerprint, time))
    return fingerprints


def get_fingerprints_with_fft(file_path, sr=22050):
    y, sr = librosa.load(file_path, sr=sr)
    S = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))

    peaks = find_peaks(S)
    fingerprints = generate_landmarks(peaks)
    return S, peaks, fingerprints


def find_peaks(S, threshold=10):
    # S is a spectrogram (log-magnitude)
    neighborhood = np.ones((20, 20))
    local_max = maximum_filter(S, footprint=neighborhood) == S
    detected_peaks = local_max & (S > threshold)
    return np.argwhere(detected_peaks)


def generate_landmarks(peaks, fan_value=15):
    landmarks = []
    for i in range(len(peaks)):
        freq1, time1 = peaks[i]
        for j in range(1, fan_value):
            if i + j < len(peaks):
                freq2, time2 = peaks[i + j]
                t_delta = time2 - time1
                if 0 < t_delta <= 200:
                    hash_str = f"{freq1}|{freq2}|{t_delta}"
                    h = hashlib.sha1(hash_str.encode()).hexdigest()[0:20]
                    landmarks.append((h, time1))
    return landmarks


