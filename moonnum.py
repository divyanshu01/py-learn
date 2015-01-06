#planet = ""
planet = str(raw_input('please type a planet  can give you the moon count:'))
#print planet

if planet == "mercury":
    print " The number of moons for " + planet + " is 0"
elif planet == "venus":
    print " The number of moons for " + planet + " is 0"
elif planet == "earth":
    print " The number of moons for " + planet + " is 1"
elif planet == "mars":
    print " The number of moons for " + planet + " is 2"
elif planet == "jupiter":
    print " The number of moons for " + planet + " is 67"
elif planet == "saturn":
    print " The number of moons for " + planet + " is 62"
elif planet == "uranus":
    print " The number of moons for " + planet + " is 27"
elif planet == "neptune":
    print " The number of moons for " + planet + " is 14"
elif planet == "pluto":
    print " The number of moons for " + planet + " is 5"
else:
    print "we are still working on the program"
    print "your planet has not been added to our list. "
    print "see you in 1 quadrillion million years"