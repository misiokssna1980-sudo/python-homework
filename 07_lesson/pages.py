from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, item_name):
        # Преобразуем название товара в формат id кнопки (например, "Sauce Labs Backpack" -> "add-to-cart-sauce-labs-backpack")
        button_id = f"add-to-cart-{item_name.lower().replace(' ', '-')}"
        self.driver.find_element(By.ID, button_id).click()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def get_total_price(self) -> str:
        # Извлекаем текст итоговой стоимости (например, "Total: $58.29")
        return self.driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
