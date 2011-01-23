number1 = Pattern("../Images/numbers/trade/confirm/number_04.png").similar(0.9)
match1 = exists(number1)
if match1:
	hover(match1.getTarget())