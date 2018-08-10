""""""

import random
from strategies import strategy_list
from constants import COOPERATE, DEFECT, POINTS

class Simulation:
    """"""
    
    def __init__(self, player_count, generation_count):
        """Initialize the simulation by creating all the players."""

        self.players = self.__create_players(player_count)
        self.generation_count = generation_count
        print(self.players)


    def __create_players(self, player_count):
        """Create all the players using an even distribution of strategies."""

        players = {}
        players_per_strategy = player_count / len(strategy_list)

        if players_per_strategy < 1:
            players_per_strategy = 1
        else:
            players_per_strategy = int(players_per_strategy)

        # Create a balanced number of players for each strategy.
        for strategy_number, Strategy in enumerate(strategy_list):
            if len(players) >= player_count:
                break

            for player_number in range(0, players_per_strategy):

                # Calculate the appropriate ID number for each player based
                # on the current progress of the function. IDs are
                # ascending integers.
                player_id = player_number + (players_per_strategy * strategy_number)
                players[player_id] = Player(player_id, Strategy())

        # If the number of strategies did not divide the number of players
        # evenly, resulting in an incorrect number of players, then add more
        # players with randomly selected strategies until the correct number
        # of players is reached.
        while len(players) < player_count:
            players[len(players)] = Player(len(players),
                                           random.choice(strategy_list)())
        return players


    def run(self):
        """"""
        pass

class Player:
    """"""
    
    def __init__(self, identifier, strategy):
        """Initialize the player with a provided strategy and ID."""

        self.identifier = identifier
        self.strategy = strategy
        self.points = 0


    def play(self):
        """Return the result of the player's strategy, when executed.'"""

        return self.strategy.execute()


    def update_points(self, points, opponent):
        """Update the player's points and reflect on the results.'"""

        self.points += points
        self.strategy.reflect(opponent)

    ###
    def __repr__(self):
        return self.strategy.__str__()


simulation = Simulation(2, 100)
simulation.run()
simulation.run()
simulation.run()
simulation.run()
simulation.run()
