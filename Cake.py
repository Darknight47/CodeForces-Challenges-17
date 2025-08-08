"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1654/A -------------------------------------

There are n pieces of cake on a line. The i-th piece of cake has weight ai (1 ≤ i ≤ n).

The tastiness of the cake is the maximum total weight of two adjacent pieces of cake (i. e., max(a1+a2,a2+a3,…,an−1+an)).

You want to maximize the tastiness of the cake. You are allowed to do the following operation at most once (doing more operations would ruin the cake):

Choose a contiguous subsegment a[l,r] of pieces of cake (1≤l≤r≤n), and reverse it.
The subsegment a[l,r] of the array a is the sequence al,al+1,…,ar.

If you reverse it, the array will become a1,a2,…,al−2,al−1,ar––,ar−1––––,…–––,al+1––––,al––,ar+1,ar+2,…,an−1,an.

For example, if the weights are initially [5,2,1,4,7,3], you can reverse the subsegment a[2,5], getting [5,7–,4–,1–,2–,3]. 
The tastiness of the cake is now 5+7=12 (while before the operation the tastiness was 4+7=11).

Find the maximum tastiness of the cake after doing the operation at most once.

Input
The first line contains a single integer t (1 ≤ t ≤ 50) — the number of test cases.

The first line of each test case contains a single integer n (2 ≤ n ≤ 1000) — the number of pieces of cake.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — ai is the weight of the i-th piece of cake.

Output
For each test case, print a single integer: the maximum tastiness of the cake after doing the operation at most once.

Input:
5
6
5 2 1 4 7 3
3
32 78 78
3
69 54 91
8
999021 999021 999021 999021 999652 999021 999021 999021
2
1000000000 1000000000

Output:
12
156
160
1998673
2000000000
"""
cases = int(input())
for _ in range(cases):
    input()
    arr = sorted(list(map(int, input().split())))
    print(arr[-1] + arr[-2])