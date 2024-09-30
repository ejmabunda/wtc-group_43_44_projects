# Implementing Test Driven Development

**NB:**  For easy readability, read this filises.
- Lastly, no shortcuts (Our boye in preview mode by pressing Ctrl + Shift + V for Windows/Linux and Cmd + Shift + V for Mac.

## Requirements:
- Create a directory called `functions`, which will contain the file with the functions.
- Create a directory called `test`, which will contain the test file with unittests for the functions in the `functions` directory.
- No modules should be imported in the `tdd.py` file located in the `functions` directory.
- Please remember to implement what we discussed during the first two exerc ChatGPT 😊).

## Instructions

Create a Python file called `tdd.py` in the `functions` directory, that will contain the following functions:

## 1.  

Write a function `sum_of_even(nums)` that returns the sum of all even numbers in a list.

**Examples:**
```
sum_of_even([1, 2, 3, 4, 5])  # returns 6 (2 + 4)
sum_of_even([7, 9, 13])       # returns 0 (no even numbers)
``` 

### Edge Cases:

- Empty list should return 0.
- List with no even numbers should return 0.
- List where all numbers are even should return their sum.
- List with negative even numbers should return the correct negative sum.

## 2. 

Write a function `calculate_mediam(nums)` that returns the median value of a list of numbers.

**Remember: For an odd-length list, the median is the middle value.
For an even-length list, the median is the average of the two middle values.**

**Examples:**
```
calculate_median([1, 3, 5])     # returns 3
calculate_median([1, 3, 5, 7])  # returns 4 (average of 3 and 5)
```


### Edge Cases:

- An empty list should raise an error or return a special value.
- A list with a single number should return that number.
- A list with all identical numbers should return that number.
- A list with negative numbers should return the correct median.



## 3. 

Write a function `find_missing_number(nums)` that finds the missing number in a sequence from 1 to n+1

**Examples:**
```
find_missing_number([2, 3, 4, 5, 6, 7, 8, 9])  # returns 1
find_missing_number([1, 2, 4, 5])  # returns 3
```
### Edge Cases:


- A list with no missing number should return None.
- A list with only one number should return the previous number in - the sequence.
- A list where all numbers are present except the first should return 1.
- An unordered list should still return the correct missing number.



## 4. 

Write a function `remove_duplicates(str)` that removes all duplicate characters from a string, maintaining the order of characters.

**Examples:**
```
remove_duplicates("programming")  # returns "progamin"
remove_duplicates("development")  # returns "devlopmnt"
```

### Edge Cases:

- An empty string should return an empty string.
- A string with all unique characters should return the same string.
- A string with all characters duplicated should return just the single character.
- A string with mixed cases should return the correct result, preserving the case sensitivity.

## 5. 

Write a function `first_non_repeating_char(str)` that finds the charcter in a string that does not repeat.

**Examples:**
```
first_non_repeating_char("pineapple")  # returns "i"
first_non_repeating_char("levelar")  # returns "v"
```

### Edge Cases:

- Empty string should return None.
- String with all characters repeating should return None.
- Function should return the first non-repeating character if present.
- String with only one non-repeating character should return that character.  

