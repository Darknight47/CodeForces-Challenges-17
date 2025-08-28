"""
------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2034/A -------------------------------------------

There is a tale about the wise King Keykhosrow who owned a grand treasury filled with treasures from across the Persian Empire. 
However, to prevent theft and ensure the safety of his wealth, King Keykhosrow's vault was sealed with a magical lock that could only be opened by solving a riddle.

The riddle involves two sacred numbers a and b. To unlock the vault, the challenger must determine the smallest key number m that satisfies two conditions:

m must be greater than or equal to at least one of a and b.
The remainder when m is divided by a must be equal to the remainder when m is divided by b.
Only by finding the smallest correct value of m can one unlock the vault and access the legendary treasures!

Input
The first line of the input contains an integer t (1 ≤ t ≤ 100), the number of test cases.

Each test case consists of a single line containing two integers a and b (1 ≤ a, b ≤ 1000).

Output
For each test case, print the smallest integer m that satisfies the conditions above.

Input:
2
4 6
472 896

Output:
12
52864
"""
import math
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    ans = math.lcm(a, b)
    print(ans)