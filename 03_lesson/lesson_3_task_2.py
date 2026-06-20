class Smartphone:

    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number


catalog = [
    Smartphone("Apple", "iPhone 12", "+79162648296"),
    Smartphone("Samsung", "Galaxy S24", "+79222222222"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79333333333"),
    Smartphone("Google", "Pixel 8", "+79444444444"),
    Smartphone("Huawei", "Pura 70", "+79555555555")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
