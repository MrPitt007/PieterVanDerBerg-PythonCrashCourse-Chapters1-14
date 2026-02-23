 Chapter 11/220 test anonymous survey single.py

from chapter 11 218_anonymous survey class import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)

    language_survey.store_response('English')

    assert 'English' in language_survey.responses
