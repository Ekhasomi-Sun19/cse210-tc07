import random
from game import constants
from game.actor import Actor
from game.point import Point

class Food(Actor):
    """A nutritious substance that snake's like. The responsibility of Food is to keep track of its appearance and position. A Food can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._points = 0
        self.set_text("@")
        self.reset()
    
    def get_points(self):
        """Gets the points this food is worth.
        
        Args:
            self (Food): an instance of Food.

        Returns:
            integer: The points this food is worth.
        """
        return self._points

    def reset(self):
        """Resets the food by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
        
        Args:
            self (Food): an instance of Food.
        """
        self._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)
        
