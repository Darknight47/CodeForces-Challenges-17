"""
------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2131/A -------------------------------------------

In Divergent Universe, The Lever iterates itself given two arrays a and b of length n. In each iteration, The Lever will do the following:

Choose a random index i such that a(i) > b(i). Then, decrease a(i) by 1. 
If there does not exist such i, ignore this step.
Choose a random index i such that a(i) < b(i). Then, increase a(i) by 1. If there does not exist such i, ignore this step.
After each iteration, the Lever will check if step 1 is ignored, and if so, it will end its iteration.

You're given the two arrays. Find the number of iterations that the Lever does. 
It can be shown this number is fixed over all possibilities of random indices that The Lever can choose for each step.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains one integer n (1 ≤ n ≤ 10).

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10).

The third line of each test case contains n integers b1,b2,…,bn (1 ≤ b(i) ≤ 10).

Output
For each test case, output one integer — the number of iterations that the Lever does.

Input:
4
2
7 3
5 6
3
3 1 4
3 1 4
1
10
1
6
1 1 4 5 1 4
1 9 1 9 8 1

Output:
3
1
10
7
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    ans = 1
    for i in range(sze):
        first = arr[i]
        second = brr[i]
        if(first > second):
            ans += (first - second)
    print(ans)