import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, -size / 2**0.5 / 2)  # Adjust the starting position for symmetry
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)  # Turn right for the next segment

    window.mainloop()

draw_koch_snowflake(3)
