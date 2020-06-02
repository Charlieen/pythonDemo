import random
class Card:
    showSide = 'down'
    def __init__(self, name):
        self.name = name

    def getValue(self):
        #H2 HJ
        dic = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        value = self.name[1]
        if value not in dic:
            return int(value)
        else:
            return dic[value]

    def setShowSide(self, side):
        self.showSide = side

    def __str__(self):
        if self.showSide == 'up':
            return self.name
        elif self.showSide == 'down':
            return 'COVER'
# Deck

class Deck:
    cards = []
    def __init__(self):
        SUITE = 'H D S C'.split()
        RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
        for suite in SUITE:
            for rank in RANKS:
                card = Card(suite+rank)
                self.cards.append(card)
        random.shuffle(self.cards)

    def __str__(self):
        result =''
        for item in self.cards:
            result = result + " " + item.name
        return result

    def getOne(self):
        return self.cards[:26]
    def getTwo(self):
        return self.cards[26:]
# deck = Deck()
# for idx,item in enumerate (deck.getOne()):
#     print(idx,item.name)
#
# print('---------')
# for idx,item in enumerate (deck.getTwo()):
#     print(idx,item.name)

# Hand

class Hand:

    def __init__(self, halfDeck, workSet):
        self.halfDeck = halfDeck
        self.workSet = workSet

    def _shuffleCards(self):
        for item in self.halfDeck:
            item.setShowSide('down')
        random.shuffle(self.halfDeck)

# default remove a card ,the card is up
    def removeCardOrChuPai(self):
        if len(self.halfDeck) > 0:
           card = self.halfDeck.pop(0)

           if card.showSide == 'up':
               self.halfDeck.append(card)
               self._shuffleCards()
               card = self.halfDeck.pop(0)

           card.setShowSide('up')

           self.workSet.append(card)
           return card
        else:
            return 'empty'

    def addCardOrWinCards(self,workSetB):
        self.workSet.extend(workSetB)
        for item in self.workSet:
            item.setShowSide('up')
        self.halfDeck.extend(self.workSet)
        self.workSet = []
        if len(self.halfDeck) == 52:
            return 'win'
        else:
            return 'ok'

# PLAYER

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def outCard(self):
        workSet = self.hand.removeCardOrChuPai()
        if type(workSet)== type('a'):
            return 'lose'
        else:
            return workSet


    def inCards(self,worksetB):
        result = self.hand.addCardOrWinCards(worksetB);
        if result == 'win':
            return 'win'
        else:
            return 'ok'

    def _to_cover(self,card):
        card.setShowSide('down')


class WarGame:

    round = 0
    workSetA = []
    workSetB = []

    def __init__(self):
        self.deck = Deck()
        self.playerA = Player('Mac', Hand(self.deck.getOne(),[]))
        self.playerB = Player('You', Hand(self.deck.getTwo(),[]))

    def _check_win(self):

        lenth_a = len(self.workSetA)

        if lenth_a % 2 == 0:
            return {'win': 'NO', 'cards': []}
        else:
            if self.workSetA[len(self.workSetA)-1].getValue() > self.workSetB[len(self.workSetB)-1].getValue():
                # self.workSetA.extend(self.workSetB)
                return {'win': 'A', 'cards':self.workSetA }
            elif self.workSetA[len(self.workSetA)-1].getValue() < self.workSetB[len(self.workSetB)-1].getValue():
                # self.workSetB.extend(self.workSetA)
                return {'win': 'B', 'cards':self.workSetB }
            elif self.workSetA[len(self.workSetA)-1].getValue() ==  self.workSetB[len(self.workSetB)-1].getValue():
                return {'win':'NO','cards':[]}

    def _arr_to_str(self, arr):
        result =''
        for item in arr:
            result = result + item.name
        return result


    def start_game(self):

        print("Welcome to Card Game War! PlayerA is : {}, PlayerB is {}".format(self.playerA.name, self.playerB.name))

        while len(self.playerA.hand.halfDeck) != 0 and len(self.playerB.hand.halfDeck) != 0:
            self.round = self.round + 1
            print("This is the round {}, and A has {} cards ,B has {} cards".format(self.round,len(self.playerA.hand.halfDeck),len(self.playerB.hand.halfDeck)))
            win_check = self._check_win()
            curr_round = 0

            while win_check['win'] == 'NO':
                card_a = self.playerA.outCard()
                card_b = self.playerB.outCard()
                input("You turn ,you must input {}:".format(card_b.name))
                if card_a == 'lose' or card_b == 'lose':
                    return 'game over'

                elif curr_round % 2 == 0:
                    self.workSetA.append(card_a)
                    self.workSetB.append(card_b)
                else:
                   self.playerA._to_cover(card_a)
                   self.playerA._to_cover(card_b)
                   self.workSetA.append(card_a)
                   self.workSetB.append(card_b)

                print("PlayerA's WorkSet is :{}".format(self._arr_to_str(self.workSetA)))
                print("PlayerB's WorkSet is :{}".format(self._arr_to_str(self.workSetB)))

                win_check = self._check_win()
                curr_round = curr_round + 1

            if win_check['win'] == 'A':
                in_a_cards_res = self.playerA.inCards(self.workSetB)
                self.playerB.hand.workSet = []
                self.workSetA=[]
                self.workSetB=[]
                if in_a_cards_res == 'win':
                    return 'game over'
                else:
                    print("PlayerA's WorkSet count :{}".format(len(self.workSetA)))

            elif win_check['win'] == 'B':
                in_b_cards_res = self.playerB.inCards(self.workSetA)
                self.playerA.hand.workSet = []
                self.workSetA = []
                self.workSetB = []
                if in_b_cards_res == 'win':
                    return 'game over'
                else:
                    print("PlayerB's WorkSet count :{}".format(len(self.workSetB)))


game = WarGame()

print(game.start_game())







