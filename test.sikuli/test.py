ticket = Pattern("../Images/product/packs/text/Scars.png").similar(0.8)

#scan = Region(466, 251, 159, 13)

match = exists(ticket)

if match:
	print(str(match.x) + ", " + str(match.y)  + ", ")
	hover(match.getTarget())
