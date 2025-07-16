import turtle

window = turtle.Screen()
snake = turtle.Turtle()

for _ in range(4):
    snake.forward(100)
    snake.right(90)

window.exitonclick()