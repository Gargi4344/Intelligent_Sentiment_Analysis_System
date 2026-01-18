
"""
Intelligent Sentiment Analysis System
Main application entry point.
Handles CLI interaction, validation, logging, and pipeline execution.
"""

from src.pipeline import SentimentPipeline
from src.logger import AppLogger
from src.utils import validate_input, format_output

def main():
    logger = AppLogger().get_logger()
    logger.info("Sentiment Analysis System Started")

    pipeline = SentimentPipeline()

    while True:
        user_input = input("Enter customer review (or 'exit'): ").strip()

        if user_input.lower() == "exit":
            logger.info("User exited application")
            break

        if not validate_input(user_input):
            logger.warning("Invalid input received")
            print("Invalid input. Please enter meaningful text.")
            continue

        result = pipeline.run(user_input)
        print(format_output(result))

    logger.info("System shutdown complete")

if __name__ == "__main__":
    main()
