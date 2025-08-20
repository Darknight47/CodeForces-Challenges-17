"""
---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1582/A --------------------------------------

Luntik has decided to try singing. He has a one-minute songs, b two-minute songs and c three-minute songs. 
He wants to distribute all songs into two concerts such that every song should be included to exactly one concert.

He wants to make the absolute difference of durations of the concerts as small as possible. The duration of the concert is the sum of durations of all songs in that concert.

Please help Luntik and find the minimal possible difference in minutes between the concerts durations.

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

Each test case consists of one line containing three integers a,b,c (1 ≤ a, b, c ≤ 10^9)— the number of one-minute, two-minute and three-minute songs.

Output
For each test case print the minimal possible difference in minutes between the concerts durations.

Input:
4
1 1 1
2 1 3
5 5 5
1 1 2

Output:
0
1
0
1
"""
cases = int(input())
for _ in range(cases):
    a, b, c = map(int, input().split())
    oneMin = a
    twoMins = b * 2
    threeMins = c * 3
    total = oneMin + twoMins + threeMins
    ans = total % 2
    print(ans)