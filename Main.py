import random
import sys

all_cards=['A of Hearts', 'A of Diamond', 'A of Spade', 'A of Club', '1 of Hearts', '1 of Diamond', '1 of spade',
    '1 of Club', '2 of Hearts', '2 of Diamond', '2 of Spade', '2 of Club', '3 of Hearts', '3 of Diamond', '3 of spade',
    '3 of Club', '4 of Hearts', '4 of Diamond', '4 of Spade', '4 of Club', '5 of Hearts', '5 of Diamond', '5 of spade',
    '5 of Club', '6 of Hearts', '6 of Diamond', '6 of Spade', '6 of Club', '7 of Hearts', '7 of Diamond',
    '7 of spade','7 of Club', '8 of Hearts', '8 of Diamond', '8 of spade', '8 of Club', '9 of Hearts', '9 of Diamond',
    '9 of spade','9 of Club', '10 of Hearts', '10 of Diamond', '10 of spade', '10 of Club', 'J of Hearts',
    'J of Diamond', 'J of spade','J of Club', 'K of Hearts', 'K of Diamond', 'K of spade', 'K of Club', 'Q of Hearts',
    'Q of Diamond', 'Q of spade', 'Q of Club',
           ]
# cards_value = {'A': (1, 11), 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'Q': 10, 'K': 10, 'J': 10}
# list1 = []
wins = 0
losses = 0
streak = 21


class Choice:
    pass


class Deck(Choice):
    i = 0
    j = 0
    win = False
    player_win = "false"
    busted = 0
    player_cards = []
    computer_cards = []
    player_value = 0
    computer_value = 0
    computer_list_value = 0
    player_list_value = 0
    def __init__(self):
        # self.name = name
        # self.balance=balance
        pass

    def person(self):
        self.player_cards.append(random.choice(all_cards))
        # self.i += 1
        # print("i value",self.i)
        return self.player_cards

    def computer(self):
        self.computer_cards.append(random.choice(all_cards))
        # self.j += 1
        # print("value of j ", self.j)
        return self.computer_cards

    def display(self):
        print(self.player_cards)
        print(self.computer_cards)

    # person()
    # computer()
    # print(player_cards)
    # print(player_cards)
    def mechanism(self):
        self.player_value = self.player_value - self.player_list_value
        for i in range(len(self.player_cards)):
            if self.player_cards[i][0] == "A":
                choose = input("choose the value of player A you want to use")
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
            elif (self.player_cards[i][0] + self.player_cards[i][1]) == "10":
                value2 = 10
                self.player_value += value2
            else:
                self.player_value += int(self.player_cards[i][0])
        self.player_list_value=self.player_value
        print("value of player is", self.player_value)
        print("value of player list is", self.player_list_value)

        self.computer_value = self.computer_value - self.computer_list_value
        for j in range(len(self.computer_cards)):
            if self.computer_cards[j][0] == "A":
                choose = input("choose the value of computer A you want to use")
                value1 = int(choose)
                self.computer_value += value1
            elif self.computer_cards[j][0] == 'K':
                value2 = 10
                self.computer_value += value2
            elif self.computer_cards[j][0] == "Q":
                value2 = 10
                self.computer_value += value2
            elif self.computer_cards[j][0] == 'J':
                value2 = 10
                self.computer_value += value2
            elif (self.computer_cards[j][0] + self.computer_cards[j][1]) == "10":
                value2 = 10
                self.computer_value += value2
            else:
                self.computer_value += int(self.computer_cards[j][0])
        self.computer_list_value = self.computer_value
        print("value of computer is", self.computer_value)
        print("value of computer list is", self.computer_list_value)

    def value_check(self):
        if self.player_value > 21:
            self.busted += 1
            print("player busted")
            sys.exit()
        elif self.player_value == 21:
            print("player won ")
            win = True
            sys.exit()

        elif self.computer_value == 21:
            print("Computer won")
            win = True
            sys.exit()

        elif self.computer_value > 21:
            print("computer busted")
            sys.exit()

# hey = Deck()
# hey.person()
# hey.computer()
#
# hey.display()
# hey.mechanism()
# hey.value_check()


class Choice(Deck):

    def choices(self):
        # while(win=="False"):
        print(self.win)

        if(self.win == False):
            while(self.win==False):
                choice = input("Enter your choice : hit or stand")
                if (choice == "hit"):
                    # while(choice == "hit"):

                        Deck.person(self)
                        Deck.display(self)
                        Deck.mechanism(self)
                        Deck.value_check(self)
                else:
                    self.win = True
                    # sys.exit()
                    Choice.computer_choice(self)

    def computer_choice(self):
        while (self.computer_value < 17):
            Deck.computer(self)
            Deck.display(self)
            Deck.mechanism(self)
            Deck.value_check(self)
            Choice.final(self)

    def final(self):
        if self.player_value > self.computer_value:
            # player_win = True
            print("Player won")
            self.win = True

            sys.exit()
        else:
            print("Computer won")
            self.win = True
            sys.exit()

#
# hey=Choice()
# hey.final()


class Money(Choice):

    Balance = 200
        # int(input("Enter your Balance"))


    def __init__(self):
        Deck.__init__(self)
        Choice.__init__(self)

    def add_money(self, amount):
        self.Balance += amount

    def debt(self):
        amount = 100
            # int(input("Enter the amount to bet"))
        if amount > self.Balance:
            print("Your balance is low")
        else:
            self.Balance -= amount
            # print(self.Balance)
            Deck.person(self)
            Deck.person(self)
            Deck.computer(self)
            Deck.computer(self)
            Deck.display(self)
            Deck.mechanism(self)
            Deck.value_check(self)
            Choice.choices(self)
            # Choice.final(self)
        if self.win == True:
            self.Balance += amount



class Main(Money):

    def __init__(self):
        Money.__init__(self)

    def winner(self):
        Money.debt(self)


hey = Main()
hey.winner()
