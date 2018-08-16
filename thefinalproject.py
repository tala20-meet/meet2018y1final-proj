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

horizontal_walls = [(range(-200,200, 5),-100) ,(range(-200,200, 5),100) , (range(-200,-170),0) ,
                    (range(-160,-120), 50) , (range(-160,-40), -50) , (range(-75, -40), 50) ,
                     (range(-35, 35), 0) , (range(170,200),0) , (range(120, 160), 50) ,
                     (range(40, 160), -50) , (range(40, 75), 50)]
vertical_walls = [(200, range(-100, 100)) , (-200, range(-100, 100)) , (-120, range(-10, 50)) ,
                  (-70, range(-50, 5)) , (0, range(50, 100)) , (0, range(-50, 0, 5)) , (120, range(-10, 50)) ,
                   (70, range(-50, 5))]

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


def check_overlap_horizontal(x,y):
    #pac_man_x = pac_man.pos()[0]
    #pac_man_y = pac_man.pos()[1]
    for horizontal_wall in horizontal_walls:
        if y == horizontal_wall[1]:#y coords are the same
            if x in horizontal_wall[0]:#x in the range of the wall
                return True
    return False

def check_overlap_vertical(x,y):
    #pac_man_x = pac_man.pos()[0]
    #pac_man_y = pac_man.pos()[1]
    for vertical_wall in vertical_walls:
        if x == vertical_wall[0]: #x coords are the same
            if y in vertical_wall[1]: #y in the range of the wall
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
    #if direction==RIGHT and not check_overlap_vertical() :
    if direction==RIGHT: 
        #pac_man.goto(x_pos + SQUARE_SIZE, y_pos)
        #print("You moved right!")
        new_x = x_pos + SQUARE_SIZE
        new_y = y_pos
    #elif direction==LEFT and not check_overlap_vertical():
    elif direction==LEFT:
        #pac_man.goto(x_pos - SQUARE_SIZE, y_pos)
        #print("You moved left!")
        new_x = x_pos - SQUARE_SIZE
        new_y = y_pos
    #elif direction==UP and not check_overlap_horizontal():
    elif direction==UP:
        #pac_man.goto(x_pos,y_pos + SQUARE_SIZE)
        #print("You moved up!")
        new_x = x_pos
        new_y = y_pos + SQUARE_SIZE
        
    #elif direction==DOWN and not check_overlap_horizontal():
    elif direction==DOWN:
        #pac_man.goto(x_pos,y_pos - SQUARE_SIZE)
        #print("You moved down!")
        new_x = x_pos
        new_y = y_pos - SQUARE_SIZE
    else:
        new_x = x_pos
        new_y = y_pos

    if not check_overlap_vertical(new_x,new_y) and not check_overlap_horizontal(new_x,new_y):
        pac_man.goto(new_x,new_y)
    

    #check if about to hit wall
    #move the pacman
    

    #print('hitting wall: ' + str(check_overlap_horizontal()))
    #print('hitting wall: ' + str(check_overlap_vertical()))

    print(pac_man.pos() in all_walls)
    print(pac_man.pos())
    turtle.ontimer(move_pac_man,TIME_STEP)
move_pac_man()

    

turtle.mainloop()

'''changed the if statements and the checking functions, so the pac-man will be
able to move away from the walls, by making the new if statements look at the
coordinates that are infront of the pac-man, and else by making the functions
take arguments'''











