
import unittest

from week0demand import calculate_daily_kwh


class TestDemandCalculation(unittest.TestCase):

    def test_demo_household(self):
        appliances = [
            {"name": "LED lamp", "power_w": 10, "hours_per_day": 5},
            {"name": "TV", "power_w": 60, "hours_per_day": 4},
        ]

        result = calculate_daily_kwh(appliances)

        self.assertAlmostEqual(result, 0.29)

    def test_negative_hours(self):
        appliances = [
            {"name": "TV", "power_w": 60, "hours_per_day": -4}
        ]

        with self.assertRaises(ValueError):
            calculate_daily_kwh(appliances)

    def test_empty_household(self):
        result = calculate_daily_kwh([])

        self.assertEqual(result, 0)
