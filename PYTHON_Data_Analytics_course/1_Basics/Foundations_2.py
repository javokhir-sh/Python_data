#  --  COMPARISON OPERATORS  ----  ###

temp = 0
if temp > 20:
    print("its warm")
elif temp > 30:
    print("hott")
else:
    print("cold")
print("done")

# ----------------------------

age = 22
if age >= 18:
    message = "eligible"
else:
    message = "not eligible"
print(message)

# -------------------- =

message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# --------------------------------------------------------

high_income = True
environment = True

if high_income and environment:
    print("el")
else:
    print("not el")


high_income = True
environment = False
student = False

if (high_income or environment) and not student:
    print("nice")
else:
    print("bad")


if 16 <= age < 24:
    print("mann")


for number in range(4):
    # print("git")
    # print("git", number + 1)
    print("git", number + 1, (number + 1) * ".")


for number in range(1, 5):
    print("algebra", number, number * ".")


for number in range(1, 10, 2):
    print("algebra", number, number * ".")


successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")


#  ------------------------ nested loops

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


print(type(5))    # int
print(type(range(3)))   # range

for x in "python":
    print(x)


for x in [1, 3, 4]:
    print(x)


number = 100
while number > 0:
    print(number)
    number //= 2
# keeps dividing 100 by 2 in int till > 0


# ----------------------------------
count = 0
for number in range(1, 10):
    if number % 2 == 0:  # dividing by 2 without remainder
        count += 1
        print(number)
print(f"we have {count} even numbers")


# ---------------------------------------------

def greet(first_name, last_name):
    print(f"Hey {first_name} {last_name}")
    print("Welcome aboard")


greet("John", "Hugo")
greet("black", "man")


# ---------------------   FUNCTIONS
# 1. Perform a task
# 2. Calculate and return value


def greet(name):
    print(f"hi {name}")


print(greet("john"))


# --------------------------------

def hallo(number, pinokio):
    return number + pinokio


print(hallo(2, 1))

# ----------------------------------


def increment(number, by=1):
    return number + by


print(increment(4))  # since by=1 given -> optional to enter by value
print(increment(4, 2))

# ---------------------------------


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))   # multiplies all
