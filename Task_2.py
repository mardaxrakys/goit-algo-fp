import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    # Малюємо квадрат
    for _ in range(4):
        t.forward(length)
        t.left(90)

    # Зберігаємо поточну позицію та напрямок
    pos = t.pos()
    angle = t.heading()

    # Розрахунок довжин сторін нових квадратів
    length_new = length * math.sqrt(2) / 2

    # Малюємо ліву гілку
    t.left(45)
    t.forward(length_new)
    draw_pythagoras_tree(t, length_new, level - 1)

    # Повертаємося до позиції батьківського квадрата
    t.setpos(pos)
    t.setheading(angle)

    # Малюємо праву гілку
    t.forward(length)
    t.right(45)
    t.forward(length_new)
    draw_pythagoras_tree(t, length_new, level - 1)

    # Повертаємося до початкової позиції та напрямку
    t.setpos(pos)
    t.setheading(angle)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed("fastest")

    # Вводимо рівень рекурсії
    level = int(input("Введіть рівень рекурсії (рекомендується від 1 до 10): "))

    # Встановлюємо початкову позицію
    t.penup()
    t.goto(-150, -200)
    t.pendown()

    # Малюємо фрактал
    draw_pythagoras_tree(t, 100, level)

    # Завершуємо роботу Turtle
    turtle.done()

if __name__ == "__main__":
    main()
