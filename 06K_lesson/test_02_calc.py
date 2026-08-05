import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Открываем тест в браузере Google Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_02_calc(driver):
    # 1. Открываем страницу калькулятора
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. В поле ввода по локатору #delay вводим значение 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()  # Очищаем поле от стандартного значения
    delay_input.send_keys("45")

    # Вспомогательная функция для клика по кнопкам калькулятора по тексту на них
    def click_button(text):
        driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    # 3. Нажимаем на кнопки: 7, +, 8, =
    click_button("7")
    click_button("+")
    click_button("8")
    click_button("=")

    # 4. Проверяем (assert), что в окне отобразится результат 15 через 45 секунд
    # Используем явное ожидание с таймаутом 50 секунд (с небольшим запасом)
    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Дополнительная финальная проверка значения на экране калькулятора
    result_screen = driver.find_element(By.CLASS_NAME, "screen").text
    assert result_screen == "15", f"Ожидался результат '15', но на экране: '{result_screen}'"