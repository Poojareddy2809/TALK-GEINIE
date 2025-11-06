import io
import sys

from Ollama import analyze_with_ollama
from Speech_To_Text import record_and_transcribe
from Text_To_Speech import speak_text
from Translator import translate_to_languages

# Ensure proper UTF-8 output in console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Step 1: Record your speech
transcript = record_and_transcribe(duration=5)
print("Transcript:", transcript)
speak_text(transcript, lang_code='en')

# Step 2: Translate into multiple languages
target_langs = ['hi', 'ta', 'fr', 'te', 'ml', 'kn', 'bn', 'gu', 'pa', 'or', 'as', 'ur']
translations = translate_to_languages(transcript, target_langs)

# Step 3: Print and speak all translations
print("\nTranslations:")
for lang, translation in translations.items():
    print(f"[{lang.upper()}] -> {translation}")
    speak_text(translation, lang_code=lang)

# Step 4: Analyze the original English text
analysis = analyze_with_ollama(transcript)

print("\nAnalysis Result:")
for key, value in analysis.items():
    print(f"{key.capitalize()}: {value}")
    speak_text(value, lang_code='en')  # Analysis will be in English
