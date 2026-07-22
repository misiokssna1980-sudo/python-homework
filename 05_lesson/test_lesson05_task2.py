from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")

    driver.maximize_window()
    # Заполнение поля "custname" значением "Оксана"
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Оксана")

    # Поиск кнопки отправки и клик на нее
    submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_btn.click()

    # Проверка изменения URL после нажатия
    submit_btn.click()
    previous_url = driver.current_url
    submit_btn.click()
    driver.quit()