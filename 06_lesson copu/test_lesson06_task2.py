from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    # 1. Откройте страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    # 2. Найдите и нажмите на кнопку "Start"
    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()

    # 3. Дождитесь появления текста "Hello World!"
    wait = WebDriverWait(driver, 15)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish")))

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("dynamic_loading_result.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    result_text = driver.find_element(By.CSS_SELECTOR, "#finish").text
    assert result_text == "Hello World!"

    driver.quit()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    base = "https://gitflic.ru/"
    driver.get(base)  # обязательно открыть домен перед добавлением cookie
    # COOKIE для пользователей
    USER1_COOKIES = [
        {"name": "SESSION",
         "value":"aeb6aa77-1df3-4548-a12b-21492f21a4cf",
         "path": "/"}
    ]
    USER2_COOKIES = [
        {"name": "SESSION",
         "value": "2d624867-44ee-45a3-a050-08ac59e7676d;",
         "path": "/"}
    ]

    # Очистим существующие cookie и установим cookie пользователя 1
    driver.delete_all_cookies()
    for c in USER1_COOKIES:
        driver.add_cookie({k: c[k] for k in ("name", "value", "path",
                                             "domain", "expiry", "secure",
                                             "httpOnly") if k in c})
    driver.refresh()  # применить cookie

    # Перейти на профиль пользователя 1
    PROFILE1 = base + "Oksana1980"
    driver.get(PROFILE1)
    wait.until(EC.url_contains("Oksana1980"))
    url1 = driver.current_url

    # Разлогиниться — удалить все cookie и обновить страницу
    driver.delete_all_cookies()
    driver.refresh()

    # Установить cookie пользователя 2
    for c in USER2_COOKIES:
        driver.add_cookie({k: c[k] for k in ("name", "value", "path",
                                             "domain", "expiry", "secure",
                                             "httpOnly") if k in c})
    driver.refresh()

    # Перейти на профиль пользователя 2
    PROFILE2 = base + "misineva"
    driver.get(PROFILE2)
    wait.until(EC.url_contains("misineva"))
    url2 = driver.current_url

    # Проверка: URLы должны различаться
    assert url1 != url2, f"{url1}"

    driver.quit()