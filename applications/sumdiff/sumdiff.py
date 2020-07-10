"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
#q = set(range(1, 200))
# q = (3, 4, 6, 15, 17)
q = (1, 3, 4, 7, 12)
pos_lookup_table = dict()
neg_lookup_table = dict()

def f(x):
    return x * 4 + 6

# Your code here
for i in range(len(q) - 1):
    for j in range(i, len(q)):
        pos_lookup_table[(q[i], "+", q[j])] = f(q[i]) + f(q[j])
        pos_lookup_table[(q[j], "+", q[i])] = f(q[j]) + f(q[i])
        neg_lookup_table[(q[i], "-", q[j])] = f(q[i]) - f(q[j])
        neg_lookup_table[(q[j], "-", q[i])] = f(q[j]) - f(q[i])

# print(pos_lookup_table)
# print(neg_lookup_table)
for pos_key, pos_value in pos_lookup_table.items():
    for neg_key, neg_value in neg_lookup_table.items():
        if pos_value == neg_value:
            print(f"f({pos_key[0]}) + f({pos_key[2]}) = f({neg_key[0]}) - f({neg_key[2]})")
