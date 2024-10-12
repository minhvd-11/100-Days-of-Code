import cmath

# Input complex number
z = complex(input().strip())

# Convert to polar coordinates
r, phi = cmath.polar(z)

# Print the results
print(f"{r:.3f}")
print(f"{phi:.3f}")
