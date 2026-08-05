import pytest
from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    """Фикстура для создания и автоматического закрытия Firefox."""
    firefox_driver = webdriver.Firefox()
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


def test_shop_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открыть сайт магазина и авторизоваться
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавить в корзину три товара
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")

    # 3. Перейти в корзину и нажать Checkout
    inventory_page.go_to_cart()
    cart_page.checkout()

    # 4. Заполнить форму оформления заказа
    checkout_page.fill_form("Оксана", "Мисинева", "143600")

    # 5. Получить итоговую стоимость
    total_price = checkout_page.get_total_price()

    # Проверить, что итоговая сумма равна $58.29
    assert total_price == "Total: $58.29"