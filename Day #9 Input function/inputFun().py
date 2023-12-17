# Input function takes value from  user
# Default behaviour of input is to take a string

a = input("Enter name: ")

print("My name is", a)

x = input("Enter first number:")
y = input("Enter first number:")

print(x + y)  # This will xy as it takes number as string to resolve this we use typecasting

c = int(input("Enter first number:"))
d = int(input("Enter first number:"))

print(c + d)  # Now it will give x+y
