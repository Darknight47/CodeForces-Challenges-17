"""
----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2107/A -------------------------------------------

You have an array a of size n — a1,a2,…an.

You need to divide the n elements into 2 sequences B and C, satisfying the following conditions:

Each element belongs to exactly one sequence.
Both sequences B and C contain at least one element.
gcd (B1,B2,…,B|B|)≠gcd(C1,C2,…,C|C|) ∗
∗gcd(x,y) denotes the greatest common divisor (GCD) of integers x and y.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains an integer n (2 ≤ n ≤ 100).

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^4).

Output
For each test case, first output Yes if a solution exists or No if no solution exists. 
You may print each character in either case, for example YES and yEs will also be accepted.

Only when there is a solution, output n integers on the second line. The i-th number should be either 1 or 2. 
1 represents that the element belongs to sequence B and 2 represents that the element belongs to sequence C.

You should guarantee that 1 and 2 both appear at least once.

Input:
3
4
1 20 51 9
4
5 5 5 5
3
1 2 2

Output:
Yes
2 2 1 1
No
Yes
1 2 2
"""
cases = int(input())
for _ in range(cases):
    sze = int(input())
    arr = list(map(int, input().split()))
    tempSet = set(arr)
    if(len(tempSet) == 1):
        print("NO")
    else:
        print("YES")
        temp = max(arr)
        seen = False
        for num in arr:
            if(not seen and temp == num):
                seen = True
                print("2", end=" ")
            else:
                print("1", end=" ")
        print()