"""
-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1956/B ------------------------------------------


You and Nene are playing a card game. The deck with 2n cards is used to play this game. 
Each card has an integer from 1 to n on it, and each of integers 1 through n appears exactly on 2 cards. 
Additionally, there is a table where cards are placed during the game (initially, the table is empty).

In the beginning of the game, these 2n cards are distributed between you and Nene so that each player receives n cards.

After it, you and Nene alternatively take 2n turns, i.e. each person takes n turns, starting with you. On each turn:

The player whose turn is it selects one of the cards in his hand. Let x be the number on it.
The player whose turn is it receives 1 point if there is already a card with the integer x on the table (otherwise, he receives no points). After it, he places the selected card with the integer x on the table.
Note that turns are made publicly: each player can see all the cards on the table at each moment.

Nene is very smart so she always selects cards optimally in order to maximize her score in the end of the game (after 2n rounds). If she has several optimal moves, she selects the move that minimizes your score in the end of the game.

More formally, Nene always takes turns optimally in order to maximize her score in the end of the game in the first place and to minimize your score in the end of the game in the second place.

Assuming that the cards are already distributed and cards in your hand have integers a1,a2,…,an written on them, what is the maximum number of points you can get by taking your turns optimally?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of test cases follows.

The first line contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the number of cards you and Nene receive in the beginning of the game.

The second line contains n integers a1,a2,…,an (1 ≤ a(i) ≤ n) — the integers on the cards in your hand. 
It is guaranteed that each integer from 1 through n appears in the sequence a1,a2,…,an at most 2 times.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output one integer: the maximum number of points you can get.

Input:
5
4
1 1 2 3
8
7 4 1 2 8 8 5 5
8
7 1 4 5 3 4 2 6
3
1 2 3
1
1

Output:
1
2
1
0
0
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    counts = Counter(arr)
    ans = 0
    for tk, tv in counts.items():
        if(tv == 2):
            ans += 1
    print(ans)