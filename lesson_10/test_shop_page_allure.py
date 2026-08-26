import pytest
import allure
from selenium import webdriver
from shop_page_allure import MainShopPage
from shop_page_allure import CartPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Оформление заказа в интернет магазине: проверка итоговой суммы")
@allure.description(
    "Тест проверяет сценарий оформления заказа:"
    "авторизация,добавление товаров в корзину,"
    "переход к оформлению,заполнение формы и проверка итоговой суммы"
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(driver):
    # sleep(n) и time.sleep() в тесте не используются.
    # Ожидание выполняется средствами Page Object.
    shop_page = MainShopPage(driver, url="https://www.saucedemo.com/")
    with allure.step("Открыть главную страницу магазина"):
        shop_page.open()
    with allure.step("Авторизоваться под стандартным пользователем"):
        shop_page.authorization()
    with allure.step("Добавить товары в корзину"):
        shop_page.get_add_product()
    shop_page = CartPage(driver, url="https://www.saucedemo.com/cart.html")
    with allure.step("Перейти в корзину и начать оформление заказа"):
        shop_page.get_shopping_card()
        shop_page.get_checkout()
    with allure.step("Заполнить данные покупателя"):
        shop_page.get_form()
    with allure.step("Продолжить оформление заказа"):
        shop_page.get_continue()
    with allure.step("Дождаться отображения итоговой суммы"):
        shop_page.get_total()
    result = shop_page.get_result()
    with allure.step(f"Проверить значение итоговой суммы: {result}"):
        assert result == "Total: $58.29"