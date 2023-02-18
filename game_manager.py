import random

clubs = "_of_clubs.png"
diamonds = "_of_diamonds.png"
hearts = "_of_hearts.png"
spades = "_of_spades.png"


class GameManager():

    def __init__(self):
        self.card_deck = {"clubs": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"],
                          "diamonds": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"],
                          "hearts": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"],
                          "spades": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]}
        #setting who is winning, default all False
        self.pc_win = 0
        self.pl_win = 0
        self.draw = 0

    # start welcome
    def give_welcome(self):
        message = 'WELLCOME TO BLACKJACK!!! \n' \
                  '...may the LUCK be with you...\n' \
                  'ENJOY'
        return message

    # adding card to a deck
    def add_card(self, card_hand):
        types = ["clubs", "diamonds", "hearts", "spades"]
        pic = {"clubs": clubs, "diamonds": diamonds, "hearts": hearts,"spades": spades}
        new_card_type = random.choice(types)
        new_card = random.choice(self.card_deck[new_card_type])
        card_hand.append(new_card)
        self.card_deck[types].remove(new_card)

    # changing outcome
    def evaluate(self, pc_score, human_score):
        diff = pc_score - human_score
        if human_score > 21:
            self.pc_win = 1
        elif human_score == pc_score:
            self.draw = 1
        elif diff > 0 and pc_score < 22:
            print(pc_score, human_score)
            self.pc_win = 1
        else:
            self.pl_win = 1

    def place_bet(self):
        pass
