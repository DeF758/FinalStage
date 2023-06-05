from entity.auto import Auto


class SportCar(Auto):
    def __init__(self, brand='no brand', model='no model', price=0,
                 horsepower=10, torque=150):
        super().__init__(brand, model, price)
        self.__horsepower = horsepower if horsepower > 0 else 10
        self.__torque = torque if torque > 0 else 150

    @property
    def horsepower(self):
        return self.__horsepower

    @horsepower.setter
    def horsepower(self, horsepower):
        if isinstance(horsepower, int) and horsepower >= 10:
            self.__horsepower = horsepower

    @property
    def torque(self):
        return self.__torque

    @torque.setter
    def torque(self, torque):
        if isinstance(torque, int) and torque >= 150:
            self.__torque = torque

    def __str__(self):
        return (super().__str__()
                + f" ({self.__horsepower} hp, {self.__torque} torque)")
