lnt = int(raw_input('enter-the-lenght-of-the-floor-in-square-feet.:'))
wth = int(raw_input('enter-the-with-of-the-floor-in-square-feet.:'))
price = int(raw_input("enter-the-price-of-a-square-foot-of-tiling-without-the-dollar-sign:"))
a = str(lnt * wth * price)
print "the floor costs " + a + " dollars"