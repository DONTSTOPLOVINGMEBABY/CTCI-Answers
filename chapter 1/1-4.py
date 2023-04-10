'''
Palindrome Permutation -- Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. You can ignore casing and non-letter characters. 

Input : "Tact Coa"
Output : True (permutations: "taco cat", "atco cta", etc.)
 

'''

string1 = "DAD"     # PALINDROME
string2 = "MOM"     # PALINDROME
string3 = "RACECAR" # PALINDROME 
string4 = "HENRY"   # NOT PALINDROME
string5 = "S"       # PALINDROME 
string6 = ""        # PALINDROME 

def palindrome(string):
    if len(string) <= 1:
        return True
    elif (string[0:1] != string[len(string) - 1 : len(string)]):
        return False 
    else : 
        return palindrome(string[1:len(string) - 1])


def palindrome_permutation(string):
    
    if (len(string) <= 1) : return True 

    string = string.lower().replace(" ", "")
    even_string = len(string) % 2 == 0
    single_found = False 

    hash_map = {}

        
    for i in string:
        if i in hash_map:
            hash_map[i] = (hash_map[i] + 1) % 2  
        else : 
            hash_map[i] = 1  
    
    for i in hash_map:
        if (hash_map[i] == 1 and not even_string and not single_found):
            single_found = True
        elif (hash_map[i] == 1 and even_string):
            return False
        elif (hash_map[i] == 1 and not even_string and single_found):
            return False

    return True
   
def almost_optimal_permutation(string):
    
    if (len(string) <= 1) : return True 

    string = string.lower().replace(" ", "")
    oddctr = 0 
    hash_map = {}

        
    for i in string:
        if i in hash_map:
            hash_map[i] = (hash_map[i] + 1) % 2  
            oddctr -= 1 
        else : 
            hash_map[i] = 1  
            oddctr += 1 

    return oddctr <= 1 





#print(palindrome(string1))
#print(palindrome(string3))
#print(palindrome(string4))
#print(palindrome("y"))
print(palindrome_permutation("tact coa"))
print(palindrome_permutation("DAD"))
print(palindrome_permutation("atco cta"))
print(palindrome_permutation("Boss"))
print(almost_optimal_permutation("tact coa"))
print(almost_optimal_permutation("DAD"))
print(almost_optimal_permutation("atco cta"))
print(almost_optimal_permutation("Boss"))
