import turtle

def draw_tree(t, branch_length, level, angle):
    if level == 0:
        return

    # Малюємо гілку
    t.forward(branch_length)
    
    # Зберігаємо поточну позицію та напрямок
    pos = t.pos()
    heading = t.heading()

    # Малюємо ліву гілку
    t.left(angle)
    draw_tree(t, branch_length * 0.7, level - 1, angle)

    # Повертаємося до позиції батьківської гілки
    t.setpos(pos)
    t.setheading(heading)

    # Малюємо праву гілку
    t.right(angle)
    draw_tree(t, branch_length * 0.7, level - 1, angle)

    # Повертаємося до початкової позиції та напрямку
    t.setpos(pos)
    t.setheading(heading)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed("fastest")
    t.pencolor("brown")

    # Встановлюємо початкову позицію
    t.penup()
    t.goto(0, -250)
    t.left(90)
    t.pendown()

    # Малюємо дерево
    draw_tree(t, 100, 9, 30)

    # Завершуємо роботу Turtle
    turtle.done()

if __name__ == "__main__":
    main()
