#planet = ""
planet = input('please type a planet  can give you the moon count:')
#print planet

if planet.lower == "mercury":
    print("The number of moons for " + planet + " is 0")
elif planet.lower == "venus":
    print("The number of moons for " + planet + " is 0")
elif planet.lower == "earth":
    print("The number of moons for " + planet + " is 1")
elif planet.lower == "mars":
    print("The number of moons for " + planet + " is 2")
elif planet.lower == "jupiter":
    print("The number of moons for " + planet + " is 67")
elif planet.lower == "saturn":
    print("The number of moons for " + planet + " is 62")
elif planet.lower == "uranus":
    print("The number of moons for " + planet + " is 27")
elif planet.lower == "neptune":
    print("The number of moons for " + planet + " is 14")
elif planet.lower == "pluto":
    print("The number of moons for " + planet + " is 5")
else:
    print("we are still working on the program.")
    print("your planet has not been added to our list.")
    print("see you in 1 quadrillion million years.")
