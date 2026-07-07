import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


class TestTrim:
    
     @pytest.mark.parametrize("input_str, expected", [
        ("   Тест", "Тест"),               
        (" 123", "123"),                      
        ("   04 апреля 2023", "04 апреля 2023")
     ])
     def test_trim_positive(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
        ("", ""),                             
        (" ", ""),                            
    ])
def test_trim_negative(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected

def test_trim_negative_none(self, utils):
        with pytest.raises(AttributeError):
            utils.trim(None)         

class TestToList:
     @pytest.mark.parametrize("input_str, delimeter, expected", [
        ("Тест,Тест2", ",", ["Тест", "Тест2"]), 
        ("123,456", ",", ["123", "456"]),
        ("04 апреля 2023,05 апреля 2023", ",", ["04 апреля 2023", "05 апреля 2023"])
    ])
     def test_to_list_positive(self, utils, input_str, delimeter, expected):
        assert utils.to_list(input_str, delimeter) == expected

        @pytest.mark.parametrize("input_str, expected", [
        ("", []),                             
        (" ", []),                            
    ])
        def test_to_list_negative_empty(self, utils, input_str, expected):
         assert utils.to_list(input_str) == expected

def test_to_list_negative_none(self, utils):
        with pytest.raises(AttributeError):
            utils.to_list(None)            
class TestContains:
     @pytest.mark.parametrize("string, symbol, expected", [
        ("Тест", "е", True),
        ("123", "2", True),
        ("04 апреля 2023", "апреля", True)
    ])
     def test_contains_positive(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

     @pytest.mark.parametrize("string, symbol, expected", [
        ("", "а", False),                     
        (" ", "а", False),                   
    ])
     def test_contains_negative(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    

def test_contains_negative_none(self, utils):
        with pytest.raises(TypeError):
            utils.contains(None, "а")   

class TestDeleteSymbol:
     @pytest.mark.parametrize("string, symbol, expected", [
        ("Тест", "Т", "ест"),
        ("123", "2", "13"),
        ("04 апреля 2023", " 2023", "04 апреля")
    ])
     def test_delete_symbol_positive(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    # --- КРИТЕРИЙ: Негативные сценарии ---
     @pytest.mark.parametrize("string, symbol, expected", [
        ("", "а", ""),                        # Пустая строка ""
        (" ", "а", " "),                       # Строка с пробелом " "
    ])
     def test_delete_symbol_negative(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

def test_delete_symbol_negative_none(self, utils):
        with pytest.raises(AttributeError):
            utils.delete_symbol(None, "а")    

class TestStartsWith:
     @pytest.mark.parametrize("string, symbol, expected", [
        ("Тест", "Т", True),
        ("123", "1", True),
        ("04 апреля 2023", "04", True)
    ])
     def test_starts_with_positive(self, utils, string, symbol, expected):
        assert utils.starts_with(string, symbol) == expected

        @pytest.mark.parametrize("string, symbol, expected", [
        ("", "Т", False),                     
        (" ", "Т", False),                    
    ])
        def test_starts_with_negative(self, utils, string, symbol, expected):
         assert utils.starts_with(string, symbol) == expected

        def test_starts_with_negative_none(self, utils):
         with pytest.raises(AttributeError):
            utils.starts_with(None, "Т")      

class TestEndsWith:
    @pytest.mark.parametrize("string, symbol, expected", [
        ("Тест", "т", True),
        ("123", "3", True),
        ("04 апреля 2023", "2023", True)
    ])
    def test_ends_with_positive(self, utils, string, symbol, expected):
        assert utils.ends_with(string, symbol) == expected

    
    @pytest.mark.parametrize("string, symbol, expected", [
        ("", "т", False),                     
        (" ", "т", False),                    
    ])
    def test_ends_with_negative(self, utils, string, symbol, expected):
        assert utils.ends_with(string, symbol) == expected

   
    def test_ends_with_negative_none(self, utils):
        with pytest.raises(AttributeError):
            utils.ends_with(None, "т")

class TestIsEmpty:
    
    
    @pytest.mark.parametrize("string, expected", [
        ("Тест", False),                      
        ("123", False),                       
        ("04 апреля 2023", False)             
    ])
    def test_is_empty_positive_cases(self, utils, string, expected):
        assert utils.is_empty(string) == expected

   
    @pytest.mark.parametrize("string, expected", [
        ("", True),                           
        (" ", True),                          
    ])
    def test_is_empty_negative_cases(self, utils, string, expected):
        assert utils.is_empty(string) == expected

    
    def test_is_empty_negative_none(self, utils):
        with pytest.raises(AttributeError):
            utils.is_empty(None) 
