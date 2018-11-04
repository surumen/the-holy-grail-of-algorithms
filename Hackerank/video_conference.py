"""
Bob is making a video conference software. Wherever a new person joins the
conference, Bob displays the person's name in the interface.
However, displaying full name is tedios and takes much space. So he decided
to display the shortest prefix which doesn't match any prefix of any person
who has joined earlier.
You are given the list of the persons who have joined the call in chronological
order. Your task is to figure out how the final list looks like.

Solution
string name = sam
vector<string> ans = {m, s, sa, samu, sam 2, mi}
unordered_set<string> s = {m, ma, mar, mary, s, st, sta, stac, stacy, sa, sam,
                            samu, samue, samuel}
"""""
from collections import defaultdict

def videoConference(names):
    s = set()
    d = defaultdict(int)
    l = list()
    for name in names:
        if name in d:
            d[name] += 1
            l.append(name+" "+str(d[name]))
        else:
            d[name] = 1
            t = ""
            inserted = False
            for i in range(len(names)):
                t += name[i:i+1]
                if t not in s and not inserted:
                    inserted = True
                    l.append(t)
                s.add(t)
            if not inserted:
                l.append(name)
    return l
