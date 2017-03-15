__author__ = 'Preston Sheppard'
from Game.GameObjects.square import Square
class GameEngine:
    def __init__(self, game):
        self.game = game
        self.square = Square(game)

    def run(self):
        """
        This method is called every tick. Everything that is required
        to run the game should be called here. By default it runs all
        objects that inherit from the GameObject class
        :return: None
        """
        #example:
        print("running")

    def keyReleased(self, event):
        """
        All key released events are passed from root to this method
        for convenience.

        To determine what key was pressed:
            if event.keysym == "d":
                do something
            elif event.keysym == "space":
                do something
            etc.

        To determine the keysym of a desired key, place: print(event.keysym)
        in this method, and then press the desired key

        :param event: the event passed from root
        :return: None
        """
        #example:
        if event.keysym == "a":
            print("a key pressed")


    def keyPressed(self, event):
        """
        All key pressed events are passed from root to this method
        for convenience.

        To determine what key was pressed:
            if event.keysym == "d":
                do something
            elif event.keysym == "space":
                do something
            etc.

        To determine the keysym of a desired key, place: print(event.keysym)
        in this method, and then press the desired key

        :param event: the event passed from root
        :return: None
        """
        #example:
        if event.keysym == "a":
            print("a key released")





