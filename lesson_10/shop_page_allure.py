from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainShopPage:

    LOGIN_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ADD_sauce_labs_backpack_BUTTON = (
        By.NAME, 'add-to-cart-sauce-labs-backpack')
    ADD_sauce_labs_bolt_t_shirt_BUTTON = (
            By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_to_cart_sauce_labs_onesie_BUTTON = (
            By.NAME, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    @allure.step("Открытие страницы магазина")
    def open(self):
        """
        Открывает страницу магазина.
        """
        self.driver.get(self.url)

    @allure.step("Авторизация пользователя standard_user")
    def authorization(self):
        login_input = self.wait.until(EC.presence_of_element_located(
            self.LOGIN_INPUT
        ))
        login_input.send_keys("standard_user")

        password_input = self.wait.until(EC.presence_of_element_located(
            self.PASSWORD_INPUT
        ))
        password_input.send_keys("secret_sauce")

        login_button = self.wait.until(EC.presence_of_element_located(
            self.LOGIN_BUTTON
        ))
        login_button.click()

    @allure.step("Добавить в корзину товары")
    def get_add_product(self):
        self.wait.until(
          EC.presence_of_element_located(self.ADD_sauce_labs_backpack_BUTTON)
        ).click()
        self.wait.until(
            EC.presence_of_element_located(
                self.ADD_sauce_labs_bolt_t_shirt_BUTTON)
        ).click()
        self.wait.until(EC.presence_of_element_located
                        (self.ADD_to_cart_sauce_labs_onesie_BUTTON)
                        ).click()


class CartPage:
    SHOPPING_CART_BUTTON = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
    TOTAL_VALUE = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.url)

    @allure.step("Перейти в корзину")
    def get_shopping_card(self):
        self.wait.until(
            EC.presence_of_element_located(self.SHOPPING_CART_BUTTON)
        ).click()

    @allure.step("Нажать кнопку Checkout")
    def get_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

    def get_form(self):
        fist_name_input = self.wait.until(EC.presence_of_element_located(
            self.FIRST_NAME_INPUT
        ))
        fist_name_input.send_keys("Anastasiya")

        last_name_input = self.wait.until(EC.presence_of_element_located(
            self.LAST_NAME_INPUT
        ))
        last_name_input.send_keys("Belyaeva")

        postal_code_input = self.wait.until(EC.presence_of_element_located(
            self.POSTAL_CODE_INPUT
        ))
        postal_code_input.send_keys("456537")

    def get_continue(self):
        self.wait.until(
            EC.presence_of_element_located(self.CONTINUE_BUTTON)
        ).click()

    def get_total(self):
        # sleep(n) и time.sleep() в коде не используются.
        # Ожидание выполняется через Selenium WebDriverWait.
        self.wait.until(EC.presence_of_element_located(
            self.TOTAL_VALUE
        ))

    @allure.step("Получение результата")
    def get_result(self):
        self.wait.until(EC.text_to_be_present_in_element(self.TOTAL_VALUE,
                                                         "Total: $58.29"))

        result_element = self.driver.find_element(*self.TOTAL_VALUE)
        return result_element.text