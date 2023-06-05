from entity.auto import Auto


class CarShowroom:
    def __init__(self, cars=None):
        if not cars:
            self.__cars = []
        else:
            self.__cars = cars

    @property
    def size(self):
        return len(self.__cars)

    def get_cars(self, i):
        if isinstance(i, int) and i >= 0 and i < self.size:
            return self.__cars[i]

    def add(self, car):
        if isinstance(car, Auto):
            self.__cars.append(car)

    def __str__(self):
        msg = "List of cars:"
        for i in range(self.size):
            msg += f"\n{i + 1}) " + str(self.__cars[i])
        return msg
