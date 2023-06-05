from container.car_showroom import CarShowroom
from entity.auto import Auto


class SalesManager:
    @staticmethod
    def max_price(cars):
        if isinstance(cars, CarShowroom) and cars.size != 0:
            max_price = cars.get_cars(0).price
            for i in range(cars.size):
                car = cars.get_cars(i)

                if isinstance(car, Auto) and max_price < car.price:
                    max_price = car.price

            return max_price
        else:
            return 0

    @staticmethod
    def min_price(cars):
        if isinstance(cars, CarShowroom) and cars.size != 0:
            min_price = SalesManager.max_price(cars)
            for i in range(cars.size):
                car = cars.get_cars(i)

                if isinstance(car, Auto) and min_price > car.price:
                    min_price = car.price

            return min_price
        else:
            return 0

    @staticmethod
    def car_max_price(cars):
        if isinstance(cars, CarShowroom) and cars.size != 0:
            max_price = SalesManager.max_price(cars)
            car_max = cars.get_cars(0)
            for i in range(cars.size):
                car = cars.get_cars(i)

                if isinstance(car, Auto) and max_price == car.price:
                    car_max = cars.get_cars(i)

            return car_max
        else:
            return 0

    @staticmethod
    def car_min_price(cars):
        if isinstance(cars, CarShowroom) and cars.size != 0:
            min_price = SalesManager.min_price(cars)
            car_min = cars.get_cars(0)
            for i in range(cars.size):
                car = cars.get_cars(i)

                if isinstance(car, Auto) and min_price == car.price:
                    car_min = cars.get_cars(i)

            return car_min
        else:
            return 0
