"""
------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1845/A ----------------------------

You are given an integer n, which you want to obtain. You have an unlimited supply of every integer from 1 to k, except integer x (there are no integer x at all).

You are allowed to take an arbitrary amount of each of these integers (possibly, zero). Can you make the sum of taken integers equal to n?

If there are multiple answers, print any of them.

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of testcases.

The only line of each testcase contains three integers n,k and x (1 ≤ x ≤ k ≤ n ≤ 100).

Output
For each test case, in the first line, print "YES" or "NO" — whether you can take an arbitrary amount of each integer from 1 to k, except integer x, so that their sum is equal to n.

If you can, the second line should contain a single integer m — the total amount of taken integers. The third line should contain m integers — each of them from 1 to k, not equal to x, and their sum is n.

If there are multiple answers, print any of them.

Input:
5
10 3 2
5 2 1
4 2 1
7 7 3
6 1 1

Output:
YES
6
3 1 1 1 1 3
NO
YES
2
2 2
YES
1
7
NO
"""
cases = int(input())
for _ in range(cases):
    n, k, x = map(int, input().split())
    if x != 1:
        print("YES")
        print(n)
        print(*([1] * n))
    elif k == 1 or (k == 2 and n % 2 == 1):
        print("NO")
    else:
        print("YES")
        count = n // 2
        first = 3 if n % 2 == 1 else 2
        rest = [2] * (count - 1)
        print(count)
        print(first, *rest)