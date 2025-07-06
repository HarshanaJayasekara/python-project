print("hello world")
print("*" * 10)
a = 5 + 3
b = 4

print(a) 


Course = "python programming"
is_real = True
count = 4.9

msg = """
Hi macha
this is i am
"""

print(msg)

print(len(Course))
print(Course[0])
print(Course[-1])
print(Course[0:3])
print(Course[0:])
print(Course[:])

name = "i am \"harry"
#\"     i am "harry
#\'     i am 'harry
#\\     i am \harry
#\n     i am -BREAK THE LINE- harry
print(name)

first = "jady"
full = f"{name} {first} {2025-1997}"
print(full)

#function call
print(Course.upper())
print(Course.splitlines())
print(Course.replace("p", "X"))
print("pro" in Course)
print("lython" not in Course)

print(4+4)
print(4-2)
print(4/2)
print(4*2)
print(4 // 2)
print(4 % 2)
print(4 ** 2)

x = 10
x += 5
print(x)

print(round(2.9))
print(abs(-2.9))

import math
y = 4.3
x = 5.5
print(math.ceil(y))
# Google search Python mathamatical function
print(math.floor(x))
print(math.fmod(x, y))
print(math.modf(x))
print(math.remainder(x, y))

# n1 = input("x : ")
# n = float(n1) + 50
# print(n)

print(bool("False"))
print(bool(""))

print(10>5)
print(10<5)
print(10>=5)


temp = 35
if temp > 30 :
    print("It's warn")
elif temp > 45 :
    print("It's hot")
else:
    print("It's cold")
print("Done 2")

age = 22
if age > 18 :
    msg = "Eligible"
else:
    msg = "not Eligible"
print(msg)

msg = "Eligible" if age >= 18 else "not Eligible"
print(msg)

#Operator and, or, not


for num in range(3) :
    print("Attempt")

for num in range(5):
    print((num+1) * "*")

successful = True
for num in range(3):
    print("Attempt")
    if successful:
        print("Succesful")
        break
else :
    print("Attempt 3")


for x in range(5):
    for y in range(3):
        for z in range(2):
            print(f"({x}, {y}, {z})")

#function
print(type(5))
print(type(range(5)))

#Iterable
for x in "Py":
    print(x)

for x in [1,2,3,4]:
    print(x)

number = 100
while number > 0:
    print(number)
    number //= 2


def nsbm():
    print("hi there")

nsbm()


def name(fname, lname):
    print(f"hi {fname} {lname}")

name("harry", "jady")


def greet(name):
    return f"hi {name}"

massage = greet("kamal")
print(massage)


def enter(num, by):
    return num + by

print(enter(5,18))

def multy(*nums):
    totle = 1
    for num in nums:
        totle *= num
    return totle

print(multy(2,4,6,7))