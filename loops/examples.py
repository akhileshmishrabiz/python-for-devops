# Looping examples in Python

# 1. Basic For Loop
print("Basic For Loop:")
for i in range(5):
    print(i)

# 2. For Loop with List
print("\nFor Loop with List:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 3. For Loop with Tuple
print("\nFor Loop with Tuple:")
tuple_example = (1, 2, 3, 4)
for num in tuple_example:
    print(num)

# 4. For Loop with Dictionary
print("\nFor Loop with Dictionary:")
student = {"name": "John", "age": 21, "major": "Computer Science"}
for key, value in student.items():
    print(f"{key}: {value}")

# 5. For Loop with String
print("\nFor Loop with String:")
for char in "Hello":
    print(char)

# 6. For Loop with Index
print("\nFor Loop with Index:")
for index, value in enumerate(fruits):
    print(f"Index: {index}, Value: {value}")

# 7. Nested For Loops
print("\nNested For Loops:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()

# 8. While Loop
print("\nWhile Loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# 9. While Loop with Break
print("\nWhile Loop with Break:")
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# 10. While Loop with Continue
# Uses continue to skip the current iteration and move to the next iteration.
print("\nWhile Loop with Continue:")
count = 0
while count < 5:
    count += 1
    if count % 2 == 0:
        continue
    print(count)

# 11. For Loop with Break
# Uses break to exit the loop when a condition is met.
print("\nFor Loop with Break:")
for i in range(10):
    if i == 5:
        break
    print(i)

# 12. For Loop with Continue
print("\nFor Loop with Continue:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 13. For Loop with Else
print("\nFor Loop with Else:")
for i in range(5):
    print(i)
else:
    print("Loop completed successfully")

# 14. While Loop with Else
print("\nWhile Loop with Else:")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed successfully")

# 15. Looping through a Dictionary with Nested Loop
print("\nLooping through a Dictionary with Nested Loop:")
nested_dict = {
    "class1": {"student1": "Alice", "student2": "Bob"},
    "class2": {"student3": "Charlie", "student4": "David"}
}
for class_name, students in nested_dict.items():
    print(f"Class: {class_name}")
    for student_id, student_name in students.items():
        print(f"  {student_id}: {student_name}")
