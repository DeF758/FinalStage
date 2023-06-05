import unittest

from container.car_showroom import CarShowroom
from entity.auto import Auto
from logic.sales_manager import SalesManager


class SalesManagerTest(unittest.TestCase):
    def test_different_type_max(self):
        car_showroom = "car_showroom"
        expected = 0

        actual = SalesManager.max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_different_type_min(self):
        car_showroom = "car_showroom"
        expected = 0

        actual = SalesManager.min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_different_type_car_max_price(self):
        car_showroom = "car_showroom"
        expected = 0

        actual = SalesManager.car_max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_different_type_car_min_price(self):
        car_showroom = "car_showroom"
        expected = 0

        actual = SalesManager.car_min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_empty_showroom_max(self):
        car_showroom = CarShowroom()
        expected = 0

        actual = SalesManager.max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_empty_showroom_min(self):
        car_showroom = CarShowroom()
        expected = 0

        actual = SalesManager.min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_empty_showroom_car_max_price(self):
        car_showroom = CarShowroom()
        expected = 0

        actual = SalesManager.car_max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_empty_showroom_car_min_price(self):
        car_showroom = CarShowroom()
        expected = 0

        actual = SalesManager.car_min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_None_max(self):
        car_showroom = None
        expected = 0

        actual = SalesManager.max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_None_min(self):
        car_showroom = None
        expected = 0

        actual = SalesManager.min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_None_car_max_price(self):
        car_showroom = None
        expected = 0

        actual = SalesManager.car_max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_None_car_min_price(self):
        car_showroom = None
        expected = 0

        actual = SalesManager.car_min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_cars_max_positive(self):
        auto1 = Auto("", "", 550)
        auto2 = Auto("", "", 800)
        auto3 = Auto("", "", 750)

        car_showroom = CarShowroom()
        car_showroom.add(auto1)
        car_showroom.add(auto2)
        car_showroom.add(auto3)

        expected = 800

        actual = SalesManager.max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_cars_min_positive(self):
        auto1 = Auto("", "", 550)
        auto2 = Auto("", "", 800)
        auto3 = Auto("", "", 750)

        car_showroom = CarShowroom()
        car_showroom.add(auto1)
        car_showroom.add(auto2)
        car_showroom.add(auto3)

        expected = 550

        actual = SalesManager.min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_cars_car_max_price_positive(self):
        auto1 = Auto("AA", "aa", 550)
        auto2 = Auto("BB", "bb", 800)
        auto3 = Auto("CC", "cc", 750)

        car_showroom = CarShowroom()
        car_showroom.add(auto1)
        car_showroom.add(auto2)
        car_showroom.add(auto3)

        expected = auto2

        actual = SalesManager.car_max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_cars_car_min_price_positive(self):
        auto1 = Auto("AA", "aa", 550)
        auto2 = Auto("BB", "bb", 800)
        auto3 = Auto("CC", "cc", 750)

        car_showroom = CarShowroom()
        car_showroom.add(auto1)
        car_showroom.add(auto2)
        car_showroom.add(auto3)

        expected = auto1

        actual = SalesManager.car_min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_one_car_max_positive(self):
        auto = Auto("", "", 550)

        car_showroom = CarShowroom()
        car_showroom.add(auto)

        expected = 550

        actual = SalesManager.max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_one_car_min_positive(self):
        auto = Auto("", "", 550)

        car_showroom = CarShowroom()
        car_showroom.add(auto)

        expected = 550

        actual = SalesManager.min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_one_car_car_max_price_positive(self):
        auto = Auto("AA", "aa", 550)

        car_showroom = CarShowroom()
        car_showroom.add(auto)

        expected = auto

        actual = SalesManager.car_max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_one_car_car_min_price_positive(self):
        auto = Auto("AA", "aa", 550)

        car_showroom = CarShowroom()
        car_showroom.add(auto)

        expected = auto

        actual = SalesManager.car_min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_invalid_dt_max(self):
        auto1 = Auto("", "", 550)
        auto2 = Auto("", "", 800)
        auto3 = Auto("", "", 750)

        car_showroom = CarShowroom()
        car_showroom.add(auto1)
        car_showroom.add("string")
        car_showroom.add(auto2)
        car_showroom.add(auto3)
        car_showroom.add(8)

        expected = 800

        actual = SalesManager.max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_invalid_dt_min(self):
        auto1 = Auto("", "", 550)
        auto2 = Auto("", "", 800)
        auto3 = Auto("", "", 750)

        car_showroom = CarShowroom()
        car_showroom.add(auto1)
        car_showroom.add("string")
        car_showroom.add(auto2)
        car_showroom.add(auto3)
        car_showroom.add(8)

        expected = 550

        actual = SalesManager.min_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_invalid_dt_car_max_price(self):
        auto1 = Auto("AA", "aa", 550)
        auto2 = Auto("BB", "bb", 800)
        auto3 = Auto("CC", "cc", 750)

        car_showroom = CarShowroom()
        car_showroom.add(auto1)
        car_showroom.add("string")
        car_showroom.add(auto2)
        car_showroom.add(auto3)
        car_showroom.add(8)

        expected = auto2

        actual = SalesManager.car_max_price(car_showroom)

        self.assertEqual(expected, actual)

    def test_showroom_with_invalid_dt_car_min_price(self):
        auto1 = Auto("AA", "aa", 550)
        auto2 = Auto("BB", "bb", 800)
        auto3 = Auto("CC", "cc", 750)

        car_showroom = CarShowroom()
        car_showroom.add(auto1)
        car_showroom.add("string")
        car_showroom.add(auto2)
        car_showroom.add(auto3)
        car_showroom.add(8)

        expected = auto1

        actual = SalesManager.car_min_price(car_showroom)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
