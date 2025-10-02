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
    original = sorted([a, b])  
    ok = False
    # Try vertical cuts
    for x in range(1, a):
        r1 = [x, b]
        r2 = [a - x, b]
        # side-by-side
        if r1[1] == r2[1]:
            new_rect = sorted([r1[0] + r2[0], r1[1]])
            if new_rect != original:
                ok = True
                break
        # stacked
        if r1[0] == r2[0]:
            new_rect = sorted([r1[0], r1[1] + r2[1]])
            if new_rect != original:
                ok = True
                break
    if(not ok): # Horizontal cut
        for y in range(1, b):
            r1 = [a, y]
            r2 = [a, b - y]
            # side-by-side
            if r1[1] == r2[1]:
                new_rect = sorted([r1[0] + r2[0], r1[1]])
                if new_rect != original:
                    ok = True
                    break
            # stacked
            if r1[0] == r2[0]:
                new_rect = sorted([r1[0], r1[1] + r2[1]])
                if new_rect != original:
                    ok = True
                    break
    print("YES" if ok else "NO")