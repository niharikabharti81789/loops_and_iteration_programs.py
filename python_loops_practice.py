
# WHILE LOOP BASICS
# ========================

count = 1
while count <= 14:
    print(count)
    count += 1


i = 1
while i <= 14:
    print("niharika", i)
    i += 1


i = 1
while i <= 26:
    print(i)
    i += 1

print("loop ended")


# Reverse counting
i = 24
while i >= 1:
    print(i)
    i -= 1

print("loop ended")


# ========================
# PRACTICE QUESTIONS (WHILE)
# ========================

# 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

print("loop ended")


# 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

print("loop ended")


# Multiplication table
n = int(input("Enter the table of: "))

i = 1
while i <= 10:
    print(n * i)
    i += 1


# ========================
# LIST TRAVERSAL
# ========================

nums = [12, 22, 44, 8, 54, 32, 567, 67, 43, 221, 654, 65]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1


# SEARCH IN TUPLE (FIXED LOGIC)
nums = (12, 22, 44, 8, 54, 32, 567, 67, 43, 221, 654, 65)
x = 43

i = 0
found = False

while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
        found = True
        break
    i += 1

if not found:
    print("Not found")


# BREAK EXAMPLE
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

print("end of loop")


# CONTINUE EXAMPLE
i = 0
while i <= 8:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


# ========================
# FOR LOOP BASICS
# ========================

veges = ("peas", "carrot", "radish", "lokey")

for val in veges:
    print(val)

print("end")


# SEARCH USING FOR LOOP
nums = (2, 3, 2, 13, 5, 43, 21, 43, 21, 76, 54, 43)
x = 21
idx = 0

for el in nums:
    if el == x:
        print("Number found at index", idx)
    idx += 1


# RANGE EXAMPLES
print(range(5))

for i in range(5):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(1, 101, 2):
    print(i)


# ========================
# PRACTICE QUESTIONS (FOR LOOP)
# ========================

# 0 to 100
for i in range(101):
    print(i)


# 100 to 1
for i in range(100, 0, -1):
    print(i)


# Multiplication table
n = int(input("Enter the number: "))

for i in range(1, 11):
    print(n * i)


# Sum of numbers (FOR)
n = 8
sum = 0

for i in range(1, n + 1):
    sum += i

print("Total sum =", sum)


# Sum of numbers (WHILE)
n = 8
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("Total sum =", sum)


# Factorial
n = 3
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
