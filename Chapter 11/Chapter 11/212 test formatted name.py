
from chapter 11 211 testing a function import get ormatted name

def test_first_last_name():
    """Test that a first and last name are formatted correctly."""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
``
