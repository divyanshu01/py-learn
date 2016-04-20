print("you have arrived at your house in the hoenn region.")
print("when you hear a rucus outside...")
print("you see the pokemon professor being chased by a poochyena!")
print("he says get a pokemon out of his bag and save him.")
print("do you choose,")
print("treeko,the grass pokemon.")
print("torchic,the fire pokemon")
print("or")
print("mudkip,the water pokemon")

nme = input('what is your name:')

a = input('type the name of the pokemon you choose and hit enter\n')

if a.lower() == "treeko":
    print("go treeko")
    print("what move should treeko use")
    print("treeko knows")
    print("absorb")
    b = input(':')
    if b.lower() == "absorb":
        print("treeko used absorb")
        print("the opposing poochyena fainted")
        print("treeko gained 50 exp")
        print("treeko grew to lv 6")
elif a.lower() == "torchic":
    print("go torchic")
    print("what move should torchic use")
    print("torchic knows")
    print("tackle")
    b = input(':')
    if b.lower() == "tackle":
        print("torchic used tackle")
        print("the opposing poochyena fainted")
        print("torchic gained 50 exp")
        print("torchic grew to lv 6")
elif a.lower() == "mudkip":
    print("go mudkip")
    print("what move should mudkip use")
    print("mudkip knows")
    print("barrage")
    b = input(':')
    if b.lower() == "barrage":
        print("mudkip used barrage")
        print("the opposing poochyena fainted")
        print("mudkip gained 50 exp")
        print("mudkip grew to lv 6")
else:
    print("you are a pokemon dummy")
