position = "right"
direction = "left"

for n in range(1, 20, 1):
    if position == "right":
        print("right")
        direction = "left"
        position = "center"

    elif position == "center":
        print("center")
        if direction == "left":
            position = "left"
        elif direction == "right":
            position = "right"
    elif position == "left":
        print("left")
        position = "center"
        direction = "right"
