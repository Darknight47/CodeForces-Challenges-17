"""
-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1805/B --------------------------------

You are given a string s. You can apply this operation to the string exactly once: choose index i and move character s(i) to the beginning of the string (removing it at the old position). 
For example, if you apply the operation with index i=4 to the string "abaacd" with numbering from 1, you get the string "aabacd". What is the lexicographically minimal† string you can obtain by this operation?

† A string a is lexicographically smaller than a string b of the same length if and only if the following holds:

in the first position where a and b differ, the string a has a letter that appears earlier in the alphabet than the corresponding letter in b.
Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5) — the length of the string.

The second line of each test case contains the string s of length n, consisting of lowercase English letters.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, on a separate line print the lexicographically smallest string that can be obtained after applying the operation to the original string exactly once.

Input:
4
3
cba
4
acac
5
abbcb
4
aaba

Output:
acb
aacc
abbcb
aaab
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    s = input()
    min_char = s[0]
    min_index = 0
    for i in range(1, len(s)):
        if s[i] <= min_char:
            min_char = s[i]
            min_index = i
    if(s[min_index] > s[0]):
        print(s)
    else:
        temp = s[min_index]
        tempStr = s[:min_index] + s[min_index + 1:]
        ans = temp  + tempStr
        print(ans)