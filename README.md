## 🧠 About the Project — TalkGenie

* **Project Name:** TalkGenie
* **Type:** Intent and Sentiment-Aware Multilingual Chatbot
* **Conference:** IEEE ICICNCT 2025

### 🔍 Overview

* Designed to break **language and emotional barriers** in digital communication.
* Enables **real-time multilingual** conversations using both **speech and text**.
* Integrates **AI, NLP, and sentiment analysis** for emotionally intelligent interactions.

### 🧩 Key Features

* 🎙️ Accepts **voice and text inputs**.
* 🧠 Detects **intent** using **LLaMA3 via Ollama**.
* ❤️ Analyzes **sentiment** using **TextBlob (NLTK-based)**.
* 🌐 **Translates** responses into multiple languages using **Deep Translator**.
* 🔊 Generates **voice output** through **Google Text-to-Speech (gTTS)**.
* 💾 Maintains short-term **chat memory** with **LangSmith**.
* ⚡ Interactive **Streamlit** frontend for user-friendly experience.

### 🏗️ Core Workflow

1. Capture user input (speech/text).
2. Convert speech to text using **Whisper**.
3. Perform **sentiment analysis** with TextBlob.
4. Extract **intent** and generate responses via **LLaMA3**.
5. Translate responses using **Deep Translator**.
6. Output responses as audio through **gTTS**.

### ⚙️ Tech Stack

* **Programming:** Python 3.9+
* **Speech-to-Text:** Whisper
* **Language Model:** LLaMA3 (via Ollama)
* **Sentiment Analysis:** TextBlob / NLTK
* **Translation:** Deep Translator
* **Text-to-Speech:** gTTS
* **Frontend:** Streamlit
* **Memory:** LangSmith
* **Data Processing:** Pandas, NumPy

### 📊 Model Performance

* **Sentiment Accuracy:** 99.43%
* **Intent Accuracy:** 73.90%
* **Weighted F1-Score:** 0.80

### 🌱 Applications

* Customer service and helpdesks
* Healthcare and accessibility tools
* Education and e-learning
* Tourism and multilingual assistance

### 🔮 Future Enhancements

* Emotion detection from **voice tone**.
* **Offline functionality** and mobile deployment.
* **Long-term conversational memory**.
* **Multimodal input** (speech, text, images).
* Integration with **third-party APIs and apps**.

