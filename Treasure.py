"""
------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/2090/A ------------------------------------------

Little B and his friend Little K found a treasure map, and now they just need to dig up the treasure, which is buried at a depth of a.5 meters.

They take turns digging. On the first day, Little B digs; on the second day, Little K. After each day, they switch. 
Little B digs exactly x meters of soil each day, while Little K digs y meters. 
They became curious about who will dig up the treasure first, meaning during whose day the total dug depth will exceed a.5.

But they are too busy digging, so help them and tell who will dig up the treasure!

Input
The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of the test cases follows.

In a single line of each test case, three integers x,y,a are given (1 ≤ x, y, a ≤ 10^9).

Output
For each test case, output "NO" if Little B digs it up first; otherwise, output "YES". You can output the answer in any case.

Input:
3
1 2 4
2 1 4
2 2 1

Output:
YES
NO
NO
"""
cases = int(input())
for _ in range(cases):
    x, y, a = map(int, input().split())
    tempSum = x + y
    cycles = a // tempSum
    depth = cycles * tempSum

    if(depth + x > a):
        print("NO")
    else:
        print("YES")