# text_to_speech.py

import os
import tempfile

from gtts import gTTS


def speak_text(text, lang_code="en"):
    try:
        tts = gTTS(text=text, lang=lang_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            return fp.name  # Return path for streamlit to play
    except Exception as e:
        print(f"[!] TTS Error: {e}")
        return None
