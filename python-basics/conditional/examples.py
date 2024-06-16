# Conditionals examples in Python

# 1. Basic If Statement
print("Basic If Statement:")
x = 10
if x > 5:
    print("x is greater than 5")

# 2. If-Else Statement
print("\nIf-Else Statement:")
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# 3. If-Elif-Else Statement
print("\nIf-Elif-Else Statement:")
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# 4. Nested If Statement
print("\nNested If Statement:")
x = 10
y = 20
if x > 5:
    print("x is greater than 5")
    if y > 15:
        print("y is greater than 15")

# 5. Using Logical Operators (and, or, not)
print("\nUsing Logical Operators:")
x = 10
y = 5
if x > 5 and y < 10:
    print("x is greater than 5 and y is less than 10")
if x > 15 or y < 10:
    print("x is greater than 15 or y is less than 10")
if not x < 5:
    print("x is not less than 5")

# 6. Conditional Expressions (Ternary Operator)
print("\nConditional Expressions:")
x = 10
result = "x is greater than 5" if x > 5 else "x is less than or equal to 5"
print(result)

# 7. Checking Membership with In
print("\nChecking Membership with In:")
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("banana is in the list")
if "grape" not in fruits:
    print("grape is not in the list")

# 8. Comparing Values
print("\nComparing Values:")
a = 10
b = 20
if a == b:
    print("a is equal to b")
if a != b:
    print("a is not equal to b")
if a < b:
    print("a is less than b")
if a <= b:
    print("a is less than or equal to b")
if a > b:
    print("a is greater than b")
if a >= b:
    print("a is greater than or equal to b")

# 9. Checking Type
print("\nChecking Type:")
value = 10
if isinstance(value, int):
    print("value is an integer")
if isinstance(value, str):
    print("value is a string")

# 10. Conditional with Multiple Conditions
print("\nConditional with Multiple Conditions:")
x = 15
if x > 10:
    print("x is greater than 10")
    if x < 20:
        print("x is also less than 20")
