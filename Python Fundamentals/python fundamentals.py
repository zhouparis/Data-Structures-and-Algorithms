# Name: Paris Zhou
# Contact Email: zhou.paris00@gmail.com
# Python Fundamentals

import random
from static_array import * 

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
    """
    This function takes a static array and finds the both the minimum and the maximum within the array iteratively.
    """
    minimum = arr.get(0)
    maximum = arr.get(0)

    for index in range(arr.length()):
        if arr.get(index) > maximum:
            maximum = arr.get(index)
        if arr.get(index) < minimum:
            minimum = arr.get(index)

    return (minimum, maximum)

    pass


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    This function takes a static array of integers and creates a modified copy of it based on the divisibility of the items. 
    Items divisible strictly by 3 print "fizz" instead, items divisible strictly by 5 print "buzz" instead, items divisible by both 3 and 5 print
    "fizzbuzz" instead.  
    """

    # Create new array object
    new_arr = StaticArray(arr.length())

    for index in range(arr.length()):

        if arr.get(index) % 3 == 0 and arr.get(index) % 5 == 0:
            new_arr.set(index, "fizzbuzz")

        elif arr.get(index) % 3 == 0:
            new_arr.set(index, "fizz")

        elif arr.get(index) % 5 == 0:
            new_arr.set(index, "buzz")

        else:
            new_arr.set(index, arr.get(index))

    return new_arr

    pass


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    This function reverses the inputted static array.
    """
    tempNum = None
    for index in range(arr.length() // 2):
        tempNum = arr.get(index)
        # Swap the item opposite to the current item, since length is 1-indexed, subtract 1 to convert to 0 indexed
        arr.set(index, arr.get(arr.length() - 1 - index)) 
        arr.set(arr.length() - 1 - index, tempNum)

    pass


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    The rotate function moves all elements in the array however many steps inputted. Negative shifts
    elements left, positive shifts elements right.
    """

    new_arr = StaticArray(arr.length())
    places_moved = steps % new_arr.length()
    tempNum = None

    for index in range(new_arr.length()):
        new_arr.set((index + places_moved) % new_arr.length(), arr.get(index))

    return new_arr

    pass


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    The sa_range function creates a static array filled with numbers between the inputted starting and ending 
    ranges. It can handle ascending and descending ranges. It can also handle negative numbers.
    """
    array = StaticArray(abs(end - start) + 1)

    if end >= start:
        for index in range(abs(end - start) + 1):
            array.set(index, start + index)

    if end < start:
        for index in range(abs(end - start) + 1):
            array.set(index, start - index)

    return array

    pass


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    This functions checks if the static array is sorted in a strictly ascending order or strictly descending order.
    Strictly ascending returns 1, strictly descending returns -1. Unsorted and non-decreasing/non-ascending returns 0.
    """
    if arr.length() == 1:
        return 1
    
    if arr.get(0) < arr.get(1):
        index = 0 
        while index < arr.length()-1:
            if arr.get(index) < arr.get(index+1):
                index += 1
            else:
                return 0
        return 1
    
    if arr.get(0) > arr.get(1):
        index = 0 
        while index < arr.length()-1:
            if arr.get(index) > arr.get(index+1):
                index += 1
            else:
                return 0
        return -1

    pass


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    The find_mode function determines the mode of a set of elements in a "StaticArray" object. It keeps iterates through
    the inputted static array object comparing each element to the next while keeping track of a counter of times it has
    seen the same element. If the element changes, it updates the current counter and the current compared element. If
    the running counter surpasses the maximum counter, it will update the mode and reset the counter. This comparison keeps
    track of only the first most repeated element in the StaticArray object.
    """
    current_counter = 1
    current = None
    max_counter = 1
    mode = None

    for index in range(arr.length()):
        if current == arr.get(index):
            current_counter += 1
        else:
            current = arr.get(index)
            current_counter = 1
        if current_counter > max_counter:
            max_counter = current_counter
            mode = current

    if mode == None:
        return (arr.get(0), 1)

    return (mode, max_counter)

    pass


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    This function determines the required length of the new array by looping through and checking for duplicates and then
    creates a new array based off of the number of unique elements in the inputted StaticArray. The function then rereads
    the inputted StaticArray object and adds unique elements to the new StaticArray object.
    """
    checker = None
    new_arr_length = 0

    for index in range(arr.length()):
        if checker == arr.get(index):
            continue
        else:
            checker = arr.get(index)
            new_arr_length += 1

    new_arr = StaticArray(new_arr_length)

    current = None
    new_arr_index_counter = -1

    for index in range(arr.length()):
        if current == arr.get(index):
            continue
        else:
            current = arr.get(index)
            new_arr_index_counter += 1
            new_arr.set(new_arr_index_counter, current)

    return new_arr

    pass


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    The count_sort function takes an unsorted "StaticArray" Object as an input and outputs a non-ascending sorted
    "StaticArray" object. The function first reads the inputted StaticArray object and finds the maximum
    of elements in the object. The function then traverses the inputted StaticArray object and counts how many times
    each number occurs, storing them as at an index within the constructor array equal to the maximum minus the value
    being assessed. The constructor array is then unpacked by another loop that reads the array from the lowest index to
    the highest index, subtracting the index from the maximum for as many times until the value of the element at that
    index reaches 0.
    """

    maximum = arr.get(0)

    # Find the maximum

    for index in range(arr.length()):
        if arr.get(index) > maximum:
            maximum = arr.get(index)

    # Set up the constructor array based off the input array, with the index of the constructor array representing
    # the value based on the distance from the maximum and the value at that index representing how many times the
    # number appears

    constructor_array = StaticArray(1000)

    for index in range(arr.length()):
        if constructor_array.get(maximum - arr.get(index)) is None:
            constructor_array.set(maximum - arr.get(index), 1)
        else:
            constructor_array.set(maximum - arr.get(index), constructor_array.get(maximum - arr.get(index)) + 1)

    # Create the sorted array, add a counter to keep track of the index as the loop will iterate over the constructor
    # Array which is not guaranteed to have the same indices as the sorted array

    sorted_array = StaticArray(arr.length())
    sorted_array_length = 0

    for index in range(constructor_array.length()):
        if constructor_array.get(index) != 0 and constructor_array.get(index) is not None:
            for times in range(constructor_array.get(index)):
                sorted_array.set(sorted_array_length, maximum - index)
                sorted_array_length += 1
        else:
            continue

    return sorted_array

    pass


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    The program sorts a StaticArray Object's elements squared. It starts by assess for negatives and then squares
    negatives and adds them to its own StaticArray object if they exist. If there are no negative numbers it will
    square the original array and return it in a new array sorted. If there are only negative numbers it will square
    the numbers, reverse the array and then return it.
    """

    new_array = StaticArray(arr.length())
    split_indicator = 0

    # Figure out where the negatives end and the positives begin if there are any
    # If the array is a mix of negative and positive numbers we then separate them into different arrays

    for index in range(arr.length()):
        if arr.get(index) < 0:
            split_indicator += 1

    # If there are only positive numbers

    if split_indicator == 0:
        for index in range(arr.length()):
            new_array.set(index, arr.get(index) ** 2)
        return new_array
    else:
        neg_squares = StaticArray(split_indicator)

    # if there are only negative numbers

    if split_indicator == arr.length():
        for index in range(arr.length()):
            new_array.set(index, arr.get(index) ** 2)
        tempNum = None
        for index in range(new_array.length() // 2):
            tempNum = new_array.get(index)
            new_array.set(index, new_array.get(new_array.length() - 1 - index))
            new_array.set(new_array.length() - 1 - index, tempNum)
        return new_array
    else:
        pos_squares = StaticArray(arr.length() - split_indicator)

    # Square the arrays separately

    for index in range(split_indicator):
        neg_squares.set(index, arr.get(index) ** 2)

    for index in range(arr.length() - split_indicator):
        pos_squares.set(index, arr.get(index + split_indicator) ** 2)

    # Reverse the negative squares list as it should be constructed in a non-ascending order by default, and
    # we need it in a non-descending order.

    tempNum = None
    for index in range(neg_squares.length() // 2):
        tempNum = neg_squares.get(index)
        neg_squares.set(index, neg_squares.get(neg_squares.length() - 1 - index))
        neg_squares.set(neg_squares.length() - 1 - index, tempNum)

    # Use two separate pointers in our arrays to construct the final array to be outputted
    # The two pointers will increment and compare the values in each array to create the final sorted array
    # The first if and elif statements check to make sure neither array has been completely traversed, if they
    # have been completely traversed then we can go and traverse the other list only

    pos_index = 0
    neg_index = 0

    while pos_index + neg_index < new_array.length():
        if neg_index >= neg_squares.length():
            new_array.set(pos_index + neg_index, pos_squares.get(pos_index))
            pos_index += 1
        elif pos_index >= pos_squares.length():
            new_array.set(pos_index + neg_index, neg_squares.get(neg_index))
            neg_index += 1
        elif neg_squares.get(neg_index) < pos_squares.get(pos_index):
            new_array.set(pos_index + neg_index, neg_squares.get(neg_index))
            neg_index += 1
        else:
            new_array.set(pos_index + neg_index, pos_squares.get(pos_index))
            pos_index += 1

    return new_array

    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\ncurrent: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
