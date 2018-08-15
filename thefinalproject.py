import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(800,500)
turtle.penup()
turtle.pensize("10")
turtle.pencolor("blue")
turtle.bgcolor("black")
turtle.hideturtle()
turtle.goto(-200,-100)
turtle.pendown()
turtle.goto(200,-100)
turtle.goto(200,100)
turtle.goto(-200,100)
turtle.goto(-200,-100)

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.goto(-170,0)

turtle.penup()
turtle.goto(-160,50)
turtle.pendown()
turtle.goto(-120,50)
turtle.goto(-120,-10)

turtle.penup()
turtle.goto(-160,-50)
turtle.pendown()
turtle.goto(-40,-50)
turtle.penup()
turtle.goto(-70,-50)
turtle.pendown()
turtle.goto(-70,5)

turtle.penup()
turtle.goto(-75,50)
turtle.pendown()
turtle.goto(-40,50)

turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.goto(0,100)

turtle.penup()
turtle.goto(-35,0)
turtle.pendown()
turtle.goto(35,0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,-50)




turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.goto(170,0)

turtle.penup()
turtle.goto(160,50)
turtle.pendown()
turtle.goto(120,50)
turtle.goto(120,-10)

turtle.penup()
turtle.goto(160,-50)
turtle.pendown()
turtle.goto(40,-50)
turtle.penup()
turtle.goto(70,-50)
turtle.pendown()
turtle.goto(70,5)

turtle.penup()
turtle.goto(75,50)
turtle.pendown()
turtle.goto(40,50)

horizontal_walls = [(range(-200,200), range(-5, 15)),range(-110, -90) , (range(-200,-170),range(-10, 10)) ,
                    (range(-160,-120), range(40, 60)) , (range(-160,-40), range(-60, 40)) , (range(-75, -40), range(40, 60)) ,
                     (range(-35, 35), range(-10, 10)) , (range(170,200),range(-10, 10)) , (range(120, 160), range(40, 60)) ,
                     (range(40, 160), range(-60, -40)) , (range(40, 75), range(40, 60))]
vertical_walls = [(range(190, 210), range(-100, 100)) , (range(-210, -190), range(-100, 100)) , (range(-130, -150), range(-10, 50)) ,
                  (range(-80, -60), range(-50, 5)) , (range(-10, 10), range(50, 100)) , (range(-10, 10), range(-50, 0, 5)) , (range(110, 130), range(-10, 50)) ,
                   (range(60, 80), range(-50, 5))]

all_walls = horizontal_walls + vertical_walls
turtle.penup()
turtle.goto(0,20)
turtle.pendown()

print(all_walls)

pac_man = turtle.clone()
pac_man.showturtle()
pac_man.shape("circle")
pac_man.color("yellow")
pac_man.penup()






UP_ARROW = "Up" 
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right" 
TIME_STEP = 20
SPACEBAR = "space" 

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3
direction = 5

def up():
    global direction
    direction=UP 
    print("You pressed the up key!")

def down():
    global direction
    direction=DOWN
    print("You pressed the down key!")

def right():
   global direction
   direction=RIGHT
   print("You pressed the right key!")

def left():
   global direction
   direction=LEFT
   print("You pressed the left key!")


turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)


def check_overlap_horizontal():
    pac_man_x = pac_man.pos()[0]
    pac_man_y = pac_man.pos()[1]
    for horizontal_wall in horizontal_walls:
        if pac_man_y == horizontal_wall[1]:#y coords are the same
            if pac_man_x in horizontal_wall[0]:#x in the range of the wall
                return True
    return False

def check_overlap_vertical():
    pac_man_x = pac_man.pos()[0]
    pac_man_y = pac_man.pos()[1]
    for vertical_wall in vertical_walls:
        if pac_man_x == vertical_wall[0]: #x coords are the same
            if pac_man_y in vertical_wall[1]: #y in the range of the wall
                return True
    return False


    '''    
    else :
        print(pac_man.pos())
        move_pac_man()

 '''

turtle.listen()

SQUARE_SIZE = 5

def move_pac_man():
    global all_walls
    my_pos = pac_man.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction==RIGHT :
        pac_man.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        pac_man.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        pac_man.goto(x_pos,y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction==DOWN:
        pac_man.goto(x_pos,y_pos - SQUARE_SIZE)
        print("You moved down!")


    print('hitting wall: ' + str(check_overlap_horizontal()))
    print('hitting wall: ' + str(check_overlap_vertical()))

  
    print(pac_man.pos() in all_walls)
    print(pac_man.pos())
    turtle.ontimer(move_pac_man,TIME_STEP)
move_pac_man()

    

turtle.mainloop()











