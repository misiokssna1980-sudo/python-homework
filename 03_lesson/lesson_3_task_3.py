class Address:

    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment


class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track


to_addr = Address("101000", "Москва", "Мясницкая", "12", "5")
from_addr = Address("143600", "Волоколамск", "Рижское шоссе", "25", "10")

mail = Mailing(to_addr, from_addr, 350.50, "RU123456789")

print(
    f"Отправление {mail.track} из {mail.from_address.index}, "
    f"{mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
