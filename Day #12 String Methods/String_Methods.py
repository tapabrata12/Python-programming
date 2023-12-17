# String Methods

# Python provides a set of built-in methods that we can use to alter and modify the strings.

# We will discuss one by one about them

# Strings are immutable

"""
Upper():
The upper() method converts a string to an upper case.

Example:
"""
str1 = "RDfvgh"
print(str1)
print(str1.upper())  # A copy of str1 generated and converted to uppercase as strings are immutable

"""
lower()
The lower() method converts a string to lower case.

Example:

"""
str2 = "DWFUYHFEF"
print(str2)
print(str2.lower())  # A copy of str2 generated and converted to lowercase as strings are immutable

"""
strip() :
The strip() method removes any white spaces before and after the string.

Example:
"""

str3 = " Silver Spoon "
print(str3)
print(str3.strip())  # removes any space before and after the string.

"""
rstrip() :
the rstrip() removes any trailing characters.

Example:
"""
str4 = "Tapabrata!!!!!!!!"
print(str4)
print(str4.rstrip("!"))

"""
replace() :
The replace() method replaces all occurrences of a string with another string. 

Example:
"""

str5 = """  
Tapabrata is very good boy. 
Tapabrata goes to school every day.  
Tapabrata respects every teacher.
Tapabrata is very weak in study.
"""

print(str5)
print(str5.replace("Tapabrata", "John"))  # Replaces all the Tapabrata ==> John

"""
split() :
The split() method splits the given string at the specified instance and returns the separated strings as list items.
We will what a list is in later.
Example:

"""
str6 = "My name is Tapabrata"
print(str6)
print(str6.split(" "))

"""
capitalize() :
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

Example:

"""

str7 = "hello"
print(str7)
print(str7.capitalize())

"""

center() :
The center() method aligns the string to the center as per the parameters given by the user.

Example:

"""

str8 = "I am a boy"
print(str8)
print(str8.center(25))  # 25 refers how many spaces I want before a string
print(str8.center(25, "-"))

"""

count() :
The count() method returns the number of times the given value has occurred within the given string.

Example:

"""

str9 = "sdfuhgbefygftywdaefJBFENwefjnffjn"
print(str9.count("f")) # Count the number

"""
endswith() :
The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

Example :

"""
str10 = "Welcome to the Console !!!"
print(str10.endswith("com", 3, 6))
print(str10.endswith("om", 3, 6))
print(str10.endswith("m", 3, 6))


"""
find() : The find() method searches for the first occurrence of the given value and returns the index where it is 
present. If given value is absent from the string then return -1.

Example:

"""

str11 = "I am a boy and my name is Tapabrata"
print(str11.find("is"))  # The First occurrence is index = 23
print(str11.find("ishh"))  # NO occurrence returns -1

"""
Very similar to find()

index() :
The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

Example:

"""
str12 = "I am a boy and my name is Tapabrata"
# print(str12.index("ishh"))

"""
isalnum() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

Example 1:

"""
str13 = "Welcome00ToTheConsole"
print(str13.isalnum())

"""
isalpha() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

Example :

"""

str14 = "Welcome00ToTheConsole"
print(str14.isalpha())

"""
islower() :
The islower() method returns True if all the characters in the string are lower case, else it returns False.

Example:
"""

str15 = "hello world"
print(str15.islower())

"""
isprintable() :
The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

Example :

"""
str16 = "I am a boy"
print(str16.isprintable())

"""
isspace() :
The isspace() method returns True only and only if the string contains white spaces, else returns False.

Example:

"""

str17 = "   "

print(str17.isspace())

"""
istitle() :
The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

Example:

"""
str18 = "I Am A Boy"

print(str18.istitle())

str18_1 = "To kill a Mocking bird"
print(str18_1.istitle())

"""
isupper() :
The isupper() method returns True if all the characters in the string are upper case, else it returns False.
"""
str19 = "I AM A BOY"

print(str19.isupper())

"""
startswith() :
The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

Example :
"""
str20 = "I am a boy"
print(str20.startswith("I am"))

"""
swapcase() :
The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

Example:
"""
str21 = "Tapabrata"

print(str21.swapcase())

"""
title() :
The title() method capitalizes each letter of the word within the string.

Example:
"""
str22 = "i am VEry GoOd bOy"

print(str22.title())