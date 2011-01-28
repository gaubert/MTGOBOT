number = Pattern("../Images/numbers/trade/confirm/number_01.png")

with findAll(number) as matches:
    while matches.hasNext():
        print "found: ", matches.next()