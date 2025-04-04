import os
import json

from fingerprint import get_fingerprints, get_fingerprints_with_fft
from match import match_clip
from plotter import plot_all_spectrograms

DB_FILE = 'fingerprints_db.json'


def add_song_to_db(song_path, song_name):
    db = {}
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            db = json.load(f)

    S, peaks, fingerprints = get_fingerprints_with_fft(song_path)
    db[song_name] = [fp for fp, _ in fingerprints]

    with open(DB_FILE, 'w') as f:
        json.dump(db, f)
    print(f"Added {song_name} to database.")
    return S, peaks


def main():
    spec_data = []

    print("Building database...")
    for filename in os.listdir('database'):
        if filename.endswith('.mp3'):
            path = os.path.join('database', filename)
            song_name = os.path.splitext(filename)[0]
            S, peaks = add_song_to_db(path, song_name)
            spec_data.append((S, peaks, song_name))

    print("\nRecognizing clip...")
    clipS, clipPeaks = match_clip('clips/clip_03.mp3')

    if clipS is None:
        print("No match found for the clip.")
        return
    spec_data.append((clipS, clipPeaks, "🎧 Clip - Fingerprint Peaks"))

    plot_all_spectrograms(spec_data)



if __name__ == '__main__':
    main()
