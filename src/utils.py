
"""
Utility helpers for validation and output formatting.
"""

def validate_input(text: str) -> bool:
    if not text or len(text.strip()) < 3:
        return False
    return True

def format_output(result: dict) -> str:
    return f"""
--- Sentiment Analysis Report ---
Original Text : {result['original_text']}
Cleaned Text  : {result['clean_text']}
Sentiment     : {result['sentiment']}
Polarity      : {result['polarity']:.4f}
Confidence    : {result['confidence']:.2f}
--------------------------------
"""
