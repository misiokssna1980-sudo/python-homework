from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT, "HTML Forms").click()
    assert driver.current_url.endswith("/forms/post")
    print(driver.current_url.endswith("/forms/post"))
    driver.back()
    assert driver.current_url == "https://httpbin.org/"
    print(driver.current_url)
    # Ваш код здесь

    driver.quit()