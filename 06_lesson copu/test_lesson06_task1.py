from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    try:
        # 1.Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        # 2. Найдите и нажмите на кнопку "Start"
        # Используем CSS-селектор для поиска кнопки внутри блока #start
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # 3. Дождитесь появления текста "Hello World!"
        # Элемент загружается динамически, поэтому ждем его появления в DOM и видимости
        finish_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )

        # 4. Сделайте скриншот страницы
        driver.save_screenshot("dynamic_loading_success.png")

        # 5. Проверьте, что появившийся текст равен "Hello World!"
        assert (
            finish_element.text == "Hello World!"
        ), f"Ожидался текст 'Hello World!', но получен '{finish_element.text}'"

        print("Тест успешно пройден!")

    finally:
        # Гарантируем закрытие браузера даже при ошибке в тесте
        driver.quit()


# Запуск теста
if __name__ == "__main__":
    test_dynamic_loading()
