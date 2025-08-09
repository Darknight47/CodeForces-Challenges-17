"""
---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1515/A ----------------------------------------

Phoenix has collected n pieces of gold, and he wants to weigh them together so he can feel rich. The i-th piece of gold has weight wi. 
All weights are distinct. He will put his n pieces of gold on a weight scale, one piece at a time.

The scale has an unusual defect: if the total weight on it is exactly x, it will explode. Can he put all n gold pieces onto the scale in some order, 
without the scale exploding during the process? If so, help him find some possible order.

Formally, rearrange the array w so that for each i (1≤i≤n), ∑j=1iwj≠x.

Input
The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 1000) — the number of test cases.

The first line of each test case contains two integers n and x (1 ≤ n ≤ 100; 1 ≤ x ≤ 10^4) — the number of gold pieces that Phoenix has and the weight to avoid, respectively.

The second line of each test case contains n space-separated integers (1 ≤ w(i) ≤ 100) — the weights of the gold pieces. 
It is guaranteed that the weights are pairwise distinct.

Output
For each test case, if Phoenix cannot place all n pieces without the scale exploding, print NO. Otherwise, print YES followed by the rearranged array w. 
If there are multiple solutions, print any.

Input:
3
3 2
3 2 1
5 3
1 2 3 4 8
1 5
5

Output:
YES
3 2 1
YES
8 1 2 3 4
NO
"""
cases = int(input())
for _ in range(cases):
    sze, x = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse=True)
    prefix_sum = 0
    ok = True
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == x:
            if i + 1 < len(arr):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:
                ok = False
            break
    if(ok):
        prefix_sum = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum == x:
                ok = False
                break
    if(ok):
        print("YES")
        print(*arr)
    else:
        print("NO")