""""""

import random
from constants import COOPERATE, DEFECT, POINTS

class RandomStrategy:
    """Randomly choose whether to coorperate or defect each game."""
    name = "RANDOM"

    def execute(self):
        """Randomly choose to cooperate or defect."""
        return random.choice((COOPERATE, DEFECT))


    def reflect(self, opponent):
        """Don't reflect or remember any information.'"""
        pass


class AlwaysDefectStrategy:
    """Always defect, every game."""
    name = "ALWAYS_DEFECT"

    def execute(self):
        """Always defect."""
        return DEFECT


    def reflect(self, opponent):
        """Don't reflect or remember anything.'"""
        pass


class AlwaysCooperateStrategy:
    """Always cooperate like a total sucker."""
    name = "ALWAYS_COOPERATE"
   
    def execute(self):
        """Always cooperate."""
        return COOPERATE


    def reflect(self, opponent):
        """Don't reflect or remember anything.'"""
        pass


class GrudgerStrategy:
    """Always cooperate with those who have not wronged you."""
    name = "GRUDGER"

    def execute(self):
        """Cooperate with those who haven't wronged you."""
        return COOPERATE

    
    def reflect(self, opponent):
        """If the opponent defected, remember it."""
        pass


STRATEGIES = {
    "RANDOM" : RandomStrategy,
    "ALWAYS_DEFECT" : AlwaysDefectStrategy,
    "ALWAYS_COOPERATE" : AlwaysCooperateStrategy,
    "GRUDGER" : GrudgerStrategy,
}
