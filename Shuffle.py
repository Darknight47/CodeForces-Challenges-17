"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1459/A -------------------------------------------------


There are n cards numbered 1,…,n. The card i has a red digit ri and a blue digit bi written on it.

We arrange all n cards in random order from left to right, with all permutations of 1,…,n having the same probability. We then read all red digits on the cards from left to right, and obtain an integer R. 
In the same way, we read all blue digits and obtain an integer B. 
When reading a number, leading zeros can be ignored. If all digits in a number are zeros, then the number is equal to 0. 
Below is an illustration of a possible rearrangement of three cards, and how R and B can be found.

Two players, Red and Blue, are involved in a bet. Red bets that after the shuffle R > B, and Blue bets that R<B. If in the end R=B, the bet results in a draw, and neither player wins.

Determine, which of the two players is more likely (has higher probability) to win the bet, or that their chances are equal. 
Refer to the Note section for a formal discussion of comparing probabilities.

Input
The first line contains a single integer T (1 ≤ T ≤ 100) — the number of test cases.

Descriptions of T test cases follow. Each test case description starts with a line containing a single integer n (1 ≤ n ≤ 1000) — the number of cards.

The following line contains a string of n digits r1,…,rn — red digits on cards 1,…,n respectively.

The following line contains a string of n digits b1,…,bn — blue digits on cards 1,…,n respectively.

Note that digits in the same line are not separated with any delimiters.

Output
Print T answers for the test cases in order, one per line.

If Red has a strictly higher change to win, print "RED".

If Blue has a strictly higher change to win, print "BLUE".

If both players are equally likely to win, print "EQUAL".

Note that all answers are case-sensitive.

Input:
3
3
777
111
3
314
159
5
09281
09281

Output:
RED
BLUE
EQUAL
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    red = input().strip()
    blue = input().strip()
    reds, blues = 0, 0
    for i in range(sze):
        r = int(red[i])
        b = int(blue[i])
        if(r > b):
            reds += 1
        elif(b > r):
            blues += 1
    if(reds > blues):
        print("RED")
    elif(blues > reds):
        print("BLUE")
    else:
        print("EQUAL")