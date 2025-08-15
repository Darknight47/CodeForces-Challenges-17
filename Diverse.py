"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1994/A ------------------------------------------------

Petr, watching Sergey's stream, came up with a matrix a, consisting of n rows and m columns (the number in the i-th row and j-th column is denoted as ai,j), which contains all integers from 1 to n⋅m.
But he didn't like the arrangement of the numbers, and now he wants to come up with a new matrix b, consisting of n rows and m columns, 
which will also contain all integers from 1 to n⋅m, such that for any 1≤i≤n,1≤j≤m it holds that a(i) , j ≠ b(i) , j.

You are given the matrix a, construct any matrix b that meets Petr's requirements, or determine that it is impossible.

Hurry up! Otherwise, he will donate all his money to the stream in search of an answer to his question.

Input
Each test consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^3) — the number of test cases. Then follows the description of the test cases.

The first line of each test case contains two integers n and m (1 ≤ n, m ≤ 10) — the number of rows and columns of matrix a.

The next n lines contain m integers each, describing matrix a. The i-th of these lines contains the elements of matrix ai,1,ai,2,…,ai,m.

It is guaranteed that all numbers in matrix a are distinct and 1 ≤ a(i), j ≤ n⋅m.

It is guaranteed that the sum of n⋅m over all test cases does not exceed 5⋅10^4.

Output
For each test case, output n⋅m integers — any suitable matrix b, or −1 if such a matrix does not exist.

Input:
5
1 1
1
2 1
2
1
1 5
2 4 5 3 1
2 4
1 2 3 4
5 6 7 8
3 3
4 2 1
9 8 3
6 7 5

Output:
-1
1 
2 
4 5 3 1 2 
6 7 8 5 
2 3 4 1 
8 3 9 
7 5 6 
2 1 4 
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    if(n == 1 and m == 1):
        print(-1)
    else:
        flat = [matrix[i][j] for i in range(n) for j in range(m)]
        
        shifted = flat[-1:] + flat[:-1]
        
        b = [[0] * m for _ in range(n)]
        idx = 0
        valid = True
        for i in range(n):
            for j in range(m):
                if shifted[idx] == matrix[i][j]:
                    # Swap with next to avoid same position
                    if j + 1 < m:
                        shifted[idx], shifted[idx+1] = shifted[idx+1], shifted[idx]
                    else:
                        shifted[idx], shifted[idx-1] = shifted[idx-1], shifted[idx]
                b[i][j] = shifted[idx]
                idx += 1
        
        for row in b:
            print(*row)