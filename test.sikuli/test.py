ticket = Pattern("../Images/numbers/trade/number_02.png").similar(1)

match = find(ticket)

if match:
    print("true")