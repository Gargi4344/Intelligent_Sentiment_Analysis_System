
"""
Text preprocessing engine.
Includes normalization, noise removal, stopword filtering, and sanitation.
"""

import re

class TextPreprocessor:
    def __init__(self):
        self.stopwords = {
            "the","is","and","a","to","of","in","it","that","this","for","on"
        }

    def clean(self, text: str) -> str:
        text = text.lower()
        text = self._remove_urls(text)
        text = self._remove_special_chars(text)
        text = self._remove_stopwords(text)
        text = self._normalize_whitespace(text)
        return text

    def _remove_urls(self, text: str) -> str:
        return re.sub(r"http\S+", "", text)

    def _remove_special_chars(self, text: str) -> str:
        return re.sub(r"[^a-z\s]", "", text)

    def _remove_stopwords(self, text: str) -> str:
        words = text.split()
        filtered = [w for w in words if w not in self.stopwords]
        return " ".join(filtered)

    def _normalize_whitespace(self, text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()
