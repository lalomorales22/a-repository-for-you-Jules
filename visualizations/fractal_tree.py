import turtle
import random

def draw_tree(branch_len, t):
    """
    Recursively draws a fractal tree.
    """
    if branch_len > 5:
        # Set the color of the branch based on its length
        if branch_len < 20:
            t.color("green")
        else:
            t.color("brown")

        t.forward(branch_len)
        right_angle = random.randint(15, 30)
        right_len = random.randint(5, 15)
        t.right(right_angle)
        draw_tree(branch_len - right_len, t)
        left_angle = random.randint(30, 60)
        left_len = random.randint(5, 15)
        t.left(left_angle)
        draw_tree(branch_len - left_len, t)
        t.right(left_angle - right_angle) # Return to original angle
        t.backward(branch_len)
        t.color("brown") # Reset color to brown for the trunk

def main():
    """
    Sets up the turtle environment and starts drawing the tree.
    """
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)  # Set the speed to the fastest
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")

    draw_tree(100, t)

    # Hide the turtle and display the window until it's closed
    t.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()
