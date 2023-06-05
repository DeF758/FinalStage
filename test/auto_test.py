import unittest
from entity.auto import Auto


class SportCarTest(unittest.TestCase):
    def test_auto_default_constructor(self):
        auto = Auto()
        expected_brand = 'no brand'
        expected_model = 'no model'
        expected_price = 0

        self.assertEqual(expected_brand, auto.brand)
        self.assertEqual(expected_model, auto.model)
        self.assertEqual(expected_price, auto.price)

    def test_auto_constructor_with_args(self):
        expected_brand = "Opel"
        expected_model = "Asta"
        expected_price = 8000

        auto = Auto(expected_brand, expected_model, expected_price)

        self.assertEqual(expected_brand, auto.brand)
        self.assertEqual(expected_model, auto.model)
        self.assertEqual(expected_price, auto.price)

    def test_negative_auto_brand(self):
        brand = 555
        expected = "no brand"

        auto = Auto(brand=brand)

        self.assertEqual(expected, auto.brand)

    def test_negative_auto_model(self):
        model = 555
        expected = "no model"

        auto = Auto(model=model)

        self.assertEqual(expected, auto.model)

    def test_negative_auto_price(self):
        price = -555
        expected = 0

        auto = Auto(model=price)

        self.assertEqual(expected, auto.price)

    def test_zero_auto_brand(self):
        brand = ""
        expected = "no brand"

        auto = Auto(brand=brand)

        self.assertEqual(expected, auto.brand)

    def test_zero_auto_model(self):
        model = ""
        expected = "no model"

        auto = Auto(model=model)

        self.assertEqual(expected, auto.model)

    def test_zero_auto_price(self):
        price = 0
        expected = 0

        auto = Auto(price=price)

        self.assertEqual(expected, auto.price)

    def test_brand_property_negative(self):
        auto = Auto()
        expected = auto.brand
        auto.brand = -200

        self.assertEqual(expected, auto.brand)

    def test_brand_property_positive(self):
        auto = Auto()
        auto.brand = "BMW"

        expected = "BMW"

        self.assertEqual(expected, auto.brand)

    def test_brand_property_with_zero(self):
        auto = Auto()
        expected = auto.brand
        auto.brand = "no brand"

        self.assertEqual(expected, auto.brand)

    def test_model_property_negative(self):
        auto = Auto()
        expected = auto.model
        auto.model = -200

        self.assertEqual(expected, auto.model)

    def test_model_property_positive(self):
        auto = Auto()
        auto.model = "M5"

        expected = "M5"

        self.assertEqual(expected, auto.model)

    def test_model_property_with_zero(self):
        auto = Auto()
        expected = auto.model
        auto.model = "no model"

        self.assertEqual(expected, auto.model)

    def test_price_property_negative(self):
        auto = Auto()
        expected = auto.price
        auto.price = -200

        self.assertEqual(expected, auto.price)

    def test_price_property_positive(self):
        auto = Auto()
        auto.price = 450

        expected = 450

        self.assertEqual(expected, auto.price)

    def test_price_property_with_zero(self):
        auto = Auto()
        expected = auto.price
        auto.price = 0

        self.assertEqual(expected, auto.price)


if __name__ == '__main__':
    unittest.main()
