"""
Represents a round of the game, storing things like
word,time, skips, drawing player and more.
"""
import time as t
from _thread import *
class Round(object):
    def __init__(self, word, player_drawing, players):
        """
        init object
        :param word: str
        :param player_drawing: Player
        :param players: Player[]
        """
        self.word = word
        self.play_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.player_scores = {player: 0 for player in players}
        self.time = 75
        self.start = t.time()
        start_new_thread(self.time_thread, ())

    def time_thread(self):
        """
        Runs in thread to keep track of time
        :return: None
        """

        while self.time > 0:
               t.sleep(1)
               self.time -= 1         
              self.end_round("Time is up")

    def guess(self, player, wrd):
        """
        :return bool if player got guess correct
        :param player: Player
        :param wrd: str
        :return: bool
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
            #TODO implement scoreing system here

    def player_left(self, player):
        """
        removes player that left from scores and list
        :param player: Player
        :return:none
        """
        # might not be able to use player as key in
        if player in self.player_scores:
            del self.player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player == self.player_drawming:
            self.end_round("Drawing player leaves")

    def end_round(self,msg):
        #TODO implement end_round functionallity
        pass
