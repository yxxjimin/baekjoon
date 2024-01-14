from functools import reduce

# [['55'], ['50', '40']]
terms_to_reduce = [s.split('+') for s in input().split('-')]

# [55, 90]
reduced_terms = [sum([int(x) for x in term]) for term in terms_to_reduce]

# -35
result = reduce(lambda x, y: x - y, reduced_terms)

print(result)
