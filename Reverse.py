"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1638/A --------------------------------------

You are given a permutation p1,p2,…,pn of length n. You have to choose two integers l,r (1 ≤ l ≤ r ≤ n) and reverse the subsegment [l,r] of the permutation. 
The permutation will become p1,p2,…,pl−1,pr,pr−1,…,pl,pr+1,pr+2,…,pn.

Find the lexicographically smallest permutation that can be obtained by performing exactly one reverse operation on the initial permutation.

Note that for two distinct permutations of equal length a and b, a is lexicographically smaller than b if at the first position they differ, a has the smaller element.

A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order. 
For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 500) — the length of the permutation.

The second line of each test case contains n integers p1,p2,…,pn (1 ≤ pi ≤ n) — the elements of the permutation.

Output
For each test case print the lexicographically smallest permutation you can obtain.

Input:
4
1
1
3
2 1 3
4
1 4 2 3
5
1 2 3 4 5

Output:
1 
1 2 3 
1 2 4 3 
1 2 3 4 5 
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    i = -1
    for idx in range(n):
        if arr[idx] != idx + 1:  
            i = idx
            break
    if i != -1:
        j = arr.index(i + 1)
        arr[i:j+1] = reversed(arr[i:j+1])
    print(*arr)