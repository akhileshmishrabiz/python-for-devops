# range(start, stop, step)
# start (optional): The starting value of the sequence. Defaults to 0 if not provided.
# stop (required): The end value of the sequence. The sequence will include numbers up to, but not including, this value.
# step (optional): The difference between each number in the sequence. Defaults to 1 if not provided.

# Example 1: Basic range() with only stop
print("Example 1: Basic range() with only stop")
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Example 2: range() with start and stop
print("\nExample 2: range() with start and stop")
for i in range(2, 7):
    print(i)  # Output: 2, 3, 4, 5, 6

# Example 3: range() with start, stop, and step
print("\nExample 3: range() with start, stop, and step")
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9

# Example 4: range() with negative step
print("\nExample 4: range() with negative step")
for i in range(10, 0, -2):
    print(i)  # Output: 10, 8, 6, 4, 2

# Example 5: range() with all parameters as defaults
print("\nExample 5: range() with all parameters as defaults")
for i in range(0):
    print(i)  # Output: (No output, as range is empty)

# Example 6: Converting range to a list
print("\nExample 6: Converting range to a list")
range_list = list(range(5))
print(range_list)  # Output: [0, 1, 2, 3, 4]
