import random
from tkinter import *

window = Tk()
window.geometry("500x400")
window.title("Rock Paper Scissors Game")

msg1=Label(window, text='WELCOME!')
msg1.config(font=('Times New Roman', 15))
msg1.grid(column=0, row=0)
msg2=Label(window, text='Click on your desired option below:-')
msg2.config(font=('calibri', 12))
msg2.grid(column=0, row=1)

USER_SCORE = 0
COMP_SCORE = 0

def random_computer_choice():
        return random.choice(['Rock','Paper','Scissor'])

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'Rock'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'Paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'Scissor'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

def result(human_choice,comp_choice):
        global USER_SCORE
        global COMP_SCORE
        user=USER_CHOICE
        computer=COMP_CHOICE
        if user == computer:
            print('Draw')
            winner='Draw'
        if user == 'Rock':
            if computer == 'Paper':
                print('Computer wins')
                COMP_SCORE+=1
                winner='Computer'
            elif computer == 'Scissor':
                print("User Wins")
                USER_SCORE+=1
                winner='User'
        if user ==  'Paper':
            if computer == 'Scissor':
                print('Computer wins')
                COMP_SCORE += 1
                winner = 'Computer'
            elif computer == 'Rock':
                print('User wins')
                USER_SCORE += 1
                winner = 'User'
        if user == 'Scissor':
            if computer == 'Rock':
                print('Computer wins')
                winner = 'Computer'
                COMP_SCORE += 1
            elif computer == 'Paper':
                print('User wins')
                USER_SCORE += 1
                winner = 'User'
        text_area = Text(master=window,height=12,width=30)
        text_area.grid(column=0,row=5)
        answer = "User Choice: {uc} \nComputer's Choice : {cc} \n Winner : {w} \n User Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,
                                                                                                                                    cc=COMP_CHOICE,
                                                                                                                                    u=USER_SCORE,
                                                                                                                                    c=COMP_SCORE, w=winner)
        text_area.insert(END,answer)


button1 = Button(text="       Rock       ",bg="turquoise",command=rock)
button1.grid(column=0,row=2)
button2 = Button(text="       Paper      ",bg="pink",command=paper)
button2.grid(column=0,row=3)
button3 = Button(text="      Scissor     ",bg="yellow",command=scissor)
button3.grid(column=0,row=4)

window.mainloop()

