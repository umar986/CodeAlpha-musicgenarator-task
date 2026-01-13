from pathlib import Path
import numpy as np
from flask import Flask, send_file, request
from music21 import note, stream, midi

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)
MIDI_FILENAME = OUTPUT_DIR / "generated.mid"


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.route("/", methods=["GET"])
def healthcheck():
    return "Music AI Backend Running"


@app.route("/generate", methods=["GET"])
def generate_music():
    """Generate mood-based random MIDI and return it for download."""
    mood = (request.args.get("mood") or "energetic").lower()

    # Mood presets
    mood_settings = {
        "energetic": {"pitch": (65, 85), "durations": [0.25, 0.5]},
        "melancholic": {"pitch": (50, 62), "durations": [1.0, 1.5]},
        "ambient": {"pitch": (60, 72), "durations": [1.5, 2.0, 2.5]},
        "classical": {"pitch": (55, 75), "durations": [0.5, 1.0, 1.5]},
        "synthwave": {"pitch": (60, 80), "durations": [0.25, 0.5, 0.75]},
        "jazz": {"pitch": (55, 75), "durations": [0.5, 1.0, 1.5]},
        "rock": {"pitch": (60, 80), "durations": [0.25, 0.5, 0.75]},
        "lofi": {"pitch": (55, 70), "durations": [0.5, 1.0, 1.5]},
        "pop": {"pitch": (60, 80), "durations": [0.25, 0.5, 1.0]},
        "hiphop": {"pitch": (50, 75), "durations": [0.25, 0.5, 0.75]},
        "electro": {"pitch": (60, 85), "durations": [0.25, 0.5, 0.75]},
        "blues": {"pitch": (50, 70), "durations": [0.5, 1.0, 1.5]},
    }

    settings = mood_settings.get(mood, mood_settings["energetic"])

    num_notes = 50
    low_note, high_note = settings["pitch"]
    durations = settings["durations"]

    melody = stream.Stream()

    for _ in range(num_notes):
        pitch = int(np.random.randint(low_note, high_note + 1))
        duration = float(np.random.choice(durations))
        melody.append(note.Note(pitch, quarterLength=duration))

    midi_file = midi.translate.streamToMidiFile(melody)
    midi_file.open(str(MIDI_FILENAME), "wb")
    midi_file.write()
    midi_file.close()

    return send_file(
        MIDI_FILENAME,
        as_attachment=True,
        download_name=f"generated_{mood}.mid",
        mimetype="audio/midi",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


