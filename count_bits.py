'''
https://www.codewars.com/kata/526571aae218b8ee490006f4/python


Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

'''

def count_bits(mynum):
    mynum_bin = (bin(mynum))
    newnum = 0
    
    for bit in mynum_bin[2:]:
        newnum = newnum + int(bit)

    return newnum 



