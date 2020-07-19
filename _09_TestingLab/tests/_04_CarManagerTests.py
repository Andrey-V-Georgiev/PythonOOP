import unittest
from unittest.mock import Mock

from Car import Car


class CarManagerTests(unittest.TestCase):

    def test_car_constructor(self):
        self.car = Car('BMW', '330ci', 18, 90)
        self.assertEqual(self.car.make, 'BMW')
        self.assertEqual(self.car.model, '330ci')
        self.assertEqual(self.car.fuel_consumption, 18)
        self.assertEqual(self.car.fuel_capacity, 90)
        self.assertEqual(self.car.fuel_amount, 0)

    """
    @make.setter
    """

    def test_car_make_setter_without_arg_raise_exception(self):
        with self.assertRaises(Exception):
            self.car = Car(None, '330ci', 18, 90)

    def test_car_make_setter_works_correctly(self):
        self.car = Car('BMW', '330ci', 18, 90)
        self.assertEqual(self.car.make, 'BMW')

    """
    @model.setter
    """

    def test_car_model_setter_without_arg_raise_exception(self):
        with self.assertRaises(Exception):
            self.car = Car('BMW', None, 18, 90)

    def test_car_model_setter_works_correctly(self):
        self.car = Car('BMW', '330ci', 18, 90)
        self.assertEqual(self.car.model, '330ci')

    """
    @fuel_consumption.setter
    """

    def test_car_fuel_consumption_setter_without_arg_raise_exception(self):
        with self.assertRaises(Exception):
            self.car = Car('BMW', '330ci', 0, 90)

    def test_car_fuel_consumption_setter_works_correctly(self):
        self.car = Car('BMW', '330ci', 18, 90)
        self.assertEqual(self.car.fuel_consumption, 18)

    """
    @fuel_capacity.setter
    """

    def test_car_fuel_capacity_setter_without_arg_raise_exception(self):
        with self.assertRaises(Exception):
            self.car = Car('BMW', '330ci', 18, None)

    def test_car_fuel_capacity_setter_works_correctly(self):
        self.car = Car('BMW', '330ci', 18, 90)
        self.assertEqual(self.car.fuel_capacity, 90)

    """
    @fuel_amount.setter
    """

    def test_car_fuel_amount_raise_exception_if_passed_full_value_is_equal_or_under_zero(self):
        self.car = Car('BMW', '330ci', 18, 90)
        with self.assertRaises(Exception):
            self.car.fuel_amount(-1)

    """
    def refuel(self, fuel)
    """

    def test_car_refuel_raise_exception_if_passed_full_value_is_zero(self):
        self.car = Car('BMW', '330ci', 18, 90)
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_car_refuel_raise_exception_if_passed_full_value_is_under_zero(self):
        self.car = Car('BMW', '330ci', 18, 90)
        with self.assertRaises(Exception):
            self.car.refuel(-1)

    def test_car_refuel_with_more_than_fuel_capacity_refuel_up_to_capacity(self):
        self.car = Car('BMW', '330ci', 18, 90)
        self.car.refuel(120)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_car_refuel_with_less_than_capacity_refuel_correctly(self):
        self.car = Car('BMW', '330ci', 18, 90)
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_car_refuel_with_less_than_capacity_refuel_correctly2(self):
        self.car = Car('BMW', '330ci', 18, 90)
        old_fuel_amount = self.car.fuel_amount
        self.car.refuel(50)
        new_fuel_amount = self.car.fuel_amount
        self.assertNotEqual(old_fuel_amount, new_fuel_amount)

    """
    def drive(self, distance)
    """

    def test_car_drive_more_than_fuel_amount_raise_exception(self):
        self.car = Car('BMW', '330ci', 18, 90)
        self.car.refuel(50)
        with self.assertRaises(Exception):
            self.car.drive(1000)

    def test_car_drive_distance_in_fuel_amount_range__fuel_amount_decrease_correctly(self):
        self.car = Car('BMW', '330ci', 20, 100)
        self.car.refuel(100)
        self.car.drive(20)  # - 4
        self.assertEqual(self.car.fuel_amount, 100 - 4)


if __name__ == '__main__':
    unittest.main()
