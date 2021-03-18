import random
from game.actor import Actor

class Buffer(Actor):
    def __init__(self):
        super().__init__()
        
        self.set_text('')
        self.set_position(0,20)

    def The_Text(self,letter):
        if letter == "*":
            self.set_text('')
        else:
            text = self.get_text()
            text = text + letter
            self.set_text(text)

    def contains(self, word):
        x = self.get_text()
        y = x.find(word)
        if y == 0:
            self.set_text('')
            return True 
        else: 
            return False




