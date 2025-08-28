"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1255/A ---------------------------------

Bob watches TV every day. He always sets the volume of his TV to b. However, today he is angry to find out someone has changed the volume to a. Of course, Bob has a remote control that can change the volume.

There are six buttons (−5,−2,−1,+1,+2,+5) on the control, which in one press can either increase or decrease the current volume by 1, 2, or 5. 
The volume can be arbitrarily large, but can never be negative. In other words, Bob cannot press the button if it causes the volume to be lower than 0.

As Bob is so angry, he wants to change the volume to b using as few button presses as possible. 
However, he forgets how to do such simple calculations, so he asks you for help. Write a program that given a and b, finds the minimum number of presses to change the TV volume from a to b.

Input
Each test contains multiple test cases. The first line contains the number of test cases T (1 ≤ T ≤ 1000). Then the descriptions of the test cases follow.

Each test case consists of one line containing two integers a and b (0 ≤ a, b ≤ 10^9) — the current volume and Bob's desired volume, respectively.

Output
For each test case, output a single integer — the minimum number of presses to change the TV volume from a to b. If Bob does not need to change the volume (i.e. a=b), then print 0.

Input:
3
4 0
5 14
3 9

Output:
2
3
2
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    diff = abs(a - b)
    fives = diff // 5
    diff = abs((fives * 5) - diff)
    if(diff > 0):      
        twos = diff // 2
    else:
        twos = diff // 2
    diff = abs((twos * 2) - diff)
    ans = fives + twos + diff
    print(ans)