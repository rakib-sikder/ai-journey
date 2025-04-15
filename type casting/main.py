a = 1
b= 2.5
c = "3"

print(a + b) # 3.5
print(a + int(c)) # 4
print(a + float(c)) # 4.0
print(str(a) + c) # 13
print(int(b)) # 2
print(float(a)) # 1.0
print(int(c)) # 3

# if we permanently want to change the type of a variable, we can use the following code:
a = float(a) # a is now a float
print(type(a)) # <class 'float'>
print(a) # 1.0