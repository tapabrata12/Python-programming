apple_prize = int(input("Enter apple prize: "))
budget = 200

if budget - apple_prize >= 80:
    print("Definitely buy it")

elif budget - apple_prize >= 50:
    print("You can proceed")
else:
    print("Don't buy it")

