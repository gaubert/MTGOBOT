check = exists(Pattern("../Images/chat/type_area.png").similar(0.7))
if check:
    match = check.getTarget()
    hover(match)
else:
    print("couldn't find it")