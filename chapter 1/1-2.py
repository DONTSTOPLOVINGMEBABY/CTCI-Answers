'''

Given two strings, write a method to decide if one is a permutation of the other

'''


def check_permutation(string1, string2):
        
    if (len(string1) != len(string2)) : return False 
    
    char_map = {}
    
    for i in string1 :
        if (i in char_map): 
            char_map[i] = [*char_map[i], i]
        else:
            char_map[i] = [i] 
    
    ## This is O(n) with constant time lookup in char_map 


    for i in string2:
        if (i in char_map):
            char_map[i].pop()
        if (i in char_map and len(char_map[i]) == 0) : del char_map[i]
    
        
    ## This is O(n) with constant time lookup and deletion in char_map 


    return True if len(char_map) == 0 else False 


    print(len(char_map))
        

print(check_permutation("iiiiii", "iiiiii"))
print(check_permutation("listen", "silent"))
print(check_permutation("triangle", "integral"))
print(check_permutation("debit card", "bad credit"))
print(check_permutation("Henry", "Jacobs"))
print(check_permutation("Lover", "Clove"))

