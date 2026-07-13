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
@pytest.mark.parametrize("input_str, delimeter, expected", [
    ("Тест,Тест", ",", ["Тест", "Тест"]),
    ("1,2,3", ",", ["1", "2", "3"]),
    ("04 апреля 2023,05 апреля", ",", ["04 апреля 2023", "05 апреля"])
])
def test_to_list_positive(input_str, delimeter, expected):
    assert string_utils.to_list(input_str, delimeter) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, delimeter, expected", [
    ("", ",", []),
    (" ", ",", [" "])
])
def test_to_list_negative_strings(input_str, delimeter, expected):
    assert string_utils.to_list(input_str, delimeter) == expected


@pytest.mark.negative
def test_to_list_negative_none():
    with pytest.raises((TypeError, AttributeError)):
     string_utils.to_list(None)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, substrings, expected", [
    ("Тест", ["Тест", "123"], True),
    ("123", ["1", "2"], True),
    ("04 апреля 2023", ["апреля", "04"], True),
])
def test_contains_any_positive(input_str, substrings, expected):
    assert string_utils.contains_any(input_str, substrings) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, substrings, expected", [
    ("", ["Тест"], False),                 
    (" ", ["Тест"], False),                
    ("Тест", [], False),                   
])
def test_contains_any_negative(input_str, substrings, expected):
    assert string_utils.contains_any(input_str, substrings) == expected


@pytest.mark.negative
def test_contains_any_none():
    with pytest.raises(TypeError):
        string_utils.contains_any(None, ["Тест"])
