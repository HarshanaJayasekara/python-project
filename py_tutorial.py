
# Python Tutorial

"""
print('Hello, World')
# variable
x = 5
y = "Hello"
a = str(6)
b = int(45)
c = float(4.5)

#Type
print(type(x))

# Multiple variable
x,y,z = "apple", "orange", "banana"
 or 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# output Variable
x = 5
y = 10
z = "John"
print(x + y)
print(x, z)

#Global Variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType

# Random Number
import random
print(random.randrange(1, 10))

a = "Hello, World!"
print(a[1])
print(a[2:5])
print(a[:5])
print(a[2:])
print(a[-5:-2])

# Loopig
for x in "banana":
  print(x)

print(len(a))
print("world" in a)
print("expensive" not in a)

#Modify String 
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))


age = 36
txt = f"My name is John, I am {age}"

#Operators
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	

&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or


#List
mylist = ["apple", "banana", "cherry"]
thislist = list(("apple", "banana", "cherry")) 

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)