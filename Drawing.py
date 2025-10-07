"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1929/B --------------------------------------------

Even in kindergarten, Sasha liked a girl. Therefore, he wanted to give her a drawing and attract her attention.

As a drawing, he decided to draw a square grid of size n×n, in which some cells are colored. 
But coloring the cells is difficult, so he wants to color as few cells as possible. But at the same time, he wants at least k diagonals to have at least one colored cell. 
Note that the square grid of size n×n has a total of 4n−2 diagonals.

Help little Sasha to make the girl fall in love with him and tell him the minimum number of cells he needs to color.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The only line of each test case contains two integers n and k (2 ≤ n ≤ 10^8, 1 ≤ k ≤ 4n−2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.

Output
For each test case, output a single integer — the minimum number of cells that need to be colored.

Input:
7
3 4
3 3
3 10
3 9
4 7
7 11
2 3

Output:
2
2
6
5
4
6
2
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    if k <= 4 * n - 4:
        ans =  (k + 1) // 2
    elif k == 4 * n - 3:
        ans =  (k + 1) // 2
    else:  # k == 4n - 2
        ans =  (k // 2) + 1
    print(ans)