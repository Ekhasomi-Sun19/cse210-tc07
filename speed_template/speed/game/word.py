import random
import game.constants
from game.actor import Actor

class Word(Actor):
    def __init__(self, word):
        super().__init__()
        self.set_text(word)
        self.set_position(0, random.randint(1, game.constants.MAX_Y-1))
        self.set_velocity(1, 0)
        #self.__value = int(len(word))

    # def get_value(self):
    #     return self.__value

    def is_expired(self):
        position = self.get_position()
        if position[0] > 60:
            return True
        else:
            return False