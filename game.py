import strategies
import random

COOPERATE = True
DEFECT = False

class Simulation:
    
    def __init__(self):
        self.players = {
            1 : Player(1, RandomStrategy()),
            2 : Player(2, RandomStrategy())
        }

        self.point_values = {
                "reward" : 3,
                "temptation" : 5,
                "sucker" : 0,
                "punishment" : 1,
                }
        
    def run(self):
        p1p = self.players[1].play()
        p2p = self.players[2].play()

        if p1p == COOPERATE:
            if p2p == COOPERATE:
                self.players[1].update_points(self.point_values["reward"], self.players[2])
                self.players[2].update_points(self.point_values["reward"], self.players[1])
            elif p2p == DEFECT:
                self.players[1].update_points(self.point_values["sucker"], self.players[2])
                self.players[2].update_points(self.point_values["temptation"], self.players[1])
        elif p1p == DEFECT:
            if p2p == COOPERATE:
                self.players[1].update_points(self.point_values["temptation"], self.players[2])
                self.players[2].update_points(self.point_values["sucker"], self.players[1])
            elif p2p == DEFECT:
                self.players[1].update_points(self.point_values["punishment"], self.players[2])
                self.players[2].update_points(self.point_values["punishment"], self.players[1])

        print("player 1 points: {}".format(self.players[1].points))
        print("player 2 points: {}".format(self.players[2].points))

class Player:
    
    def __init__(self, identifier, strategy):
        self.identifier = identifier
        self.strategy = strategy
        self.memory = {}
        self.points = 0


    def play(self):
        return self.strategy.execute()


    def update_points(self, points, opponent):
        self.points += points
        self.strategy.reflect(opponent)


class RandomStrategy:

    def __init__(self):
        self.memory = {}


    def execute(self):
        return random.choice((COOPERATE, DEFECT))


    def reflect(self, opponent):
        pass


simulation = Simulation()
simulation.run()
simulation.run()
simulation.run()
simulation.run()
simulation.run()
