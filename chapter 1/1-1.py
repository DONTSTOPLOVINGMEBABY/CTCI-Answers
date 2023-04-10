from bitarray import bitarray 

'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if it cannot use additional data structures?


string1 = "abcdef" 

string2 = "ghijkl"

string3 = "mnopqa" 

unique(string1, string2) returns True 

unique(string1, string3) returns False 

'''

string1 = "Henry" 
string2 = "HenryHenry"

def hash_table(string):
    table = {}
    for i in string:
        if i in table: return False 
        else : table[i] = True 
    return True 


def array_of_booleans(string):
    if len(string) > 128 : return False
    char_set = [False] * 128 

    for i in string: 
        if char_set[ord(i)]:
            return False
        else: char_set[ord(i)] = True 

    return True 


print(hash_table(string1))
print(hash_table(string2))

print(array_of_booleans(string1))
print(array_of_booleans(string2)) 
