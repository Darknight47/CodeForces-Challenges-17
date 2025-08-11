"""
------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1673/A -------------------------------------------

Alice and Bob are playing a game with strings. There will be t rounds in the game. In each round, there will be a string s consisting of lowercase English letters.

Alice moves first and both the players take alternate turns. Alice is allowed to remove any substring of even length (possibly empty) and Bob is allowed to remove any substring of odd length from s.

More formally, if there was a string s=s1s2…sk the player can choose a substring slsl+1…sr−1sr with length of corresponding parity and remove it. After that the string will become s=s1…sl−1sr+1…sk.

After the string becomes empty, the round ends and each player calculates his/her score for this round. The score of a player is the sum of values of all characters removed by him/her. 
The value of a is 1, the value of b is 2, the value of c is 3, …, and the value of z is 26. 
The player with higher score wins the round. For each round, determine the winner and the difference between winner's and loser's scores. Assume that both players play optimally to maximize their score. 
It can be proved that a draw is impossible.

Input
The first line of input contains a single integer t (1 ≤ t ≤ 5⋅10^4) denoting the number of rounds.

Each of the next t lines contain a single string s (1 ≤ |s| ≤ 2⋅10^5) consisting of lowercase English letters, denoting the string used for the round. Here |s| denotes the length of the string s.

It is guaranteed that the sum of |s| over all rounds does not exceed 2⋅10^5.

Output
For each round, print a single line containing a string and an integer. If Alice wins the round, the string must be "Alice". If Bob wins the round, the string must be "Bob". 
The integer must be the difference between their scores assuming both players play optimally.

Input:
5
aba
abc
cba
n
codeforces

Output:
Alice 2
Alice 4
Alice 4
Bob 14
Alice 93
"""
cases = int(input())
for _ in range(cases):
    s = input()
    if(len(s) == 1):
        print("Bob", ord(s[0]) - 96)
    elif(len(s) % 2 == 0):
        temp = sum(ord(c) - 96 for c in s)
        print("Alice", temp)
    else:
        first = ord(s[0]) - 96
        last = ord(s[-1]) - 96
        alice = 0
        bob = min(first, last)
        for c in s:
            alice += ord(c) - 96
        alice -= bob
        if(alice > bob):
            print("Alice", alice - bob)
        else:
            print("Bob", bob - alice)      