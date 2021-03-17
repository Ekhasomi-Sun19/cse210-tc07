class Actor():
    def __init__(self):
        self.__position = (0,0)
        self.__velocity = (0,0)
        self.__text = ""

    def set_text(self, text):
        self.__text = text

    def set_position(self, x, y):
        self.__position = (x, y)

    def set_velocity(self, x, y):
        self.__velocity = (x, y)

    def move_next(self):
        x1 = self.__position[0]
        y1 = self.__position[1]
        x2 = x1 + self.velocity[0]
        y2 = y1 + self.velocity[1]
        self.__position = (x2, y2)

    def get_text(self):
        return self.__text

    def get_velocity(self):
        return self.__velocity

    def get_position(self):
        return self.__position