import unittest

from utils import Time

class TestTime(unittest.TestCase):
    def test_correct_value(self):
        value = "12:34:56"

        t = Time(value)

        self.assertEqual(t.hours, 12)
        self.assertEqual(t.minutes, 34)
        self.assertEqual(t.seconds, 56)

    def test_correct_value_with_leading_zero(self):
        value = "01:02:03"

        t = Time(value)

        self.assertEqual(t.hours, 1)
        self.assertEqual(t.minutes, 2)
        self.assertEqual(t.seconds, 3)

    def test_incorrect_value_without_seconds(self):
        value = "01:02:"

        with self.assertRaises(ValueError):
            t = Time(value)

    def test_incorrect_value_without_seconds_and_colon(self):
        value = "01:02"

        with self.assertRaises(ValueError):
            t = Time(value)

    def test_incorrect_value_without_minutes(self):
        value = "01:"

        with self.assertRaises(ValueError):
            t = Time(value)

    def test_incorrect_value_without_minutes_and_colon(self):
        value = "01"

        with self.assertRaises(ValueError):
            t = Time(value)

    def test_incorrect_value_empty(self):
        value = ""

        with self.assertRaises(ValueError):
            t = Time(value)

    def test_to_seconds(self):
        value = "01:02:03"

        t = Time(value)

        self.assertEqual(t.to_seconds(), 3723)

    def test_from_seconds(self):
        value = 3723

        t = Time.from_seconds(value)

        self.assertEqual(t.hours, 1)
        self.assertEqual(t.minutes, 2)
        self.assertEqual(t.seconds, 3)
