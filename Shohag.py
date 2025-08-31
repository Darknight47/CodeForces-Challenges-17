"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2039/A -----------------------------------

Shohag has an integer n. Please help him find an increasing integer sequence 1≤a1<a2<…<an≤100 such that a(i) mod i ≠ a(j) mod(j) ∗ is satisfied over all pairs 1 ≤ i < j ≤ n.

It can be shown that such a sequence always exists under the given constraints.

∗ a mod b denotes the remainder of a after division by b. For example, 7 mod 3 =1 ,8 mod 4 = 0 and 69 mod 10 = 9.

Input
The first line contains a single integer t (1 ≤ t ≤ 50) — the number of test cases.

The first and only line of each test case contains an integer n (2 ≤ n ≤ 50).

Output
For each test case, print n integers — the integer sequence that satisfies the conditions mentioned in the statement. If there are multiple such sequences, output any.

Input:
2
3
6

Output:
2 7 8
2 3 32 35 69 95
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = [2 * i - 1 for i in range(1, n + 1)]
    print(*arr)