import random
from constants import COOPERATE, DEFECT, POINTS

class RandomStrategy:

    def execute(self):
        return random.choice((COOPERATE, DEFECT))


    def reflect(self, opponent):
        pass

   ### 
    def __str__(self):
        return "random"

class AlwaysDefectStrategy:

    def execute(self):
        return DEFECT


    def reflect(self, opponent):
        pass

###
    def __str__(self):
        return "defect"


class AlwaysCooperateStrategy:
    
    def execute(self):
        return COOPERATE


    def reflect(self, opponent):
        pass

###
    def __str__(self):
        return "coop"


strategy_list = [RandomStrategy, AlwaysDefectStrategy, AlwaysCooperateStrategy]
