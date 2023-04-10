'''
Zero Matrix : Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0. 

m = rows
n = cols 

        2 x 3 


        0 2 3           0 0 0 
                ===>    
        4 5 6           0 4 6 

    
        1  2  3  4              1  2  0  4 

        5  6  0  8      ==>     0  0  0  0 

        9  10 11 12             9  10 0  12  

representation = [ [1, 2, 3, 4], [5, 6, 0, 8 ], [9, 10, 11, 12] ]
post_transform = [ [1, 2, 0, 4], [0, 0, 0, 0], [9, 10, 0, 12]  ] 
'''


matrix1 = [ [1, 2, 3, 4], [5, 6, 0, 8 ], [9, 10, 11, 12] ]

another_matrix = [ [0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 16]  ]

'''

This solution works, but only if there is one zero in the matrix. 
Once there is more than one zero, we will start seeing the zeros that
we have added and we'll begin changing a whole bunch of other 
stuff to zeros that really shouldn't be zeros 

'''

def set_row(array, row):
    for i in range(len(array[row])):
        array[row][i] = 0 

def set_column(array, column):
    for i in range(len(array)):
        array[i][column] = 0 


def first_attempt(array):
    finished = False 
    for i in range(len(array)): 
        for j in range(len(array[i])):
            if array[i][j] == 0:
                set_row(array, i)
                set_column(array, j)
                finished = True
            if finished : break
        if finished : break 



'''
This solution works, but it takes O(mn) space
'''


def second_attempt(array):
    track_rows = [False] * len(array) 
    track_cols = [False] * len(array[0])

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                track_rows[i] = True 
                track_cols[j] = True


    for row in range(len(track_rows)):
        if track_rows[row]:
            for col in range(len(array[row])):
                array[row][col] = 0 

    for col in range(len(track_cols)):
        if track_cols[col]:
            for row in range(len(array)):
                array[row][col] = 0 
    

'''
This solution requires O(1) space
'''
def third_attempt(array): 
    rowHasZero = False
    colHasZero = False 
    
    def set_row(array, row):
        for i in range(len(array[row])):
            array[row][i] = 0 

    def set_column(array, column):
        for i in range(len(array)):
            array[i][column] = 0 


    #Check if first row has a zero
    for j in range(len(array[0])):
        if array[0][j] == 0:
            rowHasZero = True
            break 

    #Check if first column has a zero 
    for i in range(len(array)):
        if array[i][0] == 0:
            colHasZero = True 
            break

    #Check for zeros in the rest of the array
    for i in range(1, len(array)):
        for j in range(1, len(array[0])):
            if array[i][j] == 0 :
                array[i][0] = 0 
                array[0][j] = 0 

    #Nullify rows based on values in first column 
    for i in range(1, len(array)):
        if array[i][0] == 0:
            set_row(array, i)

    #Nullify columns based on values in first row
    for j in range(1, len(array[0])):
        if array[0][j] == 0:
            set_column(array, j)

    #Nullify first row
    if rowHasZero:
        set_row(array, 0)

    #Nullify first column
    if colHasZero:
        set_column(array, 0) 


print(matrix1)
third_attempt(matrix1) 
print(matrix1) 




'''
print(another_matrix)
second_attempt(another_matrix) 
print(another_matrix)
print("")
print(matrix1)
second_attempt(matrix1)
print(matrix1)
'''



