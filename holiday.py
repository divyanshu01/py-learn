print("so your going on a vacation eh?")
print("well you need me")
cav = input("are you going in a coach or first class?\n")
if cav.lower == "coach":
    scav = input("are you going to be in a penthouse or hotel:")
    if scav.lower == "hotel":
        print("your trip is possible and it costs 1000$")
    if scav.lower == "pentous":
        print("your trip is possible and it costs 2000$")

elif cav.lower == "first class":
    scav = input("are you going to be in a penthouse or hotel:")
    if scav.lower == "hotel":
        print("your trip is possible and it costs 2000$")
    if scav.lower == "pentous":
        print("your trip is possible and it costs 3000$")

