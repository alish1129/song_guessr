# Audio Fingerprinting Project

This project implements a simplified song recognition system that uses audio fingerprinting based on FFT and peak detection.

## 📁 Project Structure


## 🧠 How It Works

1. **Spectrogram Creation**: Uses FFT to transform audio into a time-frequency representation.
2. **Peak Detection**: Finds strong sound points (peaks) in the spectrogram.
3. **Fingerprinting**: Pairs peaks to generate unique hashes (landmarks).
4. **Database**: Stores fingerprints of known songs.
5. **Matching**: Compares a clip’s fingerprints to find the best match.
6. **Visualization**: Shows detected peaks and fingerprint pairs on spectrograms.

## 📦 Packages
- **matplotlib**:
Plotting library for creating spectrograms and overlaying peaks/landmarks.

- **streamlit**:
Easy way to build a web interface for uploading clips and displaying results interactively.

- **numpy**:
Fundamental package for numerical arrays and operations (e.g., spectrogram data).

- **librosa**:
Audio processing library; handles loading, FFT (STFT), and amplitude-to-dB conversion.

- **scipy**:
Provides signal-processing tools like stft and maximum_filter for peak detection.

## 📌 Key Files

- `fingerprint.py`: Functions for spectrogram, peak finding, and landmark generation.
- `match.py`: Compares clip fingerprints with songs in the database.
- `recognize.py`: Main program to build the DB and recognize clips.
- `visualize.py`: Spectrogram and landmark visualizations.

## 🧪 Requirements

Install required libraries using:


## ✅ Running the Project

1. Add songs to `database/`.
2. Add test clips to `clips/`.
3. Run the recognizer:

## 📈 Output

The program displays:
- Spectrograms of all songs + the clip
- Detected peak points (red dots)
- Landmark pairs (cyan lines)

## 📚 Terms

- **FFT**: Converts time-based signals into frequencies.
- **Spectrogram**: Heatmap showing frequency over time.
- **Peaks**: Loud points in the spectrogram.
- **Fingerprints**: Encoded landmark pairs used for matching.

---
