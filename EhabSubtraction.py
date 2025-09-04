"""

-------------------------------------------- Link for the challenge: https://codeforces.com/contest/1088/problem/B ---------------------------------------

You're given an array a. You should repeat the following operation k times: 
find the minimum non-zero element in the array, print it, and then subtract it from all the non-zero elements of the array. If all the elements are 0s, just print 0.

Input
The first line contains integers n and k (1 ≤ n, k ≤ 10^5), the length of the array and the number of operations you should perform.

The second line contains n space-separated integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9), the elements of the array.

Output
Print the minimum non-zero element before each operation in a new line.

Input:
3 5
1 2 3

Output:
1
1
1
0
0
"""
n, k = map(int, input().split())
arr = list(map(int, input().split()))

uniqueSorted = sorted(set(arr))
uniqueSorted = [x for x in uniqueSorted if x != 0]

prev = 0
count = 0

for num in uniqueSorted:
    print(num - prev)
    prev = num
    count += 1
    if(count == k):
        break

for _ in range(k - count):
    print(0)