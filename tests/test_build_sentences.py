import pytest
import json

from pytest_mock import mocker
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)

data = {
    "adjectives": ["angry", "brave", "calm", "delightful", "eager", "fancy", "gentle", "happy", "innocent"],
    "nouns": ["apple", "banana", "cat", "dog", "elephant", "frog", "goat", "hat", "ice"],
    "verbs": ["eat", "play", "jump", "run", "sleep", "dance", "sing", "walk", "watch"],
    "adverbs": ["quickly", "slowly", "happily", "sadly", "gracefully", "eagerly", "silently", "loudly", "boldly"],
    "prepositions": ["above", "below", "behind", "near", "under", "over", "beside", "between", "inside"]
}

def test_get_seven_letter_word(mocker):
    # Mock the input function
  mock_input = mocker.patch("builtins.input", return_value="Testinput")
  # Call the function under test
  result = get_seven_letter_word()
  # Assert the result
  assert len(result) >= 7

  mock_input = mocker.patch("builtins.input", return_value="Test")
  with pytest.raises(ValueError):
     result = get_seven_letter_word()
  # Assert that the input function was called with the correct prompt
  mock_input.assert_called_once_with("Please enter a word with at least 7 letters: ")

def test_parse_json_from_file():
  file_path = "word_lists.json"

  with open(file_path, 'r') as file:
    json_data = json.load(file)
  # Call the function under test
    result =  parse_json_from_file(file_path)
    # Assert the result
    assert result == json_data

def test_choose_sentence_structure():
    choice = choose_sentence_structure()
    assert choice in structures

def test_get_pronoun(mocker):
    mock_choice = mocker.patch("random.choice",return_value="alpha")
    # assert that the choice returned is "alpha"
    assert get_pronoun() == 'alpha'
    # assert that the choice method was called once
    mock_choice.assert_called_once()

def test_get_article(mocker):
    mock_choice = mocker.patch("random.choice",return_value="alpha")
    # assert that the choice returned is "alpha"
    assert get_article() == 'alpha'
    # assert that the choice method was called once
    mock_choice.assert_called_once()

def test_get_word():
    letters = "A"
    words_list = ["apple", "banana", "cherry", "date"]  # example word list
    result = get_word(letters, words_list)
    assert result == "apple"

def test_fix_agreement():
    sentence = ["the", "day", "before", "he", "saw", "me", "with", "a", "elephant", "again"]
    fix_agreement(sentence)
    assert sentence == ["the", "day", "before", "he", "saws", "mes", "with", "an", "elephant", "again"]

def test_build_sentence(mocker):
    mocker.patch('build_sentences.get_article', return_value='a')
    mocker.patch('build_sentences.get_pronoun', return_value='he')

    # Structure and seed
    structure = ["PRO","ADV","VERB","PREP","ART","ADJ","NOUN","PREP","ART","ADJ","NOUN"]
    seed_word = "ABCDEFGHIJK"  # 9 letters

    result = build_sentence(seed_word, structure, data)

    expected = "He quickly plays behind an delightful elephant over a gentle hat"

    assert result == expected, f"Expected: '{expected}', got: '{result}'"
