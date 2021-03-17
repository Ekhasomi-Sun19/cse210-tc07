from time import sleep
from game import constants
from game.word_generator import WordGenerator
from game.score import Score
from game.word import Word
from game.Buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service #
        self._keep_playing = True
        self._output_service = output_service #
        self._score = Score() # 
        self._genie = WordGenerator()
        self._buffer = Buffer()
        self.words = []
        self.first_five()


    def first_five(self):
        for i in range(5):
            word = self._genie.generate
            self._word = Word(word)
            self.words.append(self._word)
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        self._buffer.The_Text(letter)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        for word in self._words:
            word = word.get_text()
            if self._buffer.contains(word):
                self._score.add_points(1)

        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        for i in self.words:
            self._output_service.draw_actors(i)
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._buffer.get_text())
        self._output_service.flush_buffer()
