# Foundamentals of Python


import math
print("git")
print('*'*10)
x = 3

# --------------------------------------

course = 'python programming'
print(len(course))
print(course[0])
print(course[0:4])  # ending (4) is exclusive
print(course[0:])
print(course[:4])
print(course[:])
# 0...-1
# ----------------------------------------
# comments

course = "Python programming"

# \'
course = "Python \'programming"
print(course)
# \"
course = "Python \"programming"
print(course)
# \\
course = "Python \\programming"
print(course)
# \n  -- new line
course = "Python \nprogramming"
print(course)

# -- -- -- -- -- -- -- -- -- -- -- -- -- --

first = "John"
last = "Hugo"
full = first + " " + last
print(full)

# ---------------------------------------

course = '   python Programming'

print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.rstrip())
print(course.lstrip())

print(course.find("pro"))  # if not in it = -1
print(course.find("Pro"))  # if in it = position (10)
print(course.replace("p", "k"))
print("pro" in course)      # True/False
print("bit" not in course)  # True/False

# -----------------------------------

#  + - * /
#  //  %
#  **

print(10//3)  # int (3)
print(10 % 3)  # remainder (1)
print(10**3)  # to the level of (10^3 = 1000)

# ------------------------------------

x = 10
x = x+3
# -------- =
x += 3
x -= 2
x *= 6
print(x)

# --------------------------
print(round(2.4))  # regular yaxlit (2)
print(round(4.6))  # (5)
print(abs(-2.8))  # module (2.8)
print(math.ceil(2.2))  # yaxlit to top (3)

#  --------------------------------------------

x = input("x:")
y = int(x)+1
print(f"x: {x}, y: {y}")
# f - formatting variables

# int(x)
# float(x)
# bool(x)  - True/False: falsy values: 0, ""
# str(x)

# list
# dictionary
# set
# tuple
