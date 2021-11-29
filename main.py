from tkinter import *
import csv
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

class Card():
    def __init__(self):

        self.deck = []
        self.current_card = {}
        self.load_cards()
        self.timer = root.after(3000, self.flip_card)

        # UI setup
        # Canvas
        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_front = PhotoImage(file="images/card_front.png")
        self.card_back = PhotoImage(file="images/card_back.png")

        self.current_side = self.canvas.create_image(405,263, image=self.card_front)
        self.language = self.canvas.create_text(400,150, text="", font=(FONT_NAME, 40, "italic"))
        self.word = self.canvas.create_text(400,263, text="", font=(FONT_NAME, 60, "bold"))
        self.canvas.grid(column=1, row=0, columnspan=2, rowspan=2)

        # Buttons
        self.right_img = PhotoImage(file="images/right.png")
        self.wrong_img = PhotoImage(file="images/wrong.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=self.next_card)
        self.right_button = Button(image=self.right_img, highlightthickness=0, bd=0, bg=BACKGROUND_COLOR, command=self.next_card)
        self.right_button.grid(column=1,row=2)
        self.wrong_button.grid(column=2,row=2)
        
    def load_cards(self):
        with open("data/french_words.csv") as csvfile:
            records = csv.DictReader(csvfile)
            self.deck = [row for row in records]
    def next_card(self):
        # Might want to change how this is done entirely
        # could add a flag to see if the card is on front or back
        root.after_cancel(self.timer)
        choice = random.randint(0, len(self.deck) - 1)
        self.current_card = self.deck[choice]
    
        self.canvas.itemconfig(self.current_side, image=self.card_front)
        self.canvas.itemconfig(self.language, text="French", fill="black")
        self.canvas.itemconfig(self.word, text=self.current_card["French"], fill="black")

        self.timer = root.after(3000, self.flip_card)
    def flip_card(self):
        self.canvas.itemconfig(self.current_side, image=self.card_back)
        self.canvas.itemconfig(self.language, text="English", fill="white")
        self.canvas.itemconfig(self.word, text=self.current_card["English"], fill="white")

# Window
root = Tk()
root.title("Flashy")
root.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

card = Card()

# Main loop
card.next_card()
root.mainloop()