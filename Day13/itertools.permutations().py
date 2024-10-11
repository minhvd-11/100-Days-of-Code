from itertools import permutations

# Input
input_string, r = input().split()
r = int(r)

# Generate permutations
perm = permutations(sorted(input_string), r)

# Print permutations
for p in perm:
    print(''.join(p))
