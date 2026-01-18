
"""
Sentiment prediction logic.
Uses NLP polarity scoring with business thresholds.
"""

from textblob import TextBlob

class SentimentModel:
    def predict(self, text: str) -> float:
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    def label(self, polarity: float) -> str:
        if polarity >= 0.2:
            return "Positive"
        elif polarity <= -0.2:
            return "Negative"
        return "Neutral"
