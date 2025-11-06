import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix)

# Load the analyzed dataset
df = pd.read_csv(r"F:\Genie_Chatbot\Datasets\analyzed_dataset.csv")

# === Intent Evaluation ===
print("\n=== Intent Evaluation ===")
intent_accuracy = accuracy_score(df["intent"], df["detected_intent"])
print(f"Intent Accuracy: {intent_accuracy:.2%}")
print("\nClassification Report (Intent):")
print(classification_report(df["intent"], df["detected_intent"]))

# === Sentiment Evaluation ===
print("\n=== Sentiment Evaluation ===")
sentiment_accuracy = accuracy_score(df["sentiment"], df["detected_sentiment"])
print(f"Sentiment Accuracy: {sentiment_accuracy:.2%}")
print("\nClassification Report (Sentiment):")
print(classification_report(df["sentiment"], df["detected_sentiment"]))

# === Confusion Matrix Plot Function ===
def plot_confusion_matrix(y_true, y_pred, labels, title):
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    fig, ax = plt.subplots(figsize=(len(labels) * 0.6 + 1, len(labels) * 0.6 + 1))
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    ax.set(
        xticks=np.arange(len(labels)),
        yticks=np.arange(len(labels)),
        xticklabels=labels,
        yticklabels=labels,
        xlabel='Predicted',
        ylabel='True',
        title=title
    )
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, str(cm[i, j]), ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    plt.show()

# Plot Confusion Matrices
intent_labels = sorted(df['intent'].unique())
plot_confusion_matrix(df['intent'], df['detected_intent'], intent_labels, 'Intent Confusion Matrix')

sentiment_labels = sorted(df['sentiment'].unique())
plot_confusion_matrix(df['sentiment'], df['detected_sentiment'], sentiment_labels, 'Sentiment Confusion Matrix')
