"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2003/B -----------------------------------


Turtle and Piggy are playing a game on a sequence. They are given a sequence a1,a2,…,an, and Turtle goes first. 
Turtle and Piggy alternate in turns (so, Turtle does the first turn, Piggy does the second, Turtle does the third, etc.).

The game goes as follows:

Let the current length of the sequence be m. If m=1, the game ends.
If the game does not end and it's Turtle's turn, then Turtle must choose an integer i such that 1≤i≤m−1, set ai to max(ai,ai+1), and remove ai+1.
If the game does not end and it's Piggy's turn, then Piggy must choose an integer i such that 1≤i≤m−1, set ai to min(ai,ai+1), and remove ai+1.
Turtle wants to maximize the value of a1 in the end, while Piggy wants to minimize the value of a1 in the end. Find the value of a1 in the end if both players play optimally.

You can refer to notes for further clarification.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 10^5) — the length of the sequence.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^5) — the elements of the sequence a.

It is guaranteed that the sum of n over all test cases does not exceed 10^5.

Output
For each test case, output a single integer — the value of a1 in the end if both players play optimally.


Input:
5
2
1 2
3
1 1 2
3
1 2 3
5
3 1 2 2 3
10
10 2 5 2 7 9 2 5 10 7

Output:
2
1
2
2
7
"""
def optimal_game_value(a):
    a.sort()
    n = len(a)
    moves = n - 1

    turtle_moves = (moves + 1) // 2  # Turtle starts
    piggy_moves = moves // 2


    start = turtle_moves

    end = n - piggy_moves


    remaining = a[start:end]

    return remaining[0]

cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    ans = optimal_game_value(arr)
    print(ans)