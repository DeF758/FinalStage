from entity.auto import Auto


class BudgetCar(Auto):
    def __init__(self, brand='no brand', model='no model', price=0,
                 fuel_consumption=1, trunk_capacity=10):
        super().__init__(brand, model, price)
        self.__fuel_consumption = fuel_consumption if fuel_consumption > 0 else 1
        self.__trunk_capacity = trunk_capacity if trunk_capacity > 0 else 10

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, fuel_consumption):
        if isinstance(fuel_consumption, (int, float)) and fuel_consumption > 0:
            self.__fuel_consumption = fuel_consumption

    @property
    def trunk_capacity(self):
        return self.__trunk_capacity

    @trunk_capacity.setter
    def trunk_capacity(self, trunk_capacity):
        if isinstance(trunk_capacity, int) and trunk_capacity > 10:
            self.__trunk_capacity = trunk_capacity

    def __str__(self):
        return (super().__str__()
                + f" (Fuel consumption = {self.fuel_consumption} l, "
                  f"trunk capacity = {self.__trunk_capacity} l)")
