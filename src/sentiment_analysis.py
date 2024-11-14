# sentiment_analysis.py
from textblob import TextBlob

def analyze_sentiment(text):
    """Returns sentiment polarity score for a given text."""
    blob = TextBlob(text)
    return blob.sentiment.polarity

def classify_sentiment(polarity):
    """Classifies sentiment as positive, neutral, or negative."""
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

