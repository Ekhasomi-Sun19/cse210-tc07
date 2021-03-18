#from game.constants import LIBRARY
#from game.constants import LIBRARY
import random
import game.constants

class WordGenerator():

    def __init__(self):
        self.list = game.constants.LIBRARY

    def generate(self):
        x = random.choice(self.list)
        return x


        