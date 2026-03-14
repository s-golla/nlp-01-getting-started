"""
sentence_case.py

A simple NLP utility module that converts text into sentence case.
This file was created as part of a technical modification assignment.

Usage:
    uv run python src/nlp/sentence_case.py
"""


def to_sentence_case(text: str) -> str:
    """
    Convert a string into sentence case.

    Example:
        "hELLO WORLD" -> "Hello world"
    """
    if not text:
        return text

    text = text.strip()
    return text[0].upper() + text[1:].lower()


def demo():
    """
    Demonstration function to show sentence-case transformation.
    """
    sample = "tHIS IS A SAMPLE TEXT FOR TESTING."
    print("Original:", sample)
    print("Sentence case:", to_sentence_case(sample))


if __name__ == "__main__":
    demo()
