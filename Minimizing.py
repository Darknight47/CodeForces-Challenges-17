"""
----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1706/A -------------------------------------------


You have a sequence a1,a2,…,an of length n, consisting of integers between 1 and m. You also have a string s, consisting of m characters B.

You are going to perform the following n operations.

At the i-th (1 ≤ i ≤ n) operation, you replace either the ai-th or the (m+1−ai)-th character of s with A. You can replace the character at any position multiple times through the operations.
Find the lexicographically smallest string you can get after these operations.

A string x is lexicographically smaller than a string y of the same length if and only if in the first position where x and y differ, 
the string x has a letter that appears earlier in the alphabet than the corresponding letter in y.

Input
The first line contains the number of test cases t (1 ≤ t ≤ 2000).

The first line of each test case contains two integers n and m (1 ≤ n, m ≤ 50) — the length of the sequence a and the length of the string s respectively.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ m) — the sequence a.

Output
For each test case, print a string of length m — the lexicographically smallest string you can get. Each character of the string should be either capital English letter A or capital English letter B.

Input:
6
4 5
1 1 3 1
1 5
2
4 1
1 1 1 1
2 4
1 3
2 7
7 5
4 5
5 5 3 5

Output:
ABABA
BABBB
A
AABB
ABABBBB
ABABA
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    s = ['B'] * m
    for val in arr:
        i = val - 1
        j = m - val
        chosen = min(i, j)
        fallback = max(i, j)
        if s[chosen] == 'B':
            s[chosen] = 'A'
        else:
            s[fallback] = 'A'
    print(''.join(s))