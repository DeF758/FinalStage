import unittest
from entity.sport_car import SportCar


class SportCarTest(unittest.TestCase):
    def test_sport_car_default_constructor(self):
        sport_car = SportCar()
        expected_brand = 'no brand'
        expected_model = 'no model'
        expected_price = 0
        expected_horsepower = 10
        expected_torque = 150

        self.assertEqual(expected_brand, sport_car.brand)
        self.assertEqual(expected_model, sport_car.model)
        self.assertEqual(expected_price, sport_car.price)
        self.assertEqual(expected_horsepower, sport_car.horsepower)
        self.assertEqual(expected_torque, sport_car.torque)

    def test_sport_car_constructor_with_args(self):
        expected_brand = "Opel"
        expected_model = "Asta"
        expected_price = 8000
        expected_horsepower = 180
        expected_torque = 450

        sport_car = SportCar(expected_brand, expected_model, expected_price,
                             expected_horsepower, expected_torque)

        self.assertEqual(expected_brand, sport_car.brand)
        self.assertEqual(expected_model, sport_car.model)
        self.assertEqual(expected_price, sport_car.price)
        self.assertEqual(expected_horsepower, sport_car.horsepower)
        self.assertEqual(expected_torque, sport_car.torque)

    def test_negative_sport_car_horsepower(self):
        horsepower = -180
        expected = 10

        sport_car = SportCar(horsepower=horsepower)

        self.assertEqual(expected, sport_car.horsepower)

    def test_negative_sport_car_torque(self):
        torque = -180
        expected = 150

        sport_car = SportCar(torque=torque)

        self.assertEqual(expected, sport_car.torque)

    def test_zero_sport_car_horsepower(self):
        horsepower = 0
        expected = 10

        sport_car = SportCar(horsepower=horsepower)

        self.assertEqual(expected, sport_car.horsepower)

    def test_zero_sport_car_torque(self):
        torque = 0
        expected = 150

        sport_car = SportCar(torque=torque)

        self.assertEqual(expected, sport_car.torque)

    def test_horsepower_property_negative(self):
        sport_car = SportCar()
        expected = sport_car.horsepower
        sport_car.horsepower = -200

        self.assertEqual(expected, sport_car.horsepower)

    def test_horsepower_property_positive(self):
        sport_car = SportCar()
        sport_car.horsepower = 200

        expected = 200

        self.assertEqual(expected, sport_car.horsepower)

    def test_horsepower_property_with_zero(self):
        sport_car = SportCar()
        expected = sport_car.horsepower
        sport_car.horsepower = 0

        self.assertEqual(expected, sport_car.horsepower)

    def test_torque_property_negative(self):
        sport_car = SportCar()
        expected = sport_car.torque
        sport_car.torque = -200

        self.assertEqual(expected, sport_car.torque)

    def test_torque_property_positive(self):
        sport_car = SportCar()
        sport_car.torque = 450

        expected = 450

        self.assertEqual(expected, sport_car.torque)

    def test_torque_property_with_zero(self):
        sport_car = SportCar()
        expected = sport_car.torque
        sport_car.torque = 0

        self.assertEqual(expected, sport_car.torque)


if __name__ == '__main__':
    unittest.main()
