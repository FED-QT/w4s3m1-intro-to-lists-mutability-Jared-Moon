# exercise.py
# Part 1: Mutable vs Immutable
a = 100
b = a
print("Before:", a, b, id(a), id(b))

a += 1
print("After a += 1:", a, b, id(a), id(b))
#A will incease in value and change memory address, B will still contain the original A Memory Address 
x = [1, 2, 3]
y = x
print("Before:", x, y, id(x), id(y))

x.append(4)
print("After x.append(4):", x, y, id(x), id(y))
#Changes will be made but the Memory address wont change

# ===

# Part 2: Lists & Loops
names = ["alice", "bob", "charlie", "dana"]

# Task A: build upper_names
upper_names = []
for n in names:
    # TODO: append uppercase n
    upper_names.append(n.capitalize())

# Task B: enumerate over upper_names
for i, name in enumerate(upper_names):
    # TODO: print index and name
    print(f"Index: {i}, {name}")

# Task C: demo two list methods
# 1. insert
upper_names.insert(2,"Betty")
print(upper_names)
# 2. remove
upper_names.remove("Betty")
print(upper_names)
# 3. sort
upper_names.sort(key=None, reverse=True)
print(upper_names)