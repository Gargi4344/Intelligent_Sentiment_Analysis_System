
"""
Centralized logging configuration.
"""

import logging

class AppLogger:
    def __init__(self):
        self.logger = logging.getLogger("SentimentSystem")
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
