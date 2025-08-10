"""
------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/755/A ------------------------------------

PolandBall is a young, clever Ball. He is interested in prime numbers. He has stated a following hypothesis: 
"There exists such a positive integer n that for each positive integer m number n·m + 1 is a prime number".

Unfortunately, PolandBall is not experienced yet and doesn't know that his hypothesis is incorrect. Could you prove it wrong? Write a program that finds a counterexample for any n.

Input
The only number in the input is n (1 ≤ n ≤ 1000) — number from the PolandBall's hypothesis.

Output
Output such m that n·m + 1 is not a prime number. Your answer will be considered correct if you output any suitable m such that 1 ≤ m ≤ 103. It is guaranteed the the answer exists.

Input:
3

Output:
1
"""
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input())
for i in range(1, 100):
    prime = is_prime((n * i) + 1)
    if(not prime):
        print(i)
        break