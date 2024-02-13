# Author: Kristin Towns
# GitHub: kristinlashun
# Date: 2/12/2024
"""
Description: This file contains a recursive function named list_max that takes a list of numbers
and returns the maximum value in the list without using loops, external variables,
mutable default arguments, or the built-in max() function.
"""

def list_max(numbers, current_max=None, index=0):
    # If this is the first call, initialize current_max to the first element
    if current_max is None:
        current_max = numbers[0]
    
    # Base case: if the index is out of bounds, return the current_max
    if index == len(numbers):
        return current_max
    
    # Recursive case: update the current_max if the current number is larger
    if numbers[index] > current_max:
        current_max = numbers[index]
    
    # Move to the next element
    return list_max(numbers, current_max, index + 1)
