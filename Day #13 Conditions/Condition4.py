num = int(input("Enter number: "))

if num < 0:
    print("Negative")

elif num > 0:
    if 0 < num <= 10:
        print("Number is between 1-10")
    elif 11 <= num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
