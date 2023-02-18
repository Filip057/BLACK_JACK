
class Player:

    def __init__(self):
        self.score = 0
        self.card_deck = []
        self.card_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                            "9": 9, "10": 10, "jack": 10, "queen": 10, "king": 10, "ace": [1, 11]}

    def count_score(self):
        self.score = 0
        if "ace" not in self.card_deck:
            for card in self.card_deck:
                self.score += self.card_values[card]
        else:
            sc = 0
            aces = []
            secundary = self.card_deck.copy()

            for card in secundary:
                if card == "ace":
                    aces.append(card)
                    secundary.remove(card)
            for card in secundary:
                sc += self.card_values[card]
            for ace in aces:
                difference = 21 - sc
                if difference >= 11:
                    sc += self.card_values[ace][1]
                else:
                    sc += self.card_values[ace][0]
            self.score = sc

    def show_cards(self):
        return self.card_deck







