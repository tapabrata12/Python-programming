# Declaring String

a = " "  # Anything write here, consider as string

name = "Tapabrata"

print("Hello" + name)  # For string + operator acts as Concatenate operator

friend = 'Rohan'  # String can be declared in single quarts

# Creating multiline String
#
# line = "Hello
# How are
# You"     # This will give error

line = '''
Hey 
How are 
You
'''

print(line)  # This is the way to write multiline string

'''
String Indexing :
String is a sequence of character, Indexing starts with zero 

'''

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
# print(name[9])  # This will give index error, or It will print nothing

# Let's use a for loop to do this work we will learn about it later So doesn't worry

for character in line:
    print(character)
