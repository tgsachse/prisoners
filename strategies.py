""""""

import random
from constants import COOPERATE, DEFECT, POINTS

class RandomStrategy:
    """Randomly choose whether to coorperate or defect each game."""
    NAME = "RANDOM"

    def execute(self, opponent):
        """Randomly choose to cooperate or defect."""
        return random.choice((COOPERATE, DEFECT))


    def reflect(self, opponent, opponent_action):
        """Don't reflect or remember any information.'"""
        pass

    
    def reset(self):
        """Nothing to reset."""
        pass

class AlwaysDefectStrategy:
    """Always defect, every game."""
    NAME = "ALWAYS_DEFECT"

    def execute(self, opponent):
        """Always defect."""
        return DEFECT


    def reflect(self, opponent, opponent_action):
        """Don't reflect or remember anything.'"""
        pass


    def reset(self):
        """Nothing to reset."""
        pass


class AlwaysCooperateStrategy:
    """Always cooperate like a total sucker."""
    NAME = "ALWAYS_COOPERATE"
   
    def execute(self, opponent):
        """Always cooperate."""
        return COOPERATE


    def reflect(self, opponent, opponent_action):
        """Don't reflect or remember anything.'"""
        pass


    def reset(self):
        """Nothing to reset."""
        pass


class GrudgerStrategy:
    """Always cooperate with those who have not wronged you."""
    NAME = "GRUDGER"

    def __init__(self):
        """Create a set to remember cheaters."""
        self.cheaters = set()


    def execute(self, opponent):
        """Cooperate with those who haven't wronged you."""
        return DEFECT if opponent in self.cheaters else COOPERATE

    
    def reflect(self, opponent, opponent_action):
        """If the opponent defected, remember it."""
        if opponent_action == DEFECT:
            self.cheaters.add(opponent)


    def reset(self):
        """Forget the cheaters for the next generation."""
        self.cheaters = set()


class TitForTatStrategy:
    """If your opponent did you wrong, hit them back."""
    NAME = "TIT_FOR_TAT"

    def __init__(self):
        """Create a set to remember those who did you wrong."""
        self.cheaters = set()


    def execute(self, opponent):
        """Strike back against those who do you wrong."""
        if opponent in self.cheaters:
            self.cheaters.remove(opponent)

            return DEFECT
        else:
            return COOPERATE


    def reflect(self, opponent, opponent_action):
        """If the opponent defected, they did you wrong and must be punished."""
        if opponent_action == DEFECT:
            self.cheaters.add(opponent)


    def reset(self):
        """Forget the cheaters for the next generation."""
        self.cheaters = set()


STRATEGIES = {
    "RANDOM" : RandomStrategy,
    "ALWAYS_DEFECT" : AlwaysDefectStrategy,
    "ALWAYS_COOPERATE" : AlwaysCooperateStrategy,
    "GRUDGER" : GrudgerStrategy,
    "TIT_FOR_TAT" : TitForTatStrategy,
}
