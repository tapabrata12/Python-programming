"""
The for Loop for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is
nothing but iterating over strings, lists, tuples, sets and dictionaries.

Example: iterating over a string:
"""
name = "Tapabrata"

for i in name:
    print(i, end=" ")

print(end="\n")

"""
Now for list how does it work
Example: iterating over a list:
"""

lst = ["Red", "Green", "Yellow"]

for colour in lst:
    print(colour)
    # If we want to iterate each item in a list
    for i in colour:
        print(i)

"""
range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

Example:
"""
print(end="\n")
for x in range(5):  # This will zero to 4
    print(x)

"""
Here, we can see that the loop starts from 0 by default and increments at each iteration.

But we can also loop over a specific range.

Example:
"""
print(end="\n")

for k in range(4, 9):  # The upper will actually goes to n-1 Here --> 9-1 = 8 so prints --> 4 5 6 7 8
    print(k)

"""
 third parameter of range (ie range(x, y, z)) is, how many difference between previous and next number
"""

print(end="\n")

for a in range(2, 21, 2):
    print(a)
