"""
------------------------------------------- Link for the challenge: https://codeforces.com/contest/2131/problem/B -------------------------------------------

You are given an integer n. Call an array a of length n good if:

For all 1≤i<n, ai⋅ai+1<0 (i.e., the product of adjacent elements is negative).
For all subarrays ∗ with length at least 2, the sum of all elements in the subarray is positive†. 
Additionally, we say a good array a of length n is better than another good array b of length n if [|a1|,|a2|,…,|an|] is lexicographically smaller‡ than [|b1|,|b2|,…,|bn|]. Note that |z| denotes the absolute value of integer z.

Output a good array of length n such that it is better than every other good array of length n.

∗ An array c is a subarray of an array d if c can be obtained from d by the deletion of several (possibly, zero or all) elements from the beginning and several 
(possibly, zero or all) elements from the end.

† An integer x is positive if x > 0.

‡ A sequence a is lexicographically smaller than a sequence b if and only if one of the following holds:

a is a prefix of b, but a≠b; or in the first position where a and b differ, the sequence a has a smaller element than the corresponding element in b.
Input
The first line contains an integer t (1 ≤ t ≤ 500) — the number of test cases.

The single line of each test case contains one integer n (2 ≤ n ≤ 2⋅10^5) — the length of your array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output n integers a1,a2,…,an (−10^9 ≤ a(i) ≤ 10^9), the elements of your array on a new line.

Input:
2
2
3

Output: 
-1 2
-1 3 -1
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = []
    for i in range(1, n + 1):
        if(i % 2 == 1):
            #arr.append(-1)
            print(-1, end=' ')
        else:
            if(i == n):
                #arr.append(2)
                print(2, end=' ')
            else:
                #arr.append(3)
                print(3, end=' ')
    print()