import random
from game.actor import Actor

class Buffer(Actor):
    def __init__(self):
        super().__init__()
        
        self.set_text('')

    def The_Text(self,letter):
        if letter == '*':
            self.set_text('')
        else:
            text = get_text()
            text = text + letter
            self.set_text(text)




