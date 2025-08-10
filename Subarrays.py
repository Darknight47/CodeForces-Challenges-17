"""
--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1686/B ----------------------------------

For an array [b1,b2,…,bm] define its number of inversions as the number of pairs (i,j) of integers such that 1 ≤ i < j ≤ m and b(i) > b(j). 
Let's call array b odd if its number of inversions is odd.

For example, array [4,2,7] is odd, as its number of inversions is 1, while array [2,1,4,3] isn't, as its number of inversions is 2.

You are given a permutation [p1,p2,…,pn] of integers from 1 to n (each of them appears exactly once in the permutation). 
You want to split it into several consecutive subarrays (maybe just one), so that the number of the odd subarrays among them is as large as possible.

What largest number of these subarrays may be odd?

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 10^5)  — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^5)  — the size of the permutation.

The second line of each test case contains n integers p1,p2,…,pn (1 ≤ p(i) ≤ n, all p(i) are distinct)  — the elements of the permutation.

The sum of n over all test cases doesn't exceed 2⋅10^5.

Output
For each test case output a single integer  — the largest possible number of odd subarrays that you can get after splitting the permutation into several consecutive subarrays.

Input:
5
3
1 2 3
4
4 3 2 1
2
1 2
2
2 1
6
4 5 6 1 2 3

Output:
0
2
0
1
1
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    idx = 0
    while idx < sze - 1:
        first = arr[idx]
        second = arr[idx + 1]
        if(first > second):
            ans += 1
            idx += 2
        else:
            idx += 1
        if idx >= sze:
            break
    print(ans)