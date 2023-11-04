'''
https://www.codewars.com/kata/523f5d21c841566fde000009/python

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''

test_array1 = [1,2]
test_array2 = [1,2,2]
test_array3 = [1,2,2,2,3]
test_array4 = [1,2,3]

pop1 = [1]
pop2 = [2]
pop_array = [1, 2]

def array_diff(original_array,query_array):
    #initiate an empty array
    new_array = []
    i = 0
    if query_array == [] or original_array == []:
        return original_array
    else:
        for y in query_array:
             #check to see if is in list 2 by iterating through list 2 with equality          
            for x in original_array:
                #if it is in there, pop it
                # cant use if x != y because you'll 
                if x not in query_array and y not in new_array:
                    new_array.append(x)

    return new_array 
    

print(array_diff(test_array1,pop1), ' should be [2]')
print(array_diff(test_array2,pop1), " expected [2,2]")
print(array_diff(test_array2,pop2), " expected [1]")
print(array_diff(test_array2,[]), " expected [1,2,2]")
print(array_diff([],test_array1), " expected []")
print(array_diff(test_array4,pop_array), " expected [3]")

