from tkinter import *
import csv
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

with open("data/french_words.csv") as csvfile:
    records = csv.DictReader(csvfile)
    translation_dict = [row for row in records]

def next_card():
    choice = random.randint(0, len(translation_dict) - 1)
    english_translation = translation_dict[choice]["English"]
    french_translation = translation_dict[choice]["French"]

    card_canvas.itemconfig(french_word, text=french_translation)

def flip_card():
    pass
    
# Window
root = Tk()
root.title("Flashy")
root.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# Canvas
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.create_image(405,263, image=card_front_img)
english_word = card_canvas.create_text(400,150, text="French", font=(FONT_NAME, 40, "italic"))
french_word = card_canvas.create_text(400,263, text=translation_dict[0]["French"], font=(FONT_NAME, 60, "bold"))
card_canvas.grid(column=1, row=0, columnspan=2, rowspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=next_card)
right_button.grid(column=1,row=2)
wrong_button.grid(column=2,row=2)

# Labels
root.mainloop()