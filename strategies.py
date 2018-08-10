import random
from constants import COOPERATE, DEFECT, POINTS

class RandomStrategy:

    def __init__(self):
        self.name = "RANDOM"


    def execute(self):
        return random.choice((COOPERATE, DEFECT))


    def reflect(self, opponent):
        pass

   ### 
    def __str__(self):
        return self.name

class AlwaysDefectStrategy:

    def __init__(self):
        self.name = "ALWAYS_DEFECT"
    

    def execute(self):
        return DEFECT


    def reflect(self, opponent):
        pass

###
    def __str__(self):
        return self.name


class AlwaysCooperateStrategy:
    
    def __init__(self):
        self.name = "ALWAYS_COOPERATE"
    
    
    def execute(self):
        return COOPERATE


    def reflect(self, opponent):
        pass

    def __str__(self):
        return self.name


strategy_dict = {
    "RANDOM" : RandomStrategy,
    "ALWAYS_DEFECT" : AlwaysDefectStrategy,
    "ALWAYS_COOPERATE" : AlwaysCooperateStrategy
}
