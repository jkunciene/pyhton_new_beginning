price = 25
print(price > 10 or price < 30)
print(not price > 10)
print(price > 10 and price < 30 )

temperature = 15

if temperature  > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("it's a nice day")
else:
    print("It's a bit cold")


height = input("Koks tavo ugis?")
units = input("Meter(m) or Foot(ft) ?")

if units == "ft":
    converted = float(height) / 3.2808
    print("Yuor height in Meter: " + str(converted))
else:
    converted = float(height) * 3.2808
    print("Yuor height in feets is: " + str(converted))