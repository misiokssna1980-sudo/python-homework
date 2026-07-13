import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Тест", "Тест"),                    
    ("123", "123"),                     
    ("04 апреля 2023", "04 апреля 2023")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),                           
    (" ", " ")                          
])
def test_capitalize_negative_strings(input_str, expected):
    assert string_utils.capitalize(input_str) == expected    


@pytest.mark.negative
def test_capitalize_negative_none():
    with pytest.raises((TypeError, AttributeError)): 
        string_utils.capitalize(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Тест", "Тест"),
    ("  123", "123"),
    ("  04 апреля 2023", "04 апреля 2023")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", "")
])
def test_trim_negative_strings(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_negative_none():
    with pytest.raises((TypeError, AttributeError)):
        string_utils.trim(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
    ("123", "2", True),
    ("04 апреля 2023", "апреля", True),
    ("Тест", "х", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "a", False),
    (" ", " ", True),
    (None, "a", False),
    ("Skypro", None, False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "k", "sypro"),
    ("123abc123", "123", "abc"),
    ("04 апреля 2023", " ", "04апреля2023"),
    ("Тест", "а", "Тест"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "a", ""),
    ("   ", " ", ""),
    (None, "a", ""),
    ("skypro", None, "skypro"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
