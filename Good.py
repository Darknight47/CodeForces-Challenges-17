"""
-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1839/A ---------------------------------

You are given two integers n and k.

An array a1,a2,…,an of length n, consisting of zeroes and ones is good if for all integers i from 1 to n both of the following conditions are satisfied:

at least ⌈ik⌉ of the first i elements of a are equal to 1, at least ⌈ik⌉ of the last i elements of a are equal to 1.
Here, ⌈ik⌉ denotes the result of division of i by k, rounded up. For example, ⌈63⌉=2, ⌈115⌉=⌈2.2⌉=3 and ⌈74⌉=⌈1.75⌉=2.

Find the minimum possible number of ones in a good array.

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The only line of each test case contains two integers n, k (2 ≤ n ≤ 100, 1 ≤ k ≤ n) — the length of array and parameter k from the statement.

Output
For each test case output one integer — the minimum possible number of ones in a good array.

It can be shown that under the given constraints at least one good array always exists.

Input:
7
3 2
5 2
9 3
7 1
10 4
9 5
8 8

Output:
2
3
4
7
4
3
2
"""
import math
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    ans = math.ceil((n - 1) / k) + 1
    print(ans)