"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1750/A ---------------------------------

You are given a permutation a1,a2,…,an of size n, where each integer from 1 to n appears exactly once.

You can do the following operation any number of times (possibly, zero):

Choose any three indices i,j,k (1 ≤ i < j < k ≤ n).
If ai>ak, replace ai with ai+aj. Otherwise, swap aj and ak.
Determine whether you can make the array a sorted in non-descending order.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 5000) — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 10) — the length of the array a.

The second line contains n integers a1,a2,…,an (1≤ai≤n, ai≠aj if i≠j) — the elements of the array a.

Output
For each test case, output "Yes" (without quotes) if the array can be sorted in non-descending order, and "No" (without quotes) otherwise.

You can output "Yes" and "No" in any case (for example, strings "YES", "yEs" and "yes" will be recognized as a positive response).

Input:
7
3
1 2 3
3
1 3 2
7
5 3 4 7 6 2 1
7
7 6 5 4 3 2 1
5
2 1 4 5 3
5
2 1 3 4 5
7
1 2 6 7 4 3 5

Output:
Yes
Yes
No
No
No
No
Yes
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    print("YES" if arr[0] == 1 else "NO")