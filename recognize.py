import os
import json

from fingerprint import get_fingerprints_with_fft
from match import match_clip
from plotter import plot_all_spectrograms
import streamlit as st

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


def recognize(clip_path):
    progress_text = "Initializing database..."
    my_bar = st.progress(0, text=progress_text)
    spec_data = []

    print("Building database...")
    for filename in os.listdir('database'):
        if filename.endswith('.mp3'):
            path = os.path.join('database', filename)
            song_name = os.path.splitext(filename)[0]
            if song_name in ['None found', 'fingerprints_db.json']:
                S, peaks = add_song_to_db(path, song_name)
                spec_data.append((S, peaks, song_name))

    my_bar.progress(25, text="Database built. Now recognizing clip...")

    print("\nRecognizing clip...")
    clipS, clipPeaks, best_match = match_clip(clip_path)
    S, peaks, fingerprints = get_fingerprints_with_fft('database/' + best_match + '.mp3')

    spec_data.append((S, peaks, best_match))

    my_bar.progress(75, text="Clip recognized. Now plotting...")

    if clipS is None:
        print("No match found for the clip.")
        return
    spec_data.append((clipS, clipPeaks, "Clip - Fingerprint Peaks"))

    img = plot_all_spectrograms(spec_data)
    my_bar.progress(90, text="Plotting complete. Preparing results...")

    return best_match, img, my_bar


