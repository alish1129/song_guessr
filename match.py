import json
from fingerprint import get_fingerprints, get_fingerprints_with_fft


def load_database(db_file='fingerprints_db.json'):
    try:
        with open(db_file, 'r') as f:
            return json.load(f)
    except:
        return {'None found'}


def match_clip(clip_path, db_file='fingerprints_db.json'):

    """
        Now that you have fingerprints from the clip and fingerprints stored for full songs, you:
        Extract all hashes from the clip.
        Compare them to each song's fingerprints.
        Count how many hashes match.
    :param clip_path: path to the clip file
    :param db_file: path to the database file
    :return:
    """
    S, peaks, clip_fps = get_fingerprints_with_fft(clip_path)
    database = load_database(db_file)

    scores = {}
    for fp, _ in clip_fps:
        for song_name, song_fps in database.items():
            if fp in song_fps:
                scores[song_name] = scores.get(song_name, 0) + 1

    print(scores)

    if not scores:
        print("No match found")
        return None, None

    best_match = max(scores, key=scores.get)
    print(f"Best match for {clip_path}: {best_match} with {scores[best_match]} matching fingerprints")
    return S, peaks
