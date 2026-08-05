from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds: str):
        """Очищает поле задержки и вводит новое значение."""
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, text: str):
        """Находит кнопку калькулятора по её тексту и кликает."""
        # Используем поиск по тексту на кнопке (например, "7", "+", "=")
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    def get_result(self, timeout_seconds: int) -> str:
        """Ожидает появления результата в течение указанного времени и возвращает его."""
        # Ждем, пока текст в поле результата перестанет быть пустым или обновится
        result_locator = (By.CSS_SELECTOR, ".screen")
        WebDriverWait(self.driver, timeout_seconds + 5).until(
            EC.text_to_be_present_in_element(result_locator, "15")
        )
        return self.driver.find_element(*result_locator).text
