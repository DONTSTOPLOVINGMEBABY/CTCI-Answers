
'''

Write a method to replace all spaces in a string with %20. You may assume 
that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place

'''

'''
This solution is O(n) with space complexity of O(n)
'''


def urlify(string):

    ctr = 0 
    new_string = "" 
    
    print("Prior: ", string)  

    string = string.strip()
    length = len(string)
    while (ctr != length) :    
        if (string[ctr] != ' '):
            new_string += string[ctr] 
            if (ctr + 1 != length and string[ctr + 1] == ' '):
                new_string += '%20'
     
        ctr += 1 

    return new_string

print(urlify("    HI there     ss"))
print(urlify("Mr John Smith    "))
