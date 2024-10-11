from itertools import product

# Read input
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute Cartesian product
result = list(product(A, B))

# Print result
for item in result:
    print(item, end=' ')
