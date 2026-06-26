from address import Address
from mailing import Mailing

from_adr = Address("101000", "Москва", "Тверская", "12", "5")

to_adr = Address("190000", "Санкт-Петербург", "Невский проспект", "45", "18")

shipment = Mailing(to_address=to_adr, from_address=from_adr, cost=350, track="RU123456789ГД")

print(
    f"Отправление {shipment.track} из "
    f"{shipment.from_address.index}, {shipment.from_address.city}, "
    f"{shipment.from_address.street}, {shipment.from_address.house} - "
    f"{shipment.from_address.apartment} в {shipment.to_address.index}, "
    f"{shipment.to_address.city}, {shipment.to_address.street}, "
    f"{shipment.to_address.house} - {shipment.to_address.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)