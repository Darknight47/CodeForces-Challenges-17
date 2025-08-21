"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1746/B ----------------------------------

You have an array a of size n consisting only of zeroes and ones. You can do the following operation:

choose two indices 1 ≤ i, j ≤ n, i ≠ j,
add a(i) to a(j),
remove a(i) from a.
Note that elements of a can become bigger than 1 after performing some operations. Also note that n becomes 1 less after the operation.

What is the minimum number of operations needed to make a non-decreasing, i. e. that each element is not less than the previous element?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains an integer n (1 ≤ n ≤ 10^5), the size of array a.

Next line contains n integers a1,a2,…an (a(i) is 0 or 1), elements of array a.

It's guaranteed that sum of n over all test cases doesn't exceed 2⋅10^5.

Output
For each test case print a single integer, minimum number of operations needed to make a non-decreasing.

Input:
4
8
0 0 1 1 1 1 1 1
5
1 0 0 1 1
2
1 0
11
1 1 0 0 1 0 0 1 1 1 0

Output:
0
1
1
3
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    operations = 0
    left = 0
    right = sze - 1
    while left < right:

        while left < right and arr[left] != 1:
            left += 1

        while left < right and arr[right] != 0:
            right -= 1
        if left < right:
            operations += 1
            left += 1
            right -= 1
    print(operations)