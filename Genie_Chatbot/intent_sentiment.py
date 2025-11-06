import pandas as pd
from textblob import TextBlob

# Define simple intent keywords
intent_keywords = {
    "weather": ["weather", "temperature", "rain", "forecast"],
    "music": ["song", "play", "music", "track"],
    "alarm": ["alarm", "remind", "timer", "wake"],
    "joke": ["joke", "funny", "laugh"],
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"],
    "restaurant": ["food", "restaurant", "dinner", "lunch"]
}

def detect_intent(text):
    text = text.lower()
    for intent, keywords in intent_keywords.items():
        if any(keyword in text for keyword in keywords):
            return intent
    return "unknown"

def detect_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

# === Read CSV ===
df = pd.read_csv(r"F:\Genie_Chatbot\Datasets\sample_queries.csv")  # <- replace this with your CSV

if 'query' not in df.columns:
    raise ValueError("Input CSV must have a 'query' column.")

df["predicted_intent"] = df["query"].apply(detect_intent)
df["predicted_sentiment"] = df["query"].apply(detect_sentiment)

# Save
df.to_csv("queries_with_intent_sentiment.csv", index=False)
print(" Results saved to queries_with_intent_sentiment.csv")
