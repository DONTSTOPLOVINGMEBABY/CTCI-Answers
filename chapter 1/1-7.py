'''
Given an image represented by an N x N matrix, where each pixel is in the image is represented by an integer, write a method to rotate the image by 90 degrees. Can you do this in place?

    1   2   3   4               3   4   11  12

    5   6   7   8   ----->      7   8   15  16

    9   10  11  12              1   2   9   10
    
    13  14  15  16              5   6   13  14  


    [ 1, 2, 5, 6, 3, 4, 7, 8, 11, 12, 15, 16, 9, 10, 13, 14 ] 
    
    [ 3, 4, 7, 8, 11, 12, 15, 16, 9, 10, 13, 14, 1, 2, 5, 6  ]

    first = [1, 2, 5, 6]
    second = [ 3, 4, 7, 8 ]
    third = [11, 12, 15, 16]
    fourth = [9, 10, 13, 14]
    
    original = [ first, second, third, fourth  ]
    rotated = [ second, third, fourth, first  ]

    4 x 4
    
'''
import math


matrix = [ [5, 7, 9], [1, 3, 2], [8, 4, 6] ]

# [ [8, 1, 5], [4, 3, 7], [6, 2, 9]  ]

matrix2 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]  ]

# [ [7, 4, 1], [8, 5, 2], [9, 6, 3]  ] 

matrix3 = [ [5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16] ]

# [ [15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11] ]

def rotate_O_n(array):
    n = len(array)
    new_matrix = []
    for i in range(n):
        new_matrix.append([]) 

    
    for i in range(n):
        for j in range(n) :
            new_matrix[i].append((array[(n - 1 - j)][i]))
    
    return new_matrix 



def rotate_constant_space(array):
    size = len(array) 
    
    for row in range(size):
        for column in range(row, size - row  - 1):
            
            firstTemp = matrix[column][row]

            array[column][row] = matrix[size - row - 1][column] 
            array[size - row - 1][column] = matrix[size - column - 1][size - row - 1]
            array[size - column - 1][size - row - 1] = matrix[row][size - column - 1]
            array[row][size - column - 1] = firstTemp

    

print(matrix)
rotate_constant_space(matrix) 
print(matrix) 














#print(rotate_O_n(matrix))
#print(rotate_O_n(matrix2))
#print(rotate_O_n(matrix3))
