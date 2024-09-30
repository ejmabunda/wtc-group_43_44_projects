"""Test class
"""
import unittest
from functions.tdd import \
    sum_of_even,\
    calculate_median,\
    find_missing_number,\
    remove_duplicates,\
    first_non_repeating_char


class TestFunctions(unittest.TestCase):
    """Test cases
    """
    def test_sum_of_evens(self):
        """Test cases for the sum_of_evens_function
        """
        list1 = []
        self.assertEqual(sum_of_even(list1), 0)

        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sum_of_even(list2), 30)

        list3 = [1]
        self.assertEqual(sum_of_even(list3), 0)
        
        list4 = [2]
        self.assertEqual(sum_of_even(list4), 2)
        
        list5 = [-1, -2, -3, -4, -5]
        self.assertEqual(sum_of_even(list5), -6)

        list6 = [2, 4, 6, 8, 10]
        self.assertEqual(sum_of_even(list6), 30)

    def test_calculate_median(self):
        """Test cases for the calculate_median function
        """
        # Empty list returns -1
        list1 = []
        self.assertEqual(calculate_median(list1), -1)
        
        # List with a single number returns that number
        list1 = [4]
        self.assertEqual(calculate_median(list1), 4)
        
        # List with a all identical numbers returns that number
        list1 = [4, 4, 4, 4, 4]
        self.assertEqual(calculate_median(list1), 4)
        
        # List with all identical numbers returns that number
        list1 = [-4, -44, -14, -1, 0]
        self.assertEqual(calculate_median(list1), -4)

        list1 = [-4, -44, -14, -1, 0, 7]
        self.assertEqual(calculate_median(list1), -2.5)

    def test_find_missing_number(self):
        """Test cases for the find_missing_number function
        """
        list1 = [1, 2, 3, 4, 6]
        self.assertEqual(find_missing_number(list1), 5)
        
        list1 = [2, 3, 4, 6]
        self.assertEqual(find_missing_number(list1), 1)
        
        # list1 = [1]
        # self.assertEqual(find_missing_number(list1), 1)
        
        list1 = [2]
        self.assertEqual(find_missing_number(list1), 1)

    def test_remove_duplicates(self):
        """Test cases for the remove_duplicates function
        """
        string = 'Hello, world!'
        self.assertEqual(remove_duplicates(string), 'Helo, wrd!')
        
        string = ''
        self.assertEqual(remove_duplicates(string), '')
        
        string = 'lower LOWER'
        self.assertEqual(remove_duplicates(string), 'lower LOWER')
        
        string = 'lower'
        self.assertEqual(remove_duplicates(string), 'lower')

    def test_first_non_repeating_char(self):
        """Test cases for the first_non_repeating_char function
        """
        string = 'Hello, world!'
        self.assertEqual(first_non_repeating_char(string), 'H')
        
        string = 'ello, world!'
        self.assertEqual(first_non_repeating_char(string), 'e')
        
        string = 'levelar'
        self.assertEqual(first_non_repeating_char(string), 'v')
        
        string = 'lleevvewwllaarr'
        self.assertEqual(first_non_repeating_char(string), None)

if __name__ == '__main__':
    unittest.main()

