"""
-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1928/A ---------------------------------------


Bob has a rectangle of size a×b. He tries to cut this rectangle into two rectangles with integer sides by making a cut parallel to one of the sides of the original rectangle. 
Then Bob tries to form some other rectangle from the two resulting rectangles, and he can rotate and move these two rectangles as he wishes.

Note that if two rectangles differ only by a 90∘ rotation, they are considered the same. For example, the rectangles 6×4 and 4×6 are considered the same.

Thus, from the 2×6 rectangle, another rectangle can be formed, because it can be cut into two 2×3 rectangles, and then these two rectangles can be used to form the 4×3 rectangle, 
which is different from the 2×6 rectangle.

However, from the 2×1 rectangle, another rectangle cannot be formed, because it can only be cut into two rectangles of 1×1, 
and from these, only the 1×2 and 2×1 rectangles can be formed, which are considered the same.

Help Bob determine if he can obtain some other rectangle, or if he is just wasting his time.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. This is followed by the description of the test cases.

The single line of each test case contains two integers a and b (1 ≤ a, b ≤ 10^9) — the size of Bob's rectangle.

Output
For each test case, output "Yes" if Bob can obtain another rectangle from the a×b rectangle. Otherwise, output "No".

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive answers.

Input:
7
1 1
2 1
2 6
3 2
2 2
2 4
6 3

Output:
No
No
Yes
Yes
Yes
Yes
No
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a  # normalize so a ≤ b
    if a % 2 == 0:
        print("Yes")
    elif b % 2 == 0 and b != 2 * a:
        print("Yes")
    else:
        print("No")