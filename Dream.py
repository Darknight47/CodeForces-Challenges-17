"""
--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2136/A -------------------------------------

Two football teams, the RiOI team and the KDOI team, are about to have a football match. 
A football match consists of two halves — the first half and the second half. At the beginning of the match, both teams have a score of 0.

As a fan of both teams, Aquawave knows that the two teams have similar levels, so neither team will score three consecutive goals in the same half.

Aquawave had a dream the night before the match, in which:

The score at the end of the first half was a:b, where a is the score of the RiOI team, and b is the score of the KDOI team;
And, the score at the end of the second half was c:d, where c is the score of the RiOI team, and d is the score of the KDOI team.
You have to determine whether Aquawave's dream can come true according to the above information.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). The description of the test cases follows.

The only line of each test case contains four integers a, b, c, and d (0 ≤ a ≤ c ≤ 100, 0 ≤ b ≤ d ≤ 100) — the score at the end of the first half and the score at the end of the second half.

Output
For each test case, print "YES" if Aquawave's dream can come true. Otherwise, print "NO".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
11
1 4 1 4
4 1 4 1
1 4 2 5
0 100 0 100
1 4 2 9
3 1 13 5
8 11 17 36
19 41 30 50
20 38 30 60
0 0 0 0
100 100 100 100

Output:
YES
YES
YES
NO
NO
YES
NO
NO
YES
YES
YES
"""
cases = int(input())
for _ in range(cases):
    a, b, c, d = map(int, input().split())
    firstHalf = max(a, b) <= 2 * min(a, b) + 2
    c = c - a
    d = d - b
    secondHalf = max(c, d) <= 2 * min(c, d) + 2
    if(firstHalf and secondHalf):
        print("YES")
    else:
        print("NO")