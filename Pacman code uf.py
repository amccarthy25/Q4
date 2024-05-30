"""
Exercises:
1. Change the board.
2. Change the number of ghosts.
3. Change where pacman starts.
4. Make the ghosts faster/slower.
5. Make the ghosts smarter.
"""

from random import choice
from turtle import *
from turtle import Screen
from tkinter import *
from freegames import floor, vector
import pygame

"""

Where in the code is the pacman reprsented? 
Where do we move pacman? 
What are the mechanics of moving pacman? How could we move him differently? 
How do we move pacman back to the starting position? 

How do the ghosts move? 
How can we move them back to starting positions? 

How can we put the food back? 

"""


state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
# fmt: off
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on


def text():     
    pygame.init()
    # win = pygame.display.set_mode((500, 500))

    win = pygame.display.set_mode((500, 500))
    # pygame.display.set_caption("Scrolling Text")

     
    Font = pygame.font.SysFont('timesnewroman',  30)
     
    white=(255, 255, 255)
    yellow=(255, 255, 0)
    green=(0, 255, 255)
    orange=(255, 100, 0)
    done=False
     
    letter1=Font.render("P", False, yellow, white)
    letter2=Font.render("A", False, yellow, white)
    letter3=Font.render("C", False, yellow, white)
    letter4=Font.render("M", False, yellow, white)
    letter5=Font.render("A", False, yellow, white)
    letter6=Font.render("N", False, yellow, white)
    # letter7=Font.render("H", False, orange, yellow)
     
    i=0
    c=1
     
    while not done:
        if(i>=820):
            i=0
            c+=1
            pygame.time.wait(500)
             
        win.fill(white)
        # if(c%6==0):    
        #     # Scrolling the text in diagonal on right side of the Screen.copying the text surface object to the display surface object at the center coordinate. 
        #     win.blit(letter1, (662-i, -162+i))
        #     win.blit(letter2, (639-i, -139+i))
        #     win.blit(letter3, (608-i, -108+i))
        #     win.blit(letter4, (579-i, -79+i))
        #     win.blit(letter5, (552-i, -52+i))
        #     win.blit(letter6, (529-i, -29+i))
        #     # win.blit(letter7, (500 -i, 0 + i))
            
        # if(c%6==5): 
        #     # Scrolling the text in diagonal on left side of the Screen.
        #     win.blit(letter1, (-162+i, -162+i)) 
        #     win.blit(letter2, (-135+i, -135+i))
        #     win.blit(letter3, (-110+i, -110+i))
        #     win.blit(letter4, (-79+i, -79+i))
        #     win.blit(letter5, (-52+i, -52+i))
        #     win.blit(letter6, (-27+i, -27+i))
        #     # win.blit(letter7, (0+i, 0+i))
             
        # if(c%6==4): 
           
        #     # Scrolling the text in right side of the Screen.
        #     win.blit(letter1, (480, -180+i))
        #     win.blit(letter2, (480, -150+i))
        #     win.blit(letter3, (480, -120+i))
        #     win.blit(letter4, (480, -90+i))
        #     win.blit(letter5, (480, -60+i))
        #     win.blit(letter6, (480, -30+i))
        #     # win.blit(letter7, (480, 0+i))
             
        # if(c%6==3):  
        #     # Scrolling the text in left side of the Screen.
        #     win.blit(letter1, (0, -180+i))
        #     win.blit(letter2, (0, -150+i))
        #     win.blit(letter3, (0, -120+i))
        #     win.blit(letter4, (0, -90+i))
        #     win.blit(letter5, (0, -60+i))
        #     win.blit(letter6, (0, -30+i))
        #     # win.blit(letter7, (0, 0+i))
             
        if(c%2==1):
            win.blit(letter1, (-124+i, 0))
            win.blit(letter2, (-102+i, 0))
            win.blit(letter3, (-82+i, 0))
            win.blit(letter4, (-58+i, 0))
            win.blit(letter5, (-40+i, 0))
            win.blit(letter6, (-19+i, 0))
            # win.blit(letter7, (0+i, 0))
             
        # if(c%6==2):
        #     # Scrolling the text in bottom of the Screen.
        #     win.blit(letter1, (-124+i, 470))
        #     win.blit(letter2, (-102+i, 470))
        #     win.blit(letter3, (-82+i, 470))
        #     win.blit(letter4, (-58+i, 470))
        #     win.blit(letter5, (-40+i, 470))
        #     win.blit(letter6, (-19+i, 470))
        #    # win.blit(letter7, (0+i, 470))
             
            
        i += 80
        # Draws the surface object to the screen.
        pygame.display.update()
         
        # iterate over the list of Event objects 
        # that was returned by pygame.event.get() method
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                done=True
        #Delay with 5ms
        pygame.time.wait(250)
    pygame.quit()




def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False
    

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


def world():
    """Draw world using path."""
    bgcolor('black')
    path.color('blue')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')



def move():
    """Move pacman and all ghosts."""
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:

            screen = Screen()
            
            # Write on window 
            color('Yellow')
            write("PACMAN", font=("Verdana", 45, "normal"), align="left", move=False)
          
            #writer.write(state['score'])
            
            #text()
           #screen.setup(width=600, height=400)
            def do_something():
                print("Good bye")
                Screen().bye()
            def restart():
                print("Restart game")
                # play_pacman()
                # screen.onclick(reset)
                # mainloop()
                
                
            # canvas = screen.getcanvas()
            # button = Button(canvas.master, text="HI", command=do_something, bg='light blue', height=2, width=10, font= ('Helvetica 10 bold italic'))
            # button.pack()
            # button.place(x = ((index % 20) * 20 - 200), y = (180 - (index // 20) * 20))
            
            
            canvas = screen.getcanvas()
            button = Button(canvas.master, text="Play Again", command=reset_game, bg='light blue', height=2, width=30, font= ('Helvetica 10 bold italic'))
            button.pack()
            button.place(x=85, y=170)

            # screen.onclick(reset)
            # mainloop()
            
            canvas = screen.getcanvas()
            button = Button(canvas.master, text="Exit Window", command=do_something, bg='light blue', height=2, width=30, font= ('Helvetica 10 bold italic'))
            button.pack()
            button.place(x=85, y=230)
            screen.exitonclick()
            
            
            # screen.onclick(reset_game)
            # mainloop()
            # screen.playpacmanonclick()
            
            return

    # ontimer(move, 100)
    ontimer(move, 75)

def change(x, y):
    """Change pacman aim if valid."""
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y
        
        
# def play_pacman():
#     x = (floor(point.x, 20) + 200) / 20
#     y = (180 - floor(point.y, 20)) / 20
#     index = int(x + y * 20)
#     square((index % 20) * 20 - 200, 180 - (index // 20) * 20)
#     def offset(point):
#         """Return offset of point in tiles."""
#         x = (floor(point.x, 20) + 200) / 20 
#         y = (180 - floor(point.y, 20)) / 20
#         index = int(x + y * 20)
#         return index    
#     def valid(point):
#         """Return True if point is valid in tiles."""
#         index = offset(point)
    
#         if tiles[index] == 0:
#             return False
    
#         index = offset(point + 19)
    
#         if tiles[index] == 0:
#             return False
    
#         return point.x % 20 == 0 or point.y % 20 == 0    
#     world()
#     move()
#     change(aim.x, aim.y)

def reset_game(): 
    writer.undo()
    writer.write(state['score'])

    clear()

    
    
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)
        
    reset()
    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')
    down()
    
    # up()
    # goto(point.x + 10, point.y + 10)
    # dot(20, 'red')
    # down()

    update()
    
    for point, course in ghosts:
        if abs(pacman - point) < 20:

            screen = Screen()
    # pass 



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()

world()
move()
done()
