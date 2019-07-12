import random
from itertools import permutations, repeat
all_cards=['A of Hearts','A of Diamond','A of Spades','A of Club','1 of Hearts','1 of Diamond','1 of Spades',
    '1 of Club', '2 of Hearts','2 of Diamond','2 of Spades','2 of Club','3 of Hearts','3 of Diamond','3 of Spades',
    '3 of Club', '4 of Hearts','4 of Diamond','4 of Spades','4 of Club','5 of Hearts','5 of Diamond','5 of Spades',
    '5 of Club', '6 of Hearts','6 of Diamond','6 of Spadesv','6 of Club','7 of Hearts','7 of Diamond','7 of Spades',
    '7 of Club', '8 of Hearts','8 of Diamond','8 of Spades','8 of Club','9 of Hearts','9 of Diamond','9 of Spades',
    '9 of Club', '10 of Hearts','10 of Diamond','10 of Spades','10 of Club','J of Hearts','J of Diamond','J of Spades',
    'J of Club', 'K of Hearts','K of Diamond','K of Spades','K of Club','Q of Hearts','Q of Diamond','Q of Spades',
    'Q of Club',
           ]

cards_value = {'A': (1, 11), 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'Q': 10, 'K': 10, 'J': 10}
list1 = []
wins = 0
player_value = 0
computer_value = 0
busted = 0
losses = 0
streak = 21
win=False
class Deck() :
    # busted=0
    player_cards = ['J of Club', 'K of Hearts','8 of Spades']
    computer_cards = ['8 of Spades']
    player_value = 0
    computer_value = 21

    def __init__(self, name,balance):
        self.name = name
        self.balance=balance

    def person(self):
        self.player_cards.append(random.choice(all_cards))
        self.player_cards.append(random.choice(all_cards))
        return self.player_cards

    def computer(self):
        self.computer_cards.append(random.choice(all_cards))
        self.computer_cards.append(random.choice(all_cards))
        return self.computer_cards[0]
    # person()
    # computer()
    # print(player_cards)
    # print(player_cards)
    def mechanism(self):
        for i in range(len(self.player_cards)):
            if(self.player_cards[i][0]=="A"):
                choose=input("choose the value of A you want to use")
                A=choose
                self.player_value += A
            elif(self.player_cards[i][0]=='K'):
                K=10
                self.player_value += K
            elif (self.player_cards[i][0] == "Q"):
                K = Q = J = 10
                self.player_value += K
            elif (self.player_cards[i][0] == 'J'):
                K = Q = J = 10
                self.player_value += K
            else:
                self.player_value +=int(self.player_cards[i][0])
                # computer_value=self.computer_cards[i][0] + computer_value
        print(self.player_value)

        for i in range(len(self.computer_cards)):
            if(self.computer_cards[i][0]=="A"):
                choose=input("choose the value of A you want to use")
                A=choose
                self.computer_value += A
            elif(self.computer_cards[i][0]=='K'):
                K=10
                self.computer_value += K
            elif (self.computer_cards[i][0] == "Q"):
                K = Q = J = 10
                self.computer_value += K
            elif (self.computer_cards[i][0] == 'J'):
                K = Q = J = 10
                self.computer_value += K
            else:
                self.computer_value +=int(self.computer_cards[i][0])
                # computer_value=self.computer_cards[i][0] + computer_value
        print(self.computer_value)

        if(self.player_value>21 | self.computer_value>21 ):
            self.busted += 1
            if(self.player_value>21):
                return "player busted"
            else:
                return "computer busted"

        else:
            if(self.player_value>self.computer_value):
                diff = self.player_value-self.computer_value
                print("player won")
            else:
                diff = self.computer_value - self.player_value
                print("computer won")

    def choice(self):
        # while(win=="False"):
            choice=input("Enter your chioce")
            if(choice=="hit"):
                self.person()
            else:
                self.mechanism()

    def debt(self):
        amount=int(input("Enter the amount to bet"))
        if(amount>self.balance):
            print("Your balance is low")
        else:
            self.balance -=amount
            print(self.balance)
dec=Deck('john',300)
(dec.mechanism())


class Money():

    def __init__(self,balance):
        self.balance=balance

    def add_money(self,amount):
        self.balance +=amount

    def bet_amount(self,amount):
        if(self.win=='True'):
            self.balance +=amount

        else:
            self.balance -=amount



# class move():
#
#     def __init__(self,move):
#         self.move=move
#
#     def move(self):
#         if(self.move=="hit"):
#             self.player_cards.append(random.choice(all_cards))
#
#         else:
#             pass
#