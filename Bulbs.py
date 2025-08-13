"""
------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/615/A -------------------------------------------

Vasya wants to turn on Christmas lights consisting of m bulbs. Initially, all bulbs are turned off. 
There are n buttons, each of them is connected to some set of bulbs. 
Vasya can press any of these buttons. When the button is pressed, it turns on all the bulbs it's connected to. Can Vasya light up all the bulbs?

If Vasya presses the button such that some bulbs connected to it are already turned on, they do not change their state, i.e. remain turned on.

Input
The first line of the input contains integers n and m (1 ≤ n, m ≤ 100) — the number of buttons and the number of bulbs respectively.

Each of the next n lines contains xi (0 ≤ xi ≤ m) — the number of bulbs that are turned on by the i-th button, and then xi numbers y_ij (1 ≤ yij ≤ m) — the numbers of these bulbs.

Output
If it's possible to turn on all m bulbs print "YES", otherwise print "NO".

Input:
3 4
2 1 4
3 1 3 1
1 2

Output:
YES
"""
n, m = map(int, input().split())
turned_on = set()

for _ in range(n):
    data = list(map(int, input().split()))
    bulbs = data[1:]  
    turned_on.update(bulbs)

if len(turned_on) == m:
    print("YES")
else:
    print("NO")
