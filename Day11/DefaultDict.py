from collections import defaultdict

# Read input values
n, m = map(int, input().split())

# Create a defaultdict to store the indices of words in group A
group_a = defaultdict(list)

# Read words for group A and store their indices
for i in range(1, n + 1):
    word = input().strip()
    group_a[word].append(i)

# Read words for group B and check their occurrences in group A
for _ in range(m):
    word = input().strip()
    if word in group_a:
        print(" ".join(map(str, group_a[word])))
    else:
        print(-1)
