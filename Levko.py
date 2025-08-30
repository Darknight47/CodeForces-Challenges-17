"""
-------------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/361/A ------------------------------------------------------

Levko loves tables that consist of n rows and n columns very much. He especially loves beautiful tables. A table is beautiful to Levko if the sum of elements in each row and column of the table equals k.

Unfortunately, he doesn't know any such table. Your task is to help him to find at least one of them.

Input
The single line contains two integers, n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 1000).

Output
Print any beautiful table. Levko doesn't like too big numbers, so all elements of the table mustn't exceed 1000 in their absolute value.

If there are multiple suitable tables, you are allowed to print any of them.

Input:
2 4

Output:
1 3
3 1
"""
n, k = map(int, input().split())
for i in range(n):
    row = []
    for j in range(n):
        row.append(k if i == j else 0)
    print(*row)