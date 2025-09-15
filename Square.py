"""
---------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2008/B ----------------------------------------------


A beautiful binary matrix is a matrix that has ones on its edges and zeros inside.

Today, Sakurako was playing with a beautiful binary matrix of size r×c and created a binary string s by writing down all the rows of the matrix, starting from the first and ending with the r-th. 
More formally, the element from the matrix in the i-th row and j-th column corresponds to the ((i−1)∗c+j)-th element of the string.

You need to check whether the beautiful matrix from which the string s was obtained could be squared. 
In other words, you need to check whether the string s could have been build from a square beautiful binary matrix (i.e., one where r=c).

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains a single integer n (2 ≤ n ≤ 2⋅10^5) — the length of the string.

The second line of each test case contains the string s of length n. The string is always the result of writing out the strings of a beautiful matrix.

It is guaranteed that the sum of n across all test cases does not exceed 2⋅10^5.

Output
Print "Yes", if the original matrix could have been square, and "No" otherwise.

Input:
5
2
11
4
1111
9
111101111
9
111111111
12
111110011111

Output:
No
Yes
Yes
No
No
"""
import math
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    r = int(math.sqrt(sze))
    ok = True
    if r * r != sze:
        ok = False
    else:
        matrix = [s[i*r:(i+1)*r] for i in range(r)]
        for i in range(r):
            row = matrix[i]
            if i == 0 or i == r - 1:
                if row != '1' * r:
                    ok = False
                    break
            else:
                if row[0] != '1' or row[-1] != '1':
                    ok = False
                    break
                if any(ch != '0' for ch in row[1:-1]):
                    ok = False
                    break
    print("Yes" if ok else "No")