"""
----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1863/A -----------------------------------------

Petya is an administrator of a channel in one of the messengers. A total of n people are subscribed to his channel, and Petya is not considered a subscriber.

Petya has published a new post on the channel. At the moment of the publication, there were a subscribers online. 
We assume that every subscriber always reads all posts in the channel if they are online.

After this, Petya starts monitoring the number of subscribers online. He consecutively receives q notifications of the form "a subscriber went offline" or "a 
subscriber went online". Petya does not know which exact subscriber goes online or offline. It is guaranteed that such a sequence of notifications could have 
indeed been received.

Petya wonders if all of his subscribers have read the new post. Help him by determining one of the following:

it is impossible that all n subscribers have read the post;
it is possible that all n subscribers have read the post;
it is guaranteed that all n subscribers have read the post.
Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains three integers n, a, and q (1 ≤ n ≤ 100, 0 ≤ a ≤ n, 1 ≤ q ≤ 100) — the number of subscribers of the channel, 
the initial number of subscribers online, and the number of notifications.

The second line of each test case contains a string of length q, consisting of characters '+' and '-'. The i-th of 
these characters is '+', if the i-th notification tells that a subscriber goes online, and it is '-' otherwise.

Output
For each test case, output a single line: "YES" if all n subscribers are guaranteed to have read the post, 
"NO" if it is impossible for all n subscribers to have read the post, and "MAYBE" otherwise.

Input:
4
5 5 3
--+
5 2 3
++-
5 4 2
-+
5 0 7
++++-++

Output:
YES
NO
MAYBE
YES
"""
cases = int(input())
for _ in range(cases):
    n, a, q = map(int, input().split())
    subs = input()
    if(n == a):
        print("YES")
    else:
        onlines = subs.count('+')
        if(onlines + a < n):
            print("NO")
        else:
            ok = False
            for sub in subs:
                if(sub == '+'):
                    a += 1
                else:
                    a -= 1
                if(a >= n):
                    ok = True
                    break
            print("YES" if ok else "MAYBE")