#Speech_To_Text.py

import os
import tempfile

import numpy as np
import sounddevice as sd
import whisper
from scipy.io.wavfile import write

# Load Whisper model
model = whisper.load_model("base")

def record_and_transcribe(duration=5):
    fs = 44100  # Sample rate
    print(f" Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Create a temporary WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        write(temp_audio.name, fs, recording)
        temp_path = temp_audio.name

    print(" Audio captured. Transcribing...")
    result = model.transcribe(temp_path)

    # Now safe to delete
    os.remove(temp_path)
    return result["text"]


# Example usage
if __name__ == "__main__":
    transcript = record_and_transcribe(duration=5)
    print(" You said:", transcript)
