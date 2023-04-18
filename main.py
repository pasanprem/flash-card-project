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

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------GENERATE INTERFACE ---------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_img)

canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0)
known_button.grid(row=1,column=1)

window.mainloop()

############ Task 2 - Unguided #############################



