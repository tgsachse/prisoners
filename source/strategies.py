"""All strategies available for the Iterated Prisoner's Dilemma.

By Tiger Sachse.
"""

import random
from constants import COOPERATE, DEFECT, POINTS

class RandomStrategy:
    """Randomly choose whether to coorperate or defect each game."""
    NAME = "RANDOM"

    def execute(self, opponent):
        """Randomly choose to cooperate or defect."""
        return random.choice((COOPERATE, DEFECT))


    def reflect(self, opponent, opponent_action):
        """Don't reflect or remember any information."""
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
        """Don't reflect or remember anything."""
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
        """Don't reflect or remember anything."""
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


class ExploiterStrategy:
    """Exploit the opponent if she was nice last time."""
    NAME = "EXPLOITER"

    def __init__(self):
        """Create a set to remember the suckers."""
        self.suckers = set()


    def execute(self, opponent):
        """Cooperate unless the opponent has been nice before, then exploit."""
        if opponent in self.suckers:
            self.suckers.remove(opponent)

            return DEFECT
        else:
            return COOPERATE


    def reflect(self, opponent, opponent_action):
        """If the opponent was nice, remember to exploit later."""
        if opponent_action == COOPERATE:
            self.suckers.add(opponent)


    def reset(self):
        """Forget the suckers for the next generation."""
        self.suckers = set()


class BurnTheBridgeStrategy:
    """Once you abuse an opponent, always abuse them."""
    NAME = "BURN_THE_BRIDGE"

    def __init__(self):
        """Create a set to remember the burnt bridges."""
        self.burnt_bridges = set()


    def execute(self, opponent):
        """Randomly decide to cooperate or defect.
        
        If defecting, remember to always defect from the opponent in
        the future.
        """
        decision = random.choice((COOPERATE, DEFECT))

        if decision == DEFECT:
            self.burnt_bridges.add(opponent)
        
        return DEFECT if opponent in self.burnt_bridges else decision


    def reflect(self, opponent, opponent_action):
        """Remember nothing."""
        pass


    def reset(self):
        """Forget the burnt bridges for the next generation."""
        self.burnt_bridges = set()


# A dictionary of all strategies mapped to their names.
STRATEGIES = {
    "RANDOM" : RandomStrategy,
    "ALWAYS_DEFECT" : AlwaysDefectStrategy,
    "ALWAYS_COOPERATE" : AlwaysCooperateStrategy,
    "GRUDGER" : GrudgerStrategy,
    "TIT_FOR_TAT" : TitForTatStrategy,
    "EXPLOITER" : ExploiterStrategy,
    "BURN_THE_BRIDGE" : BurnTheBridgeStrategy,
}
