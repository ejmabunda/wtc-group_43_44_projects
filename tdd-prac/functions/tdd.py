def sum_of_even(nums: list[int]) -> int:
    """Calculates the sum of even numbers
    in a given list
    
    Arguments:
        nums(list): A list of numbers
        
    Returns:
        int: The sum of even numbers
    """
    return sum(filter(lambda x: x % 2 == 0, nums))

def calculate_median(nums: list) -> int:
    """Calculates the median of a list
    
    Arguments:
        nums(list): A list of numbers
        
    Returns:
        int: The median number of a list
    """
    # Sort the list
    nums = sorted(nums)

    # length of list
    nums_len = len(nums)
    if nums_len == 0:
        return -1
    elif nums_len == 1:
        return nums[0]

    if nums_len % 2 == 0: # Even number of items
        return (nums[nums_len//2] + nums[(nums_len//2) - 1]) / 2
    
    return nums[nums_len//2]

def find_missing_number(nums: list) -> int:
    """Finds the missing number in a sequence from
    1 to n+1
    
    Arguments:
        nums(list[int]): A list of integers
        
    Returns:
        int: The missing number
    """
    # Sort the list
    nums = sorted(nums)

    if nums[0] != 1:
        return 1
    if len(nums) == 1:
        return 1 if nums[0] > 1 else nums[0] - 1

    previous = nums[0]
    for ix in range(1, len(nums)):
        # difference between previous and current must be 1
        if nums[ix] == previous + 1:
            previous = nums[ix]
        else:
            return previous + 1
    
    # No missing numbers
    return None

def remove_duplicates(str: str) -> str:
    """Removes all duplicates from a string,
    maintaining the order of characters
    
    Arguments:
        str(str): A string
        
    Returns:
        str: A string with no duplicates
    """
    new_str = ''
    for char in str:
        if char not in new_str:
            new_str += char
    
    return new_str

def first_non_repeating_char(str: str) -> str:
    """Finds the characer in a string that does
    not repeat
    
    Arguments:
        str(str): A string
    
    Returns:
        str: A character that does not repeat
    """
    for char in str:
        if str.count(char) == 1:
            return char
        
    return None
