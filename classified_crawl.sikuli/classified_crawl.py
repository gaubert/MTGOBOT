scroll_direction = WHEEL_DOWN
match = False
hover("1294193250260.png")
start_mouse_loc = Env.getMouseLocation()
scroll_loc = start_mouse_loc.getY() 
while match == False:
    if exists(Pattern("1294198025750.png").similar(1)):
        text = find(Pattern("1294198025750.png").similar(1))
        hover(Location(text.getX(), text.getY()))
        match = True
    else:
        hover("1294193250260.png")
        mouse_loc = Env.getMouseLocation()
        if abs(mouse_loc.getY() - scroll_loc) < 10:
            if scroll_direction == WHEEL_DOWN:
                scroll_direction = WHEEL_UP
            else:
                scroll_direction = WHEEL_DOWN
        wheel("1294193250260.png", WHEEL_DOWN, 3)
        mouse_loc = Env.getMouseLocation()
        scroll_loc = mouse_loc.getY()