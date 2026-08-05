import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Тест будет запущен в браузере Edge (можно заменить на webdriver.Safari(), если тест идет на macOS)
@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_01_form(driver):
    # 1. Открываем нужную страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # Поле Zip code оставляем пустым по условию задачи

    # 2. Нажимаем кнопку Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Явное ожидание: ждем, пока форма обновится и элементы получат новые классы подсветки
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#zip.alert-danger"))
    )

    # 3. Проверяем, что поле Zip code подсвечено красным (имеет класс alert-danger)
    zip_code_element = driver.find_element(By.CSS_SELECTOR, "#zip")
    assert "alert-danger" in zip_code_element.get_attribute("class"), "Поле Zip code должно быть подсвечено красным"

    # 4. Проверяем, что остальные поля подсвечены зеленым (имеют класс alert-success)
    success_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in success_fields:
        element = driver.find_element(By.CSS_SELECTOR, f"#{field_id}")
        assert "alert-success" in element.get_attribute("class"), f"Поле {field_id} должно быть подсвечено зеленым"
