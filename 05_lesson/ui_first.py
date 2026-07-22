import time
from selenium import webdriver


# Современный способ. Selenium Manager автоматически настроит драйвер
driver = webdriver.Chrome()

# Открываем страницу
driver.get("https://www.google.com")

# Ждем 5 секунд (чтобы увидеть результат)
time.sleep(5)

# Закрываем браузер
driver.quit()


from selenium import webdriver

driver = webdriver.Chrome()

# Открываем страницу
driver.get("https://www.google.com")

# Выводим заголовок страницы
print("Заголовок:", driver.title)

# Выводим текущий URL
print("URL:", driver.current_url)

# Обновляем страницу
driver.refresh()

# Закрываем браузер
driver.quit()