'''
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. 
'''

def one_away(string1, string2):

    if (abs(len(string1) - len(string2)) > 1) : return False 
 
    xAway = 0
    ctr1 = 0
    ctr2 = 0 

    while (ctr1 != len(string1) and ctr2 != len(string2)) : 
        if (string1[ctr1] != string2[ctr2] and len(string1) < len(string2)):
            ctr2 += 1
            xAway += 1 
        elif (string1[ctr1] != string2[ctr2] and len(string1) > len(string2)):
            ctr1 += 1 
            xAway += 1
        elif (string1[ctr1] != string2[ctr2] and len(string1) == len(string2)):
            ctr1 += 1 
            ctr2 += 1
            xAway += 1
        else : 
            ctr1 += 1 
            ctr2 += 1 

    return True if xAway <= 1 else False 



print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
print(one_away("Henry", "Haasdkljf"))
