from itertools import permutations
a = list(permutations('make'))
print(set([''.join(i) for i in a]))