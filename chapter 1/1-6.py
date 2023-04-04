'''
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters. 
'''


'''

# compressed = [ {a : ["a, a, a"]}, {b : ["b", "b"]}, ... ]

# compressed = [ ["a", "a", "a"], ["b", "b", "b"], ... ]

Need to keep track of where I am in the array, and what current letter is at that location. 

'''

def string_compression(string) : 
    
    compressed_characters = [ [] ]
    current_character = string[0]
    compressed_ctr = 0 
    ctr = 0
    
    while (ctr < len(string)) :
        if (string[ctr] == current_character):
            compressed_characters[compressed_ctr].append(string[ctr])
        else :
            compressed_ctr += 1 
            compressed_characters.append([])
            compressed_characters[compressed_ctr].append(string[ctr])
            current_character = string[ctr]
        
        ctr += 1 


    new_string = "" 
    for i in compressed_characters:
        new_string += f'{i[0]}{len(i)}'
    
    return new_string if len(new_string) < len(string) else string



print(string_compression("aabcccccaaa"))
print(string_compression("Henry"))
print(string_compression("Heeeeeeeello"))
