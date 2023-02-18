from game_manager import GameManager
from player import Player
from gui_blackjack import GuiBlackjack

game = GameManager()


'''
GUI 
open window - give welcome
start button that stats the game 
    - computer round 
    - player cards 
    bet 
    split??? 
    - add a card 
    if over instant lose
    if 21 win if not draw 
    
'''

game.give_welcome()
computer = Player()
human = Player()
gui = GuiBlackjack()
gui.show_card(["cards/2_of_clubs.png"])


game.add_card(computer.card_deck)
game.add_card(computer.card_deck)
computer.count_score()
print("\n")
print("COMPUTER turn")
if computer.score < 17:
    game.add_card(computer.card_deck)
    computer.count_score()
print(f"Computer has [{computer.card_deck[0]}, XX]")
print("\n")

print("Your turn!")
print("\n")

game.add_card(human.card_deck)
game.add_card(human.card_deck)
print(human.show_cards())
human.count_score()
if human.score < 21:
    while True:
        if input("Do you want to add a card?") == "1":
            game.add_card(human.card_deck)
            human.count_score()
            print(human.show_cards())
        else:
            break

print(game.evaluate(computer.score, human_score=human.score))
print(f"Computer cards: {computer.show_cards()}")
print(f"Your cards: {human.show_cards()}")
























