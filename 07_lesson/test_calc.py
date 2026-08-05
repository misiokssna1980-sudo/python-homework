import pytest
from selenium import webdriver
from calc_page import CalcPage


@pytest.fixture
def driver():
    """Фикстура для создания и автоматического закрытия браузера."""
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_slow_calculator(driver):
    # Создаем объект страницы
    calc_page = CalcPage(driver)

    # Шаг 1. Открыть страницу калькулятора
    calc_page.open()

    # Шаг 2. Ввести значение 45 в поле задержки
    calc_page.set_delay("45")

    # Шаг 3. Нажать кнопки: 7, +, 8, =
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    # Шаг 4. Получить результат с ожиданием в 45 секунд
    result = calc_page.get_result(45)

    # Проверяем результат (assert разрешен только тут!)
    assert result == "15"
