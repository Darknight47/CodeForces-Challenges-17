"""
-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2134/A --------------------------------


You are given three positive integers n, a, and b (1 ≤ a, b ≤ n).

Consider a row of n cells, initially all white and indexed from 1 to n. You will perform the following two steps in order:

Choose an integer x such that 1≤x≤n−a+1, and paint the a consecutive cells x,x+1,…,x+a−1 red.
Choose an integer y such that 1≤y≤n−b+1, and paint the b
 consecutive cells y,y+1,…,y+b−1 blue.
If a cell is painted both red and blue, its final color is blue.

A coloring of the grid is considered symmetric if, for every integer i from 1 to n (inclusive), the color of cell i is the same as the color of cell (n+1−i). 
Your task is to determine whether there exist integers x and y such that the final coloring of the grid is symmetric.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first and the only line of each test case contains three integers n, a, and b (1 ≤ n ≤ 10^9, 1 ≤ a, b ≤ n) — the number of cells of the grid and the number of cells to be painted in each step.

Output
For each testcase, output "YES" if it is possible that the final coloring of the grid is symmetric; otherwise, output "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
7
5 3 1
4 1 2
7 7 4
8 3 7
1 1 1
1000000000 1000000000 1000000000
3 2 1

Output:
YES
YES
NO
NO
YES
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n, a, b = map(int, input().split())
    if(a > b):
        if(n % 2 != a % 2 or n % 2 != b % 2):
            print("NO")
        else:
            print("YES")
    else:
        if(n % 2 == b % 2):
            print("YES")
        else:
            print("NO")