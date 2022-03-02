from game.casting.actor import Actor
import random

class Artifact(Actor):
    '''A collection of gems and stones falling from the top of screen.
    The responsibility of gems is to add, and remove them.  '''
    
    def __init__(self):
        '''Constructs a new gem or stone.'''
        super().__init__()
        self._is_alive = True
        self._score = 0
        
    def display(self):
        '''Sets a stone to an O.'''
        list = ["O", "*"]
        self._text = random.choice(list)
        return self._text
    
    def get_score(self):
        '''Gets the artifacts score and returns it.'''
        if self._text == "*":
            self._score += 1
        elif self._text == "O":
            self._score -= 1
        return self._score
    
        
    def set_score(self, score):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._score = score
    
    def collide(self):
        if self._is_alive == False:
            if list[0]:
                self._score -= 1
        elif self._is_alive == False:
            if list[1]:
                self._score += 1
        else: 
            pass