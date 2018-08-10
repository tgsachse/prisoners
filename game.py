import strategies
from constants import COOPERATE, DEFECT, POINTS

class Simulation:
    
    def __init__(self, player_count, generation_count):
        self.players = self.__create_players(player_count)
        print(len(self.players))
        print(self.players)

    def __create_players(self, player_count):
        strategy_count = len(strategies.strategy_list)
        players = {}

        if strategy_count > player_count:
            pass

        player_id = 0
        for Strategy in strategies.strategy_list:
            for player in range(int(player_count / strategy_count)):
                players[player_id] = Player(player_id, Strategy())
                player_id += 1

        return players


    def run(self):
        pass
        #p1p = self.players[1].play()
        #p2p = self.players[2].play()

        """
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
        """

class Player:
    
    def __init__(self, identifier, strategy):
        self.identifier = identifier
        self.strategy = strategy
        self.points = 0


    def play(self):
        return self.strategy.execute()


    def update_points(self, points, opponent):
        self.points += points
        self.strategy.reflect(opponent)


    def __repr__(self):
        return self.strategy.__str__()


simulation = Simulation(10, 100)
simulation.run()
simulation.run()
simulation.run()
simulation.run()
simulation.run()
