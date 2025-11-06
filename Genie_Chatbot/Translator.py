# my_translator.py

from deep_translator import GoogleTranslator


def translate_to_languages(text, target_languages):
    """
    Translates English text into a list of target languages.

    Args:
        text (str): The English input text.
        target_languages (list): List of language codes, e.g., ['hi', 'ta', 'fr','te', 'ml', 'kn', 'bn', 'gu', 'pa', 'or', 'as', 'ur']
    
    Returns:
        dict: Translations in the form {lang_code: translated_text}
    """
    if text is None:
        raise ValueError("Input text must not be None.")

    if target_languages is None:
        raise ValueError("Target languages must not be None.")

    translations = {}
    for lang in target_languages:
        if lang is None:
            raise ValueError("Target language must not be None.")
        try:
            translated = GoogleTranslator(source='en', target=lang).translate(text)
            translations[lang] = translated
        except Exception as e:
            translations[lang] = f"❌ Translation failed: {e}"
    return translations

