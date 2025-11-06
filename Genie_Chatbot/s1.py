import asyncio
import os

import streamlit as st

# Ensure there's a running event loop (fix for "no running event loop")
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Import your custom modules
try:
    from Ollama import analyze_with_ollama, generate_chatbot_response
    from Speech_To_Text import record_and_transcribe
    from Text_To_Speech import speak_text
    from Translator import translate_to_languages
except ImportError as e:
    st.error(f"Failed to import custom modules: {e}")
    st.stop()

# Supported languages mapping
LANGUAGES = {
    "English": "en", "Hindi": "hi", "Tamil": "ta", "Telugu": "te",
    "Malayalam": "ml", "Kannada": "kn", "Bengali": "bn", "Gujarati": "gu",
    "Punjabi": "pa", "Odia": "or", "Assamese": "as", "Urdu": "ur",
    "Marathi": "mr", "Konkani": "kok", "Maithili": "mai", "Santali": "sat",
    "Sindhi": "sd", "Manipuri (Meitei)": "mni", "Bodo": "brx", "French": "fr"
}

# Core processing function
def process_input(input_text: str, selected_lang_code: str):
    try:
        analysis = analyze_with_ollama(input_text)
        intent = analysis.get('intent', 'N/A')
        sentiment = analysis.get('sentiment', 'N/A')
        summary = analysis.get('summary', 'N/A')

        reply_original = generate_chatbot_response(input_text)
        reply_translation = translate_to_languages(reply_original, [selected_lang_code]).get(selected_lang_code, reply_original)

        return {
            'transcript': input_text,
            'intent': intent,
            'sentiment': sentiment,
            'summary': summary,
            'reply_original': reply_original,
            'reply_translation': reply_translation
        }
    except Exception as e:
        st.error(f"An error occurred during processing: {e}")
        st.exception(e)
        return None

# Message handling
def handle_message_processing(message_text: str, lang_code: str):
    if message_text and message_text.strip():
        result = process_input(message_text, lang_code)
        if result:
            st.session_state['chat_history'].insert(0, result)

# Page config
st.set_page_config(page_title="Talk to Genie", layout="centered")

# Initialize state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'text_input_message' not in st.session_state:
    st.session_state.text_input_message = ""
if 'selected_lang_code' not in st.session_state:
    st.session_state.selected_lang_code = LANGUAGES["English"]

# Header
st.image("Genie.jpg", use_container_width='auto')

# Input controls
st.subheader("📥 Input Type")
input_method = st.radio(
    "Choose input method:",
    ["💬 Text", "🎤 Microphone"],
    key="input_method_radio"
)
lang_name = st.selectbox(
    "🌍 Select Output Language",
    list(LANGUAGES.keys()),
    index=list(LANGUAGES.keys()).index("English"),
    key="output_language_select"
)
st.session_state.selected_lang_code = LANGUAGES[lang_name]

# Input area
with st.container():
    if input_method == "💬 Text":
        with st.form(key="chat_form_text", clear_on_submit=True):
            user_input_text = st.text_input("🎨 Type your message here:", key="text_input_message", value=st.session_state.text_input_message)
            if st.form_submit_button("➡️ Send"):
                handle_message_processing(st.session_state.text_input_message, st.session_state.selected_lang_code)
    else:
        st.info("Click 'Start Recording' and speak.")
        if st.button("🎤 Start Recording", key="record_button"):
            with st.spinner("Recording..."):
                try:
                    transcript = record_and_transcribe(duration=5)
                    if transcript:
                        st.success("Transcription complete!")
                        handle_message_processing(transcript, st.session_state.selected_lang_code)
                    else:
                        st.warning("Could not capture voice or transcription failed.")
                except Exception as e:
                    st.error(f"Error during voice recording/transcription: {e}")
                    st.exception(e)

# Chat history display
st.subheader("📚 Chat History")
with st.container():
    for i, entry in enumerate(st.session_state['chat_history']):
        unique_key_base = f"chat_entry_{i}"
        with st.chat_message("user"):
            st.markdown(entry.get('transcript', ''))
        with st.chat_message("assistant"):
            st.markdown(f"**Intent:** {entry.get('intent', 'N/A')}")
            st.markdown(f"**Sentiment:** {entry.get('sentiment', 'N/A')}")
            st.markdown(f"**Summary:** {entry.get('summary', 'N/A')}")
            reply_translation_text = entry.get('reply_translation', '')
            st.markdown(f"**Reply ({lang_name}):** {reply_translation_text}")

            # Play audio without 'key' argument (fixed)
            if reply_translation_text.strip():
                try:
                    audio_path_reply = speak_text(reply_translation_text, st.session_state.selected_lang_code)
                    if isinstance(audio_path_reply, str) and os.path.exists(audio_path_reply):
                        with open(audio_path_reply, 'rb') as f:
                            st.audio(f.read(), format="audio/mp3")  # removed key
                    elif isinstance(audio_path_reply, bytes):
                        st.audio(audio_path_reply, format="audio/mp3")  # removed key
                    else:
                        st.warning("Audio generation returned an unexpected format.")
                except FileNotFoundError:
                    st.error(f"Audio file not found: {audio_path_reply}")
                except Exception as audio_e:
                    st.error(f"Error displaying/playing audio: {audio_e}")
