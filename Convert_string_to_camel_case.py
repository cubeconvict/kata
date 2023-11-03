# Solution to Kata at https://www.codewars.com/kata/517abf86da9663f1d2000003

import re

string1 = "the_stealth_warrior"
string2 = "The-Stealth-Warrior"


def to_camel_case(text):
    mylist = re.split('_|-', text)
    
    length = len(mylist)

    for i in range(1,length):      
        #if the first character is lower
        if re.match(r'^[a-z]', mylist[i]):
            mylist[i] = mylist[i][0].upper()+mylist[i][1:]
        

    final_string = ''.join(mylist)
    return  final_string


'''
Test Block
print(to_camel_case(string1))
print(to_camel_case(string2))
'''
