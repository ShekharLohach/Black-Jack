import random

all_cards=['A of Hearts', 'A of Diamond', 'A of Spade', 'A of Club', '1 of Hearts', '1 of Diamond', '1 of spade',
    '1 of Club', '2 of Hearts', '2 of Diamond', '2 of Spade', '2 of Club', '3 of Hearts', '3 of Diamond', '3 of spade',
    '3 of Club', '4 of Hearts', '4 of Diamond', '4 of Spade', '4 of Club', '5 of Hearts', '5 of Diamond', '5 of spade',
    '5 of Club', '6 of Hearts', '6 of Diamond', '6 of Spade', '6 of Club', '7 of Hearts', '7 of Diamond',
    '7 of spade','7 of Club', '8 of Hearts', '8 of Diamond', '8 of spade', '8 of Club', '9 of Hearts', '9 of Diamond',
    '9 of spade','9 of Club', '10 of Hearts', '10 of Diamond', '10 of spade', '10 of Club', 'J of Hearts',
    'J of Diamond', 'J of spade','J of Club', 'K of Hearts', 'K of Diamond', 'K of spade', 'K of Club', 'Q of Hearts',
    'Q of Diamond', 'Q of spade', 'Q of Club',
           ]

cards_value = {'A': (1, 11), 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'Q': 10, 'K': 10, 'J': 10}
list1 = []
wins = 0
losses = 0
streak = 21
win = False

#decide computer factor
class Deck:

    busted = 0
    player_cards = []
    computer_cards = []
    player_value = 0
    computer_value = 0

    def __init__(self):
        # self.name = name
        # self.balance=balance
        pass

    def person(self):
        self.player_cards.append(random.choice(all_cards))

        return self.player_cards

    def computer(self):
        self.computer_cards.append(random.choice(all_cards))

        return self.computer_cards

    def display(self):
        print(self.player_cards)
        print(self.computer_cards[0])

    # person()
    # computer()
    # print(player_cards)
    # print(player_cards)
    def mechanism(self):
        for i in range(len(self.player_cards)):
            if self.player_cards[i][0] == "A":
                choose = input("choose the value of A you want to use")
                value1 = int(choose)
                self.player_value += value1
            elif self.player_cards[i][0] == 'K':
                value2 = 10
                self.player_value += value2
            elif self.player_cards[i][0] == "Q":
                value2 = 10
                self.player_value += value2
            elif self.player_cards[i][0] == 'J':
                value2 = 10
                self.player_value += value2
            else:
                self.player_value += int(self.player_cards[i][0])
                # computer_value=self.computer_cards[i][0] + computer_value
        print(self.player_value)

        for i in range(len(self.computer_cards)):
            if self.computer_cards[i][0] == "A":
                choose = input("choose the value of A you want to use")
                value1 = int(choose)
                self.computer_value += value1
            elif self.computer_cards[i][0] == 'K':
                value2 = 10
                self.computer_value += value2
            elif self.computer_cards[i][0] == "Q":
                value2 = 10
                self.computer_value += value2
            elif self.computer_cards[i][0] == 'J':
                value2 = 10
                self.computer_value += value2
            else:
                self.computer_value += int(self.computer_cards[i][0])
                # computer_value=self.computer_cards[i][0] + computer_value
        print(self.computer_value)

    def value_check(self):
        if self.player_value > 21:
            self.busted += 1
            print("player busted")
        elif self.computer_value > 21:
            print("computer busted")

        else:
            if self.player_value > self.computer_value:
                # diff = self.player_value-self.computer_value
                win=True
                print("player won")

            else:
                # diff = self.computer_value - self.player_value
                print("computer won")


class Choice(Deck):

    def choices(self):
        # while(win=="False"):
        choice = input("Enter your chioce")
        if choice == "hit":
            Deck.person(self)
        else:
            Deck.mechanism(self)
            Deck.value_check(self)


# hey=Choice()
# hey.choices()
# hey = Deck()
# hey.person()
# hey.computer()
# hey.display()
# hey.mechanism()
# hey.value_check()


class Money(Deck):

    win = False
    Balance=int(input("Enter your Balance"))

    def __init__(self):
        Deck.__init__(self)

    def add_money(self, amount):
        self.balance += amount

    def debt(self):
        amount = int(input("Enter the amount to bet"))
        if amount > self.balance:
            print("Your balance is low")
        else:
            self.balance -= amount
            print(self.balance)
            Deck.person(self)
            Deck.person(self)
            Deck.computer(self)
            Deck.computer(self)
            Deck.display(self)
            Deck.mechanism()
            Deck.value_check()
            if self.win == True:
                self.balance += amount


class Main(Money):

    def __init__(self):
        Money.__init__(self)

    def winner(self):
        while win == False :
            Money.debt(self)

hey=Main()
hey.winner()
