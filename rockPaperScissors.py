"""
Rock Paper Scissor

user picks the rock 
for just one round
random picker

"""
from random import randint
import tkinter as tk




choices = {
    0:"ROCK",
    1:"PAPER",
    2:"SCISSORS"
}

def computerPlayer():
    computerRand = randint(0,2)
    computerChoice = choices.get(computerRand)
    return computerChoice

computers_choice = computerPlayer()

def userPlayer(choice) -> str:
    return choice


def isWInner(userChoice, computersChoice, winner = 0) -> int:
    """
    0: COMPUTER
    1: USER
    2: DRAW
    """
    
    if (userChoice=="ROCK" and computersChoice== "PAPER" ):
        winner = 0
    elif (userChoice=="ROCK"   and computersChoice == "SCISSORS"):
        winner = 1
    elif (userChoice=="PAPER"  and computersChoice == "ROCK"):
        winner = 1
    elif (userChoice=="PAPER"  and computersChoice == "SCISSORS"):
        winner = 0
    elif (userChoice=="SCISSORS"  and computersChoice == "ROCK"):
        winner = 0
    elif (userChoice=="SCISSORS" and computersChoice == "PAPER"):
        winner = 1
    else:
        winner = 2
    return winner
# print(isWInner())


def won(isWinner, userChoice, computersChoice):
    match isWInner(userChoice=userChoice, computersChoice=computersChoice):
        case 0:
            return "COMPUTER WON"
        case 1:
            return "USER WON"
        case 2:
            return "DRAW"
     
        
def setRock():
    userPlayer("ROCK")
    user_choice_label["text"] = f"ROCK"
    print(userPlayer("ROCK"))

def setPaper():
    userPlayer("PAPER")
    user_choice_label["text"] = f"PAPER"
    user = "PAPER"
    print(userPlayer("PAPER"))

def setScissors():
    userPlayer("SCISSORS")
    user_choice_label["text"] = f"SCISSORS"
    user = "SCISSORS"
    print(userPlayer("SCISSORS"))

def changeUi():
    computers_choice = computerPlayer()
    won_label["text"] = f"{won(isWinner=isWInner(user_choice_label['text'], computers_choice), userChoice=user_choice_label['text'], computersChoice=computers_choice)}"
    computer_choice_label["text"] = f"                {computers_choice}"
    print(f"                 {computers_choice}")



app = tk.Tk()
app.title("ROCK PAPER SCISSORS")


frame = tk.Frame(
    master=app
)
comp_choice = tk.Label(
    master=frame,
    text="Computer's Choice: "
)
computer_choice_label = tk.Label(
    master=frame,
    text= "XXXX",
    bg="red"
)

frame.grid(row=0, column=0, sticky="N", padx=20)
comp_choice.grid(row=0, column=0)
computer_choice_label.grid(row=0, column=1)

button_frames = tk.Frame(
    master=app
)
computer_choice_button_rock = tk.Button(
    master=button_frames,
    text="Rock",
    command=setRock
    
)
computer_choice_button_paper = tk.Button(
    master=button_frames,
    text="Paper",
    command=setPaper
    
)
computer_choice_button_scissors = tk.Button(
    master=button_frames,
    text="Scissors",
    command=setScissors
)



user_choice_frame = tk.Frame(
    master=app,
   
)
you_choose = tk.Label(text="Your choice: ", master=user_choice_frame)
user_choice_label = tk.Label(
    master=user_choice_frame,
    bg="blue",
    text="Make a Choice"
)

sure_button = tk.Button(
    master=app,
    text="You sure?",
    command=changeUi
)



won_label = tk.Label(
    master=app,
    bg="green",
    text=""
)


button_frames.grid(row=1, column=0, pady=30)
computer_choice_button_rock.grid(row=0,column=0)
computer_choice_button_paper.grid(row=0,column=1)
computer_choice_button_scissors.grid(row=0,column=2)
sure_button.grid(row=4, column=0, padx=20)
you_choose.grid(row=0, column=0)
user_choice_label.grid(row=0, column=1, padx=40)
user_choice_frame.grid(row=2, column=0, pady=5,)
won_label.grid(row=3, column=0, pady=5)



app.mainloop()