import csv
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

class Card():
    def __init__(self):
        super().__init__()
        self.flashcards = []
        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.front_img = PhotoImage(file="images/card_front.png")
        self.back_img = PhotoImage(file="images/card_back.png")
        self.create_image(405,263, image=card_front_img)
    def load_cards(self):
        with open("data/french_words.csv") as csvfile:
            records = csv.DictReader(csvfile)
            self.flashcards = [row for row in records]
    def next_word(self):
        choice = random.randint(0, len(self.flashcards) - 1)
        english_translation = self.flashcards[choice]["English"]
        french_translation = self.flashcards[choice]["French"]

