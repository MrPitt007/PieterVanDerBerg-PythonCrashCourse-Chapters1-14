 Chapter 11/221 survey fixture example.py

import pytest
from chapter 11 218 anonymous survey class import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)
