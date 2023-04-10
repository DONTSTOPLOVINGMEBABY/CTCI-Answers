'''
Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only call to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat")

"waterbottle" = "erbottlewat"

waterbottle
erbottlewat

x = wat
y = erbottle

waterbottle = x * y 

erbottlewat = y * x 

we need to find x and y

reverse_waterbottle = elttobretaw

reverse_erbottlewat = tawelttobre


go through the entire string until you find a character that matches the end character of substring

if [0:index of found character] == [len(substring) - index_of_character: len(substring)] 

then we have a match

'''

def first_attempt(string, substring):
    
    if (len(string) != len(substring)) : return False 

    split_index = 0
    first_character = substring[len(substring) - 1]
    
    while split_index < len(string):
        if (string[split_index] == first_character):
            first = string[0:split_index + 1]
            second = substring[len(substring) - split_index - 1  : len(substring)]
            if (first == second): 
                break
        split_index += 1

    if (substring[len(substring) - split_index - 1 : len(substring)] + substring[0:len(substring) - split_index - 1]) == string:
        return True
    else :
        return False 



print(first_attempt("waterbottle", "erbottlewat"))
print(first_attempt("thisthing", "isthingth")) 
print(first_attempt("thisthing", "histhingth"))
