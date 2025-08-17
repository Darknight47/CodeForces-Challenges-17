"""

------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2047/B -----------------------------


You're given a string s of length n, consisting of only lowercase English letters.

You must do the following operation exactly once:

Choose any two indices i and j (1 ≤ i, j ≤ n). You can choose i=j.
Set si:=sj.
You need to minimize the number of distinct permutations† of s. 
Output any string with the smallest number of distinct permutations after performing exactly one operation.

† A permutation of the string is an arrangement of its characters into any order. For example, "bac" is a permutation of "abc" but "bcc" is not.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains n (1 ≤ n ≤ 10) — the length of string s.

The second line of each test case contains s of length n. The string contains only lowercase English letters.

Output
For each test case, output the required s after applying exactly one operation. If there are multiple solutions, print any of them.

Input:
6
3
abc
4
xyyx
8
alphabet
1
k
10
aabbccddee
6
ttbddq

Output:
cbc
yyyx
alphaaet
k
eabbccddee
tttddq
"""
from collections import Counter
def transform_string(s: str) -> str:
    if len(s) <= 1:
        return s

    freq = Counter(s)
    min_count = min(freq.values())
    max_count = max(freq.values())

    least_frequent = [char for char in freq if freq[char] == min_count]
    most_frequent = [char for char in freq if freq[char] == max_count]


    for l_char in least_frequent:
        for m_char in most_frequent:
            if l_char != m_char:
                char_to_remove = l_char
                char_to_add = m_char
                break
        else:
            continue
        break
    else:
        if len(s) > 1:
            char_to_remove = s[1]
            char_to_add = s[0]
        else:
            return s

    result = list(s)
    for i, c in enumerate(result):
        if c == char_to_remove:
            result[i] = char_to_add
            break

    return ''.join(result)

cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    print(transform_string(s))