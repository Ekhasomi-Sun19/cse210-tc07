import random
import constants
from actor import Actor

class Word(Actor):
    def __init__(self, word):
        super().__init__()
        self.set_text(word)
        self.set_position(0, random.randint(1, constants.MAX_Y))
        self.set_velocity(1, 0)
        self.__value = int(len(word))

    def get_value(self):
        return self.__value

    def is_expired(self):
        if self.position[0] > constants.MAX_X:
            return True
        else:
            return False