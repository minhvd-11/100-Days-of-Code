from collections import Counter

# Read input values
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())

# Create a dictionary to count the number of each shoe size
inventory = Counter(shoe_sizes)

total_earnings = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        total_earnings += price
        inventory[size] -= 1

print(total_earnings)
