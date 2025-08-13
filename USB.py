"""
------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/609/A ------------------------------------------------

Sean is trying to save a large file to a USB flash drive. He has n USB flash drives with capacities equal to a1, a2, ..., an megabytes. The file size is equal to m megabytes.

Find the minimum number of USB flash drives needed to write Sean's file, if he can split the file between drives.

Input
The first line contains positive integer n (1 ≤ n ≤ 100) — the number of USB flash drives.

The second line contains positive integer m (1 ≤ m ≤ 105) — the size of Sean's file.

Each of the next n lines contains positive integer ai (1 ≤ ai ≤ 1000) — the sizes of USB flash drives in megabytes.

It is guaranteed that the answer exists, i. e. the sum of all ai is not less than m.

Output
Print the minimum number of USB flash drives to write Sean's file, if he can split the file between drives.

Input:
3
5
2
1
3

Output:
2
"""
n = int(input())
m = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
capacity = arr[0]
ans = 1
for i in range(1, len(arr)):
    if(capacity >= m):
        break
    capacity += arr[i]
    ans += 1
print(ans)