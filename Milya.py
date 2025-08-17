"""
--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2059/A -----------------------------------------

An array is called good if for any element x that appears in this array, it holds that x appears at least twice in this array. 
For example, the arrays [1,2,1,1,2], [3,3], and [1,2,4,1,2,4] are good, while the arrays [1], [1,2,1], and [2,3,4,4] are not good.

Milya has two good arrays a and b of length n. 
She can rearrange the elements in array a in any way. After that, she obtains an array c of length n, where ci=ai+bi (1 ≤ i ≤ n).

Determine whether Milya can rearrange the elements in array a such that there are at least 3 distinct elements in array c.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (3 ≤ n ≤ 50) — the length of the arrays a and b.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the elements of the array a.

The third line of each test case contains n integers b1,b2,…,bn (1 ≤ b(i) ≤ 10^9) — the elements of the array b.

Output
For each test case, output «YES» (without quotes) if it is possible to obtain at least 3 distinct elements in array c, and «NO» otherwise.

You can output each letter in any case (for example, «YES», «Yes», «yes», «yEs» will be recognized as a positive answer).

Input:
5
4
1 2 1 2
1 2 1 2
6
1 2 3 3 2 1
1 1 1 1 1 1
3
1 1 1
1 1 1
6
1 52 52 3 1 3
59 4 3 59 3 4
4
100 1 100 1
2 2 2 2

Output:
YES
YES
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    setArr = set(arr)
    setBrr = set(brr)
    ok = True
    if(len(setArr) == 1 and len(setBrr) <= 2):
        ok = False
    elif(len(setArr) == 2 and len(setBrr) == 1):
        ok = False
    
    print("YES" if ok else "NO")