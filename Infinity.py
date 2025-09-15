"""
--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/987/A ----------------------------------------

You took a peek on Thanos wearing Infinity Gauntlet. In the Gauntlet there is a place for six Infinity Gems:

the Power Gem of purple color,
the Time Gem of green color,
the Space Gem of blue color,
the Soul Gem of orange color,
the Reality Gem of red color,
the Mind Gem of yellow color.
Using colors of Gems you saw in the Gauntlet determine the names of absent Gems.

Input
In the first line of input there is one integer n (0 ≤ n ≤ 6) — the number of Gems in Infinity Gauntlet.

In next n lines there are colors of Gems you saw. Words used for colors are: purple, green, blue, orange, red, yellow. 
It is guaranteed that all the colors are distinct. All colors are given in lowercase English letters.

Output
In the first line output one integer m (0 ≤ m ≤ 6) — the number of absent Gems.

Then in m lines print the names of absent Gems, each on its own line. Words used for names are: Power, Time, Space, Soul, Reality, Mind. Names can be printed in any order. 
Keep the first letter uppercase, others lowercase.

Input:
4
red
purple
yellow
orange

Output:
2
Space
Time
"""
diction = {
    "purple": "Power",
    'green': 'Time',
    'blue': 'Space',
    'orange': 'Soul',
    'red': 'Reality',
    'yellow': 'Mind'
}

n = int(input())
if(n == 0):
    print(6)
    for value in diction.values():
        print(value)
else:
    tempKeys = []
    for _ in range(n):
        tempKeys.append(input())
    print(6 - n)
    for key in diction.keys():
        if key not in tempKeys:
            print(diction[key])