"""
--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1635/B -----------------------------------------

You are given an array a of size n. Each element in this array is an integer between 1 and 10^9.

You can perform several operations to this array. During an operation, you can replace an element in the array with any integer between 1 and 10^9.

Output the minimum number of operations needed such that the resulting array doesn't contain any local maximums, and the resulting array after the operations.

An element ai is a local maximum if it is strictly larger than both of its neighbors (that is, ai>ai−1 and ai > ai+1). 
Since a1 and an have only one neighbor each, they will never be a local maximum.

Input
Each test contains multiple test cases. The first line will contain a single integer t (1 ≤ t ≤ 10000) — the number of test cases. Then t test cases follow.

The first line of each test case contains a single integer n (2 ≤ n ≤ 2⋅10^5) — the size of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9), the elements of array.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, first output a line containing a single integer m — minimum number of operations required. 
Then ouput a line consist of n integers — the resulting array after the operations. Note that this array should differ in exactly m elements from the initial array.

If there are multiple answers, print any.

Input:
5
3
2 1 2
4
1 2 3 1
5
1 2 1 2 1
9
1 2 1 3 2 3 1 2 1
9
2 1 3 1 3 1 3 1 3

Output:
0
2 1 2
1
1 3 3 1
1
1 2 2 2 1
2
1 2 3 3 2 3 3 2 1
2
2 1 3 3 3 1 1 1 3
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    op = 0
    i = 1
    while i < sze - 1:
        left = arr[i - 1]
        midd = arr[i]
        right = arr[i + 1]
        
        if midd > left and midd > right:
            op += 1
            if (i + 2 < sze):
                arr[i + 1] = max(midd, arr[i + 2])
            else:
                arr[i + 1] = midd
            i += 2  
        else:
            i += 1
    print(op)
    print(*arr)