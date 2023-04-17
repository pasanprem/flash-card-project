from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------GENERATE INTERFACE ---------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="images\card_front.png")
back = PhotoImage(file="images\card_back.png")
image_wrong = PhotoImage(file="images\wrong.png")
image_right = PhotoImage(file="images\\right.png")  # What the hell is wrong with this?? Turns out it need to escape \ . Why??

canvas.create_image(400, 300, image=front)
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)

french_word = "TO_DO"
english_word = "TO_DO"

label_title = Label(text="French",font=("Arial",50))
label_title.grid(column=0,row=0,columnspan=2)

label_french = Label(text=french_word,font=("Arial",30))
label_french.grid(column=0,row=1,columnspan=2)

# label_english = Label(text=english_word)
# label_english.grid(column=0,row=1)

button_wrong = Button(image=image_wrong, highlightthickness=0)
button_wrong.grid(column=0, row=3)

button_right = Button(image=image_right, highlightthickness=0)
button_right.grid(column=1, row=3)

window.mainloop()
