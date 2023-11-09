'''
https://www.codewars.com/kata/523f5d21c841566fde000009/python

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''

def array_diff(original_array, query_array):
    '''Remove all values from original_arry, which are present in query_array, keeping their order'''

    # Exit early if either array is empty
    if not original_array or not query_array:
        return original_array

    # Build a new_array with original_array values not present in query_array
    new_array = []

    for x in original_array:
        if x not in query_array:
            new_array.append(x)

    return new_array 


test_array1 = [1,2]
test_array2 = [1,2,2]
test_array3 = [1,2,2,2,3]
test_array4 = [1,2,3]

pop1 = [1]
pop2 = [2]
pop_array = [1, 2]

assert(array_diff(test_array1, pop1) == [2])
assert(array_diff(test_array2, pop1) == [2,2])
assert(array_diff(test_array2, pop2) == [1])
assert(array_diff(test_array2, []) == [1,2,2])
assert(array_diff([], test_array1) == [])
assert(array_diff(test_array4, pop_array) == [3])
