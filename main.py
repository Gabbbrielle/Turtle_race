def main():

    from tkinter import messagebox
    import turtle
    from turtle import Turtle, Screen
    import random
    from coolname import generate_slug
    turtle.colormode(255)
    screen = Screen()
    screen.title("Let's race! ")
    screen.bgcolor('lavenderblush')
    screen.setup(width=.75, height=0.75, startx=None, starty=None)

    def create(num):
        colors = [(255, 51, 192), (223, 45, 168), (191, 38, 144), (159, 32, 120), (128, 26, 96), (96, 19, 72),
                  (64, 13, 48), (32, 6, 24), (156, 208, 216), (154, 213, 175), (241, 171, 151), (229, 212, 16),
                  (125, 115, 160)]
        x = -450
        y = -150
        players = []
        for turtles in range(num):
            name = Turtle()
            name.name = generate_slug(2)
            name.shape('turtle')
            name.penup()
            name.color(random.choice(colors))
            name.setx(x)
            name.sety(y)
            name.write(f'  {name.name}\n', True, align="right")
            name.pendown()
            name.pensize(2)
            y += 50
            players.append(name)
        return players

    def finish_line():
        line_dude = Turtle()
        line_dude.hideturtle()
        line_dude.shape('turtle')
        line_dude.color((241, 13, 77))
        line_dude.penup()
        line_dude.setheading(90)
        line_dude.speed(0)
        line_dude.setpos(400, -200)
        line_dude.showturtle()
        line_dude.pendown()
        line_dude.speed(1)
        line_dude.forward(50 * num + 50)
        line_dude.hideturtle()

    num = int(screen.numinput("Number of Players", "How many players in the race?:", 3, minval=0, maxval=10))

    players = create(num)
    finish_line()
    finish = 400
    messagebox.askquestion(title="Let's play!", message="ready to play?")
    if 'yes':
        game_on = True
        while game_on:
            for turtl in players:
                if turtl.xcor() >= finish-1:
                    game_on = False
                    messagebox.askokcancel('winner', f'{turtl.name} won! yes!')
                    print(f'{turtl.name}')
                    break
                else:
                    rand_distance = random.randint(1, 10)
                    turtl.forward(rand_distance)

    if messagebox.askyesno(title="again?", message="Want to play again?"):
        turtle.clearscreen()
        main()
    else:
        turtle.clearscreen()


    screen.listen()
    screen.exitonclick()


main()
