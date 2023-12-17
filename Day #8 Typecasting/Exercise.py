# Explicit Conversion

string = "10"
number = 5

# print(string+number) giving error

str_to_num = int(string)

print(str_to_num + number)

# Impolite Conversion

a = 1.5
b = 9
c = a + b
print(c)  # Convert automatically to float to prevent data loss

c = a - b
print(c)  # Convert automatically to float to prevent data loss

c = a * b
print(c)  # Convert automatically to float to prevent data loss

c = a / b
print(c)  # Convert automatically to float to prevent data loss

