
"""
Pipeline orchestration module.
Coordinates preprocessing, sentiment scoring, and business rules.
"""

from .preprocessing import TextPreprocessor
from .sentiment_model import SentimentModel

class SentimentPipeline:
    def __init__(self):
        self.preprocessor = TextPreprocessor()
        self.model = SentimentModel()

    def run(self, text: str) -> dict:
        clean_text = self.preprocessor.clean(text)
        polarity = self.model.predict(clean_text)
        sentiment = self.model.label(polarity)
        confidence = abs(polarity)

        return {
            "original_text": text,
            "clean_text": clean_text,
            "polarity": polarity,
            "sentiment": sentiment,
            "confidence": confidence
        }
