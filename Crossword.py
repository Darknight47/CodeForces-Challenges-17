"""


Recently Adaltik discovered japanese crosswords. Japanese crossword is a picture, represented as a table sized a × b squares, and each square is colored white or black. 
There are integers to the left of the rows and to the top of the columns, encrypting the corresponding row or column. 
The number of integers represents how many groups of black squares there are in corresponding row or column, 
and the integers themselves represents the number of consecutive black squares in corresponding group (you can find more detailed explanation in Wikipedia https://en.wikipedia.org/wiki/Japanese_crossword).

Adaltik decided that the general case of japanese crossword is too complicated and drew a row consisting of n squares (e.g. japanese crossword sized 1 × n),
which he wants to encrypt in the same way as in japanese crossword.

Help Adaltik find the numbers encrypting the row he drew.

Input
The first line of the input contains a single integer n (1 ≤ n ≤ 100) — the length of the row. The second line of the input contains a single string consisting of n characters 'B' or 'W', 
('B' corresponds to black square, 'W' — to white square in the row that Adaltik drew).

Output
The first line should contain a single integer k — the number of integers encrypting the row, e.g. the number of groups of black squares in the row.

The second line should contain k integers, encrypting the row, e.g. corresponding to sizes of groups of consecutive black squares in the order from left to right.

Input:
3
BBW

Output:
1
2
"""
sze = int(input())
password = input()
arr = []
tempCount = 0
for i in range(sze):
    temp = password[i]
    if(temp == 'B'):
        tempCount += 1
    else:
        if(tempCount > 0):
            arr.append(tempCount)
            tempCount = 0
if(tempCount > 0):
    arr.append(tempCount)
print(len(arr))
if(len(arr) > 0):
    print(*arr)