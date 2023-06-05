from random import choice, randint

from entity.auto import Auto
from container.car_showroom import CarShowroom


class CarCreator:
    @staticmethod
    def create(size=15):
        cars = CarShowroom()
        BRAND = ("BMW", "Porsche", "Kia", "Ford", "Chevrolet")

        MODEL_BMW = ("M5", "X5", "X5M", "i8", "M4")
        MODEL_PORSCHE = ("911", "718", "Taycan", "Panamera", "Macan", "Cayenne")
        MODEL_KIA = ("Sportage", "Ceed", "Sorento", "Soul", "K5", "Carnival")
        MODEL_FORD = ("Shelby", "Explorer", "Fiesta", "GT", "Focus", "Mondeo")
        MODEL_CHEVROLET = ("Camaro", "Aveo", "Captiva",
                           "Cobalt", "Corvette", "Cruze")

        MIN_PRICE = 10000
        MAX_PRICE = 278000

        for _ in range(size):
            car = Auto()
            car.brand = choice(BRAND)

            if car.brand == "BMW":
                car.model = choice(MODEL_BMW)
            elif car.brand == "Porsche":
                car.model = choice(MODEL_PORSCHE)
            elif car.brand == "Kia":
                car.model = choice(MODEL_KIA)
            elif car.brand == "Ford":
                car.model = choice(MODEL_FORD)
            elif car.brand == "Chevrolet":
                car.model = choice(MODEL_CHEVROLET)

            car.price = randint(MIN_PRICE, MAX_PRICE)

            cars.add(car)

        return cars
