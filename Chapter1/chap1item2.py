print(" *** Wind classification ***")
speed = float(input("Enter wind speed (km/h) : "))

print("Wind classification is", end=" ")
if speed<=51.99:
    print("Breeze.")
elif 52<=speed<=55.99:
    print("Depression.")
elif 56<=speed<=101.99:
    print("Tropical Storm.")
elif 102<=speed<=208.99:
    print("Typhoon.")
elif speed>=209:
    print("Super Typhoon.")