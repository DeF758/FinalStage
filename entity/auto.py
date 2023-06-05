class Auto:
    def __init__(self, brand='no brand', model='no model', price=0):
        self.__brand = (brand if isinstance(brand, str) and len(brand) > 0
                        else "no brand")
        self.__model = (model if isinstance(model, str) and len(model) > 0
                        else "no model")
        self.__price = price if price >= 0 else 0

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self.__model = model

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self.__price = price

    def __str__(self):
        return f"{self.__brand}, {self.__model} - {self.__price}$"
