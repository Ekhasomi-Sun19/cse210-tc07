from constants import LIBRARY
import random

class WordGenerator():
    def __init__(self):
        self.list = LIBRARY

    def generate(self):
        return random.choice(self.list)