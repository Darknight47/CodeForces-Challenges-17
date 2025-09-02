"""
--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2122/A -------------------------------------

A path in a grid is called greedy if it starts at the top-left cell and moves only to the right or downward, always moving to its neighbor with the greater value (or either if the values are equal).

The value of a path is the sum of the values of the cells it visits, including the start and end.

Does there exist an n×m grid of nonnegative integers such that no greedy path achieves the maximum value among all down/right paths?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 5000). The description of the test cases follows.

The only line of each test case contains two integers n, m (1 ≤ n, m ≤ 100) — the number of rows and columns in the grid, respectively.

Output
For each test case, on a separate line output "YES" if the required grid exists, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
2
3 3
1 2

Output:
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    if((n == 1 or m == 1) or (n == 2 and m == 2)):
        print("NO")
    else:
        print("YES")