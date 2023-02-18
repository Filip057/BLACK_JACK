# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
from game_manager import GameManager


class GuiBlackjack(GameManager):

    def __init__(self):
        super().__init__()
        # Create an instance of tkinter frame
        self.win = Tk()
        # Set the geometry of tkinter frame
        self.win.geometry("482x332")
        self.win.title("BLACKJACK")
        # Create a canvas
        self.canvas = Canvas(self.win, width=483, height=332)
        self.canvas.pack()

        # Load an image in the script
        img = ImageTk.PhotoImage(Image.open("backround.png"))

        # Add image to the Canvas Items
        self.canvas.create_image(10, 10, anchor=NW, image=img)



    def show_card(self, card_deck):
        x = 0
        for i in range(len(card_deck)):
            card = card_deck[i]
            img_card = Image.open(card)
            resized_card = img_card.resize((100, 145), Image.ANTIALIAS)
            new_card = ImageTk.PhotoImage(resized_card)
            self.canvas.create_image(0, x, anchor=NW, image=new_card)
            x += 10


        self.win.mainloop()