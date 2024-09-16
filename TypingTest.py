# Importing the modules
from english_words import get_english_words_set
from tkinter import *
import tkinter.font as font
import random

# Initialize global variables
score = 0
time_elapsed = 0
count = 0
words = list(get_english_words_set(sources=['common']))  # Provide the required argument

def startGame():
    # Creating the game window and adding size, title and color
    wn = Tk()
    wn.geometry('700x600')
    wn.title('Typing Test By PythonGeeks')
    wn.config(bg='honeydew2')

    def timeFunc():
        global time_elapsed, score, count
        if count <= 10:  # If count is less than or equal to 10, update the time
            time_elapsed += 1
            timer.configure(text=time_elapsed)
            timer.after(1000, timeFunc)
        else:  # If count is more than 10, show the results
            result = Label(wn, text='', font=('arial', 25, 'italic bold'), fg='grey')
            result.place(x=230, y=250)
            result.configure(text='Time taken = {} \nScore = {} \nMissed = {}'
                                      .format(time_elapsed, score, count - score))
            # Reset variables
            time_elapsed, score, count
            time_elapsed = 0
            score = 0
            count = 0
            # Destroy widgets
            nextWord.destroy()
            userInput.destroy()
            scorelabel.destroy()
            scoreboard.destroy()
            timerlabel.destroy()
            timer.destroy()

    def mainGame(event):
        global score, count, time_elapsed
        if time_elapsed == 0:  # At the start of the game
            random.shuffle(words)  # Shuffle the list of words
            nextWord.configure(text=words[0])  # Show the first word
            userInput.delete(0, END)  # Clear the input field
            timeFunc()  # Start the timer

        if userInput.get() == nextWord['text']:  # Check if the input matches the word
            score += 1
            scoreboard.configure(text=score)  # Update the score
        count += 1
        if count <= 10:  # Update word if count is less than or equal to 10
            random.shuffle(words)
            nextWord.configure(text=words[0])
            userInput.delete(0, END)  # Clear the input field

    # Creating labels and widgets
    label = Label(wn, text='Typing Test By PythonGeeks', font=('arial', 25, 'italic bold'), fg='gray', width=40)
    label.place(x=10, y=10)

    nextWord = Label(wn, text='Hit enter button to start and after typing the word', font=('arial', 20, 'italic bold'), fg='black')
    nextWord.place(x=30, y=240)

    scorelabel = Label(wn, text='Your Score:', font=('arial', 25, 'italic bold'), fg='red')
    scorelabel.place(x=10, y=100)

    scoreboard = Label(wn, text=score, font=('arial', 25, 'italic bold'), fg='blue')
    scoreboard.place(x=100, y=180)

    timerlabel = Label(wn, text='Time Elapsed:', font=('arial', 25, 'italic bold'), fg='red')
    timerlabel.place(x=450, y=100)

    timer = Label(wn, text=time_elapsed, font=('arial', 25, 'italic bold'), fg='blue')
    timer.place(x=560, y=180)

    userInput = Entry(wn, font=('arial', 25, 'italic bold'), bd=10, justify='center')
    userInput.place(x=150, y=330)
    userInput.focus_set()

    wn.bind('<Return>', mainGame)  # Run the mainGame function on pressing enter
    wn.mainloop()  # Run the window until it is closed

# Creating the main window
wn = Tk()
wn.geometry('600x600')
wn.title("PythonGeeks Typing Test")
wn.config(bg='LightBlue1')

# Creating a frame to show the title of the project
headingFrame1 = Frame(wn, bg="snow3", bd=5)
headingFrame1.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n PythonGeeks Typing Test", bg='azure2', fg='black', font=('Courier', 15, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Creating a button to start the game
btn = Button(wn, text="Start", bg='old lace', fg='black', width=20, height=2, command=startGame)
btn['font'] = font.Font(size=12)
btn.place(x=200, y=300)

wn.mainloop()  # Run the window until it is closed
