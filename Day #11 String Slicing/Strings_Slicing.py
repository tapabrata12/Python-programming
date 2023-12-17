name = "Tapabrata"
length = len(name)
print(length)

print(name[0:5])
print(name[:5])
print(name[1:5])
print(name[0:])

# Negative Slicing

print(name[0:-3])   # len(name)-3
print(name[-1:-3])  # len(name)-1:len(name)-3 = 8:6 makes no sense
print(name[-4:-3])  # len(name)-4:len(name)-3 = 5:6 makes sense
