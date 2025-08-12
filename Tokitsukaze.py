"""
-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1678/A --------------------------------------

Tokitsukaze has a sequence a of length n. For each operation, she selects two numbers ai and aj (i ≠ j; 1 ≤ i, j ≤ n).

If ai=aj, change one of them to 0.
Otherwise change both of them to min(ai,aj).
Tokitsukaze wants to know the minimum number of operations to change all numbers in the sequence to 0. It can be proved that the answer always exists.

Input
The first line contains a single positive integer t (1 ≤ t ≤ 1000) — the number of test cases.

For each test case, the first line contains a single integer n (2 ≤ n ≤ 100) — the length of the sequence a.

The second line contains n integers a1,a2,…,an (0 ≤ a(i) ≤ 100) — the sequence a.

Output
For each test case, print a single integer — the minimum number of operations to change all numbers in the sequence to 0.

Input:
3
3
1 2 3
3
1 2 2
3
1 2 0

Output:
4
3
2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = sorted(list(map(int, input().split())))
    tempSet = set(arr)
    if(arr[0] > 0):
        if(len(tempSet) == sze):
            print(sze + 1)
        else:
            print(sze)
    else:
        zeros = arr.count(0)
        print(sze - zeros)