
'''
Yet another new challenge from the team. The ask is simple.
Given a positive integer n. generate an n x x matrix filled with elements from 1 to n^2 in spiral order
 
Examples are below
  
  
                                                           1 -->  2 -->  3 -->  4 --> 5
                                  1 -->  2 -->  3 --> 4                               |
                 1 --> 2 --> 3                        |   16 --> 17 --> 18 --> 19     6
       1 --> 2               |   12 --> 13 --> 14     5    |                    |     |
  1          |   8 --> 9     4    |             |     |   15     24 --> 25     20     7
       4 <-- 3   |           |   11     16 <-- 15     6    |      |             |     |
                 7 <-- 6 <-- 5    |                   |   14     23 <-- 22 <-- 21     8
                                 10 <--  9 <--  8 <-- 7    |                          |
                                                          13 <-- 12 <-- 11 <-- 10 <-- 9
       
n = 1   n = 2       n = 3                n = 4                       n = 5   
      
Below is the code that I could come up with.
But the code below is an exact replica on how we would manually fill.
If you could find a better way, please do let me know!
Thanks.
'''

if __name__ == "__main__" :
    size = 3
    matrix = [[0 for col in range(size)] for row in range(size)] 

    direction = 'R'
    row = 0
    col = 0
    
    for element in range(size*size):
        matrix[row][col] = element + 1
        if direction == 'R':
            if (col < (size - 1)) and (matrix[row][col + 1] == 0):
                col += 1
            else:
                direction = 'D'
                row += 1

        elif direction == 'D':
            if (row < (size - 1)) and (matrix[row + 1][col] == 0):
                row += 1
            else:
                direction = 'L'
                col -= 1

        elif direction == 'L':
            if (col > 0) and (matrix[row][col - 1] == 0):
                col -= 1
            else:
                direction = 'U'
                row -= 1

        elif direction == 'U':
            if (row > 0) and (matrix[row - 1][col] == 0):
                row -= 1
            else:
                direction = 'R'
                col += 1

    for r in matrix:
        print(r)