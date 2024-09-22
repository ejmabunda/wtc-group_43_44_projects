# group_tests.py
# Testing the Petrol Station App

import unittest
from group_exercise import user_authentication, menu, calculate_petrol, main

class TestPetrolStationApp(unittest.TestCase):

    # Test user authentication with valid inputs
    def test_user_authentication_valid(self):
        self.assertTrue(user_authentication("John Doe", "1234567890"))

    # Test user authentication with an invalid phone number
    def test_user_authentication_invalid_number(self):
        self.assertFalse(user_authentication("Alice", "1234"))

    # Test user authentication with an invalid name
    def test_user_authentication_invalid_name(self):
        self.assertFalse(user_authentication("", "1234567890"))

    # Test menu function
    def test_menu(self):
        self.assertEqual(menu(), "Menu:\n1. Snacks\n2. Perishables\n3. Diesel Price\n4. Unleaded Price\n5. Calculate Petrol\n6. Exit")

    # Test petrol calculation with valid input
    def test_calculate_petrol_valid(self):
        self.assertEqual(calculate_petrol(50, "unleaded", 1.2), "You can get 41.67 liters of unleaded petrol.")

    # Test petrol calculation with an invalid petrol type
    def test_calculate_petrol_invalid_type(self):
        self.assertEqual(calculate_petrol(50, "propane", 1.2), "Invalid petrol type.")

    # Test petrol calculation with an invalid price
    def test_calculate_petrol_invalid_price(self):
        self.assertEqual(calculate_petrol(0, "diesel", 1.2), "Invalid price. Please enter a valid amount.")

    # Test main function with valid input
    def test_main_valid(self):
        self.assertEqual(main("John Doe", "1234567890", "4"), "Goodbye, John Doe!")

    # Test main function with an invalid menu choice
    def test_main_invalid_choice(self):
        self.assertEqual(main("Alice", "9876543210", "7"), "Invalid choice. Please select a valid option.")

    # Test main function with an invalid phone number
    def test_main_invalid_number(self):
        self.assertEqual(main("Bob", "123", "2"), "Invalid phone number. Please enter a 10-digit number.")

    # Test main function with an invalid name
    def test_main_invalid_name(self):
        self.assertEqual(main("", "9876543210", "3"), "Invalid name. Please enter a valid name.")

    # Test main function with calculating petrol
    def test_main_calculate_petrol(self):
        self.assertEqual(main("Carol", "5555555555", "5\nunleaded\n50"), "You can get 41.67 liters of unleaded petrol.")

    # Test main function with quitting the app
    def test_main_quit(self):
        self.assertEqual(main("David", "9999999999", "6"), "Goodbye, David!")

if __name__ == "__main__":
    unittest.main()
