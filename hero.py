#STICK HERO GAME

from tkinter import *
import random

PILLER_HEIGHT = 150
MIN_PILLER_WIDTH = 30
MAX_PILLER_WIDTH = 80
MIN_PILLER_X_POS =100
MAX_PILLER_X_POS =310
LEFT_PILLER_WIDTH =30
PILLER_COLOR = "#380024"
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 500
CANVAS_BG = "#d7fa66"
HERO_X=10
HERO_Y=CANVAS_HEIGHT-PILLER_HEIGHT
HERO_HEIGHT=50
HERO_WIDTH =15
HERO_COLOR = "#ba0092"
STICK_WIDTH = 5
STICK_COLOR ="#1c0012"
STICK_INCREASE_RATE =5
SPEED = 30


first_y_pos= CANVAS_HEIGHT-PILLER_HEIGHT
y =first_y_pos
enable_increase = True
vertical_stick = []
hero_list = []
my_score =0
scroll =0


#create display tkinter
root =Tk()
root.title('STICK HERO')
root.resizable(height = False, width = False)
MY_HERO = PhotoImage(file="N2.png")
MY_GAME_BACKGROUND =PhotoImage(file="panopink.png")
DEAD_HERO =PhotoImage(file="dead_hero.png")


#create canvas
canvas = Canvas(root, width=CANVAS_WIDTH,height=CANVAS_HEIGHT,bg=CANVAS_BG)
canvas.pack()

#scroll  background
def scroll_bck():
    global scroll
    if scroll ==-1660:
        scroll =0
    my_bck = canvas.create_image(scroll, 0, image=MY_GAME_BACKGROUND,anchor = NW)
    scroll -=5


#create piller
def create_piller():
    global piller_width,piller_pos,PILLER
    piller_width = random.randint(MIN_PILLER_WIDTH,MAX_PILLER_WIDTH)
    piller_pos = random.randint(MIN_PILLER_X_POS,MAX_PILLER_X_POS)
    PILLER=canvas.create_rectangle(piller_pos, CANVAS_HEIGHT-PILLER_HEIGHT, piller_pos+piller_width, CANVAS_HEIGHT, fill=PILLER_COLOR)


#create initial piller on that the Hero will stand
def create_initial_hero_piller():
    canvas.create_rectangle(0,CANVAS_HEIGHT,LEFT_PILLER_WIDTH,CANVAS_HEIGHT-PILLER_HEIGHT,fill=PILLER_COLOR)


#create Hero
def create_hero():
    global HERO,my_hero
    my_hero = canvas.create_image(3, HERO_Y, image=MY_HERO,anchor=SW)

def dead_hero():
    global DEAD_HERO,stick_length
    dead = canvas.create_image(stick_length, CANVAS_HEIGHT, image=DEAD_HERO, anchor=SW)


#create the stick
def create_stick(y_pos):
    global first_y_pos,enable_increase,stick_length,enable_increase,vertical_stick
    if enable_increase:
        for i in range (STICK_WIDTH):
           vertical_stick.append(canvas.create_line(HERO_X+HERO_WIDTH+i,first_y_pos,HERO_X+HERO_WIDTH+i,y_pos,fill = STICK_COLOR))
        stick_length =  first_y_pos - y_pos


#fall stick makes the stick stop to increase in event up key
def fall_stick(event):
    global enable_increase,vertical_stick
    if len(vertical_stick ) ==0:
        pass
    else:
        enable_increase = False
        tilt_stick()



#tilt the stick
def tilt_stick():
    global falling_stick,stick_length,vertical_stick
    delete_vertical_stick()
    falling_stick = []
    vertical_stick = []
    for j in range(STICK_WIDTH):
        falling_stick.append(canvas.create_line(LEFT_PILLER_WIDTH,HERO_Y-j,LEFT_PILLER_WIDTH+stick_length,HERO_Y-j,fill=STICK_COLOR,tag = "fall_stick"))
    check_stick_piller()


def delete_stick():
    global STICK_WIDTH, falling_stick
    for stick in range(STICK_WIDTH):
        canvas.delete(falling_stick[stick])


def delete_vertical_stick():
    global vertical_stick
    for stick in range(stick_length):
        canvas.delete(vertical_stick[stick])


#check the piller and stick alignment
def check_stick_piller():
    global piller_pos,piller_width,stick_length,enable_increase,falling_stick,y,STICK_COLOR,HERO,HERO_WIDTH,hero_list,my_score,t,scroll

    left =piller_pos-LEFT_PILLER_WIDTH
    right =piller_pos+piller_width-LEFT_PILLER_WIDTH

    if (left<=stick_length<=right):
        for _ in range(stick_length//HERO_WIDTH):
            root.after(300,move_hero)
        my_score += 1
        root.after(700, reset)
    else:
        global button
        canvas.delete(my_hero)
        dead_hero()
        canvas.create_text(CANVAS_WIDTH // 2, 140, text="Game  Over\n  You Died", fill="#7d0051", font=('Helvetica 15 bold'))
        my_score = 0
        scroll = 0
        button = Button(canvas, height=3, width=15, bg="#5e003d",text="Restart Game ",fg ="#ff9cdc",command=destroy_button)
        button.place(x=145,y=200)

def destroy_button():
        global button
        button.destroy()
        reset()


def move_hero():
    global stick_length,HERO_Y,HERO_X,hero_list,my_hero
    canvas.delete(my_hero)
    my_hero = canvas.create_image(HERO_X+stick_length, HERO_Y, image=MY_HERO, anchor=SW)




#RESET ALL PARAMETER
def reset():
    global y,enable_increase,STICK_COLOR,PILLER,falling_stick,count,vertical_stick,button
    y = first_y_pos
    enable_increase = True
    canvas.delete(PILLER)
    delete_stick()
    canvas.delete(my_hero)
    scroll_bck()
    t = canvas.create_text(CANVAS_WIDTH // 2, 40, text="SCORE : {}".format(my_score), fill="#7d0051", font=('Helvetica 15 bold'))
    create_initial_hero_piller()
    create_hero()
    create_piller()


#mouse or keyboard  control
def control(event):
    global y
    y -=STICK_INCREASE_RATE
    create_stick(y)

root.bind("<Up>", control)
root.bind("<Down>",fall_stick)

def main():
        scroll_bck()
        t = canvas.create_text(CANVAS_WIDTH // 2, 40, text="SCORE : {}".format(my_score), fill="#7d0051", font=('Helvetica 15 bold'))
        create_initial_hero_piller()
        create_piller()
        create_hero()


if __name__=='__main__':
         main()

root.mainloop()


