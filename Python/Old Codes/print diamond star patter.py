diamond = ""

# Iterate through the rows of the diamond pattern
for n in range(1, 11):
    # Create a string of stars and spaces
    row = " " * n + "*" * (2 * n - 1) + " " * n
    
    # Append the row string to the diamond variable
    diamond += row + "\n"

# Print the diamond pattern
print(diamond)
