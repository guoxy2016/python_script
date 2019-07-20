class Flower:
    def __init__(self, name, petal_count, price):
        self._name = name
        self._pet_count = petal_count
        self._price = price

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_petal_count(self, count):
        self._pet_count = count

    def get_petal_count(self):
        return self._pet_count

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price
