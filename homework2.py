temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 0:
    print("Slip on another layer, it's freezing!")
elif temperature < 10:
    print("It's quite cold, keep your jacket and pull over on!")
elif temperature < 20:
    print("It's a bit chilly, take your jacket off, but keep your pull over on!")
elif temperature < 30:
    print("It's warm, take your jacket and pull over off!")
else:
    print("You should only be in a t-shirt and shorts, it's boiling hot!")