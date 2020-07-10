"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
# q = (3, 4, 6, 15, 17)
q = (1, 3, 4, 7, 12)

pos_lookup_table = dict()
neg_lookup_table = dict()

def f(x):
    return x * 4 + 6

# Your code here
for i in q:
    for j in q:
        pos = f(i) + f(j)
        neg = f(i) - f(j)

        # ADD
        if pos not in pos_lookup_table:
            pos_lookup_table[pos] = [(i, "+", j)]
        else:
            pos_lookup_table[pos].append((i, "+", j))

        # SUBTRACT
        if neg not in neg_lookup_table:
            neg_lookup_table[neg] = [(i, "-", j)]
        else:
            neg_lookup_table[neg].append((i, "-", j))

for key in pos_lookup_table:
    if key in neg_lookup_table:
        pos_matches = pos_lookup_table[key]
        neg_matches = neg_lookup_table[key]
        for pos in pos_matches:
            for neg in neg_matches:
                print(f"f({pos[0]}) + f({pos[2]}) = f({neg[0]}) - f({neg[2]}) ")
