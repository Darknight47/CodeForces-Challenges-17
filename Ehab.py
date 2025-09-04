"""
------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1088/A ------------------------------------

Given an integer x, find 2 integers a and b such that:

1 ≤ a, b ≤ x
b divides a (a is divisible by b).
a⋅b > x.
ab < x.
Input
The only line contains the integer x (1 ≤ x ≤ 100).

Output
You should output two integers a and b, satisfying the given conditions, separated by a space. If no pair of integers satisfy the conditions above, print "-1" (without quotes).

Input:
10

Output:
6 3
"""
num = int(input())
if(num == 1):
    print(-1)
else:
    print(num, num)