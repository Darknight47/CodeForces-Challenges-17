"""
---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1890/B ---------------------------------------


Qingshan has a string s, while Daniel has a string t. Both strings only contain 0 and 1.

A string a of length k is good if and only if

ai ≠ ai+1 for all i=1,2,…,k−1.
For example, 1, 101, 0101 are good, while 1, 1001, 001100 are not good.

Qingshan wants to make s good. To do this, she can do the following operation any number of times (possibly, zero):

insert t to any position of s (getting a new s).
Please tell Qingshan if it is possible to make s good.

Input
The input consists of multiple test cases. The first line contains a single integer T (1 ≤ T ≤ 2000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n and m (1 ≤ n, m ≤ 50) — the length of the strings s and t, respectively.

The second line of each test case contains a string s of length n.

The third line of each test case contains a string t of length m.

It is guaranteed that s and t only contain 0 and 1.

Output
For each test case, print "YES" (without quotes), if it is possible to make s good, and "NO" (without quotes) otherwise.

You can print letters in any case (upper or lower).

Input:
5
1 1
1
0
3 3
111
010
3 2
111
00
6 7
101100
1010101
10 2
1001001000
10


Output:
Yes
Yes
No
No
No
"""
cases = int(input())
for _ in range(cases):
    n, m = map(int, input().split())
    s = input()
    t = input()
    sOk = True
    tOk = True
    for i in range(n - 1):
        if(s[i] == s[i + 1]):
            sOk = False
            break
    if(not sOk):
        for i in range(m - 1):
            if(t[i] == t[i + 1]):
                tOk = False
                break

        if(tOk):
            firsT = t[0]
            lasT = t[-1]
            ok = True
            for j in range(n - 1):
                first = s[j]
                second = s[j + 1]
                if(first == second):
                    if(first == firsT or second == lasT):
                        ok = False
                        break
            print("YES" if ok else "NO")
        else:
            print("NO")
    else:
        print("YES")