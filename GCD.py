"""
---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1665/A -----------------------------

You are given a positive integer n. You have to find 4 positive integers a,b,c,d such that

a + b + c+ d = n, and
gcd(a,b) = lcm(c,d).
If there are several possible answers you can output any of them. It is possible to show that the answer always exists.

In this problem gcd(a,b) denotes the greatest common divisor of a and b, and lcm(c,d) denotes the least common multiple of c and d.

Input
The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. Description of the test cases follows.

Each test case contains a single line with integer n (4 ≤ n ≤ 10^9) — the sum of a, b, c, and d.

Output
For each test case output 4 positive integers a, b, c, d such that a+b+c+d=n and gcd(a,b)=lcm(c,d).

Input:
5
4
7
8
9
10

Output:
1 1 1 1
2 2 2 1
2 2 2 2
2 4 2 1
3 5 1 1
"""
cases = int(input())
for _ in range(cases):
    num = int(input())
    print(num - 3, 1, 1, 1)