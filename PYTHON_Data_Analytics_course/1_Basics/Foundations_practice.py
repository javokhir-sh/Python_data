# ---- Variables, Strings, Numbers ----

# 1. Create variables for your name, age, and height. Print them using an f-string in one sentence.
# 2. Given name = "javohir", print it in uppercase, then print just the first 4 letters.
# 3. Ask: what's the output of "5" + "5" vs 5 + 5 vs int("5") + 5?
# 4. Round 7.6789 to 2 decimal places using a built-in function.

print("5" + "5")  # 55
print(type("5" + "5"))  # str
print(int("5") + 5)   # 10

x = 7.6789
print(round(x, 2))  # 7.68  decimal places = 2nd value

# ---- Comparison & Conditional Statements ----

# 5. Write a program that takes a number and prints "positive", "negative", or "zero".

number = 10
if number > 0:
    print('positive')
elif number < 0:
    print('negative')
else:
    print('zero')


# 6. Write a ternary expression that prints "even" or "odd" for a given number.

number = 8

if number % 2 == 0:
    print('even')
else:
    print('odd')

# -- same

number = 8
result = 'even' if number % 2 == 0 else 'odd'
print(result)

# 7. Given age = 25 and has_id = True, use a logical operator to check if someone can enter a club (must be 18+ AND have ID).

age = 25
has_id = True

if age >= 18 and has_id:
    print('u welcome man')
else:
    print('get the fuck outa here')


# 8. Explain what 1 < x < 10 does and rewrite it without chaining.

1 < x and x < 10


# Loops
# 9. Print numbers 1 to 20, but skip multiples of 3.

for _ in range(1, 21):
    if _ % 3 != 0:
        print(_)


# 10. Use for...else to check if a number is prime (loop through possible divisors; if none divide it, print "prime" in the else).
# prime number = tub son

# starting from 2 (cuz of division 1, and ending value is exclusive = number -1)
number = 13
for divisor in range(2, number):
    if number % divisor == 0:
        print('NotPrime')
        break
    else:
        print('prime')

# 11. Write nested loops to print a 5x5 grid of stars (*).

for row in range(5):
    for col in range(5):
        print('*', end=" ")
    print()


# 12. Write a while loop that keeps asking the user for a password until they type "correct".

password = 'correct'
x = input('Enter password:  ')

while x != password:
    x = input('Wrong, try again: ')

print('here u go')  # no need for else, while loop passes to next line auto


# ----  Functions  ----

# 13. Write a function calculate_area(length, width) that returns the area of a rectangle.

def area(length, width):
    return length * width


print(area(8, 10))


# 14. Write a function greet(name, greeting="Hello") using a default argument, then call it two ways (with and without specifying greeting).

def greet(name, greeting='Hello'):
    print(f'{greeting} {name}!')


greet('john')
greet('john', 'hallo')


# 15. Write a function that accepts *args and returns their sum.


def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3))

# ------ = ---------


def sum_all(*args):
    total = 0
    for number in args:
        total += number
    return total


print(sum_all(1, 2, 3))
