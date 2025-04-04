🎶 What the Program Does (Big Picture)
This is a song recognition system. Here's what it does:

Reads songs or clips as input.
Converts audio into a spectrogram using FFT (Fourier Transform).
Finds peaks in the spectrogram (these represent dominant frequencies).
Pairs peaks into landmarks (time-frequency "fingerprints").
Matches fingerprints between the sample clip and known songs.
Outputs the best match by comparing how many fingerprints overlap.
