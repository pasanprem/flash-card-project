############## First Task - Unguided #######################

# from tkinter import *
#
# BACKGROUND_COLOR = "#B1DDC6"
#
# # ---------------GENERATE INTERFACE ---------------- #
#
# window = Tk()
# window.title("Flashy")
# window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
#
# canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
# front = PhotoImage(file="images\card_front.png")
# back = PhotoImage(file="images\card_back.png")
# image_wrong = PhotoImage(file="images\wrong.png")
# image_right = PhotoImage(file="images\\right.png")  # What the hell is wrong with this?? Turns out it need to escape \ . Why??
#
# canvas.create_image(400, 300, image=front)
# canvas.grid(column=0, row=0, columnspan=2, rowspan=2)
#
# french_word = "TO_DO"
# english_word = "TO_DO"
#
# label_title = Label(text="French",font=("Arial",40,"italic"))
# label_title.grid(column=0,row=0,columnspan=2)
#
# label_french = Label(text=french_word,font=("Arial",60,"bold"))
# label_french.grid(column=0,row=1,columnspan=2)
#
# # label_english = Label(text=english_word)
# # label_english.grid(column=0,row=1)
#
# button_wrong = Button(image=image_wrong, highlightthickness=0)
# button_wrong.grid(column=0, row=3)
#
# button_right = Button(image=image_right, highlightthickness=0)
# button_right.grid(column=1, row=3)
#
# window.mainloop()

############ First Task - Guided ################################

#Based on the tutor



import pandas.core.tools.datetimes



# ############ Task 2 - Unguided #############################
#
# import random
# import pandas as pd
#
# word_list = pd.read_csv("data/french_words.csv")
# word_dict = pandas.DataFrame.to_dict(word_list)
# # print(word_dict)
#
#
# def get_french_word():
#     index = random.randint(0,99)
#     global word_dict
#     word = word_dict["French"][index]
#     # print(word)
#     canvas.create_text(400, 263, text=word, font=("Arial", 60, "bold"))
#################### End #################################

# ---------------GENERATE INTERFACE ---------------- #

############ 2nd Task - Guided ##############################

from tkinter import *
import pandas
import random
from time import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_date = pandas.read_csv("data/french_words.csv")
    to_learn = original_date.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


####################
## PROBLEM - To learn list keep resetting to the full list
###################

# print(to_learn)
# print(to_learn[2]) # The syntax to get key value pair


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)

    # canvas.itemconfig(card_background, image=card_front_img)  # This part did not work. Goes straight to back image.
    # canvas.after((3000))
    # canvas.itemconfig(card_background, image=card_back_img)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)           # Removes the card from the full list
    data = pandas.DataFrame(to_learn)       # Converts the full list minus the currnet card in to a data frame
    data.to_csv("data/words_to_learn.csv", index=False)       # Creates this csv with the current full list
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400,263,image=card_front_img)

card_back_img = PhotoImage(file="images/card_back.png")


card_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()
