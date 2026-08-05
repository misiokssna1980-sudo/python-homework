import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # 1. Открываем сайт магазина в браузере FireFox
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    # 9. Закрываем браузер по завершении теста
    driver.quit()

def test_03_shop(driver):
    # Открываем сайт
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизуемся как пользователь standard_user
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")  # Стандартный пароль для демо-сайта
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # Ждем загрузки каталога товаров
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_list"))
    )

    # 3. Добавляем в корзину товары
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-onesie']").click()

    # 4. Переходим в корзину
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    # 5. Нажимаем Checkout
    driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()

    # 6. Заполняем форму своими данными
    driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']").send_keys("Оксана")
    driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("Мисинева")
    driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']").send_keys("143600")

    # 7. Нажимаем кнопку Continue
    driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()

    # Ждем загрузки финальной страницы оформления заказа
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
    )

    # 8. Читаем со страницы итоговую стоимость (Total)
    # На странице текст имеет формат "Total: $58.29"
    total_label_text = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text

    # 10. Проверяем, что итоговая сумма равна $58.29
    assert "Total: $58.29" in total_label_text, f"Ожидалась сумма '$58.29', но получено: '{total_label_text}'"