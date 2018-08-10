""""""

import heapq
import random
from strategies import strategy_dict
from constants import COOPERATE, DEFECT, POINTS

class Simulation:
    """"""
    
    def __init__(self, player_count, generation_count, population_shift=5):
        """Initialize the simulation by creating all the players."""
        
        self.next_player_id = 0
        self.players = self.__create_players(player_count)
        self.generation_count = generation_count
        self.population_shift = population_shift


    def __create_players(self, player_count):
        """Create all the players using an even distribution of strategies."""

        players = {}
        players_per_strategy = player_count / len(strategy_dict)

        if players_per_strategy < 1:
            players_per_strategy = 1
        else:
            players_per_strategy = int(players_per_strategy)

        # Create a balanced number of players for each strategy.
        for name, Strategy in strategy_dict.items():
            if len(players) >= player_count:
                break

            for player_number in range(0, players_per_strategy):
                players[self.next_player_id] = Player(self.next_player_id, Strategy())
                self.next_player_id += 1

        # If the number of strategies did not divide the number of players
        # evenly, resulting in an incorrect number of players, then add more
        # players with randomly selected strategies until the correct number
        # of players is reached.
        while len(players) < player_count:
            Strategy = random.choice(list(strategy_dict.values()))
            players[self.next_player_id] = Player(self.next_player_id, Strategy())
            self.next_player_id += 1

        return players

    
    def __play_game(self, player1, player2):
        """Play the game between two players."""

        player1_result = player1.play()
        player2_result = player2.play()
        
        if player1_result == COOPERATE:
            if player2_result == COOPERATE:
                player1.update_points(POINTS["REWARD"], player2)
                player2.update_points(POINTS["REWARD"], player1)
            elif player2_result == DEFECT:
                player1.update_points(POINTS["SUCKER"], player2)
                player2.update_points(POINTS["TEMPTATION"], player1)
        elif player1_result == DEFECT:
            if player2_result == COOPERATE:
                player1.update_points(POINTS["TEMPTATION"], player2)
                player2.update_points(POINTS["SUCKER"], player1)
            elif player2_result == DEFECT:
                player1.update_points(POINTS["PUNISHMENT"], player2)
                player2.update_points(POINTS["PUNISHMENT"], player1)


    def __remove_weak_players(self):
        """Remove the weakest players from the simulation."""

        weakest_players = heapq.nsmallest(self.population_shift, self.players.values())

        for player in weakest_players:
            del self.players[player.identifier]
        

    def __replicate_strong_players(self):
        """Allow the strongest players to replicate in the simulation."""

        strongest_players = heapq.nlargest(self.population_shift, self.players.values())

        for player in strongest_players:
            Strategy = strategy_dict[player.strategy.name]
            self.players[self.next_player_id] = Player(self.next_player_id,
                                                       Strategy())
            self.next_player_id += 1

    def __reset_player_points(self):
        """Reset the points for each player."""

        for player in self.players.values():
            player.reset_points()

    def run(self):
        """Run the simulation."""

        for player_id, player in self.players.items():
            other = random.choice(list(self.players.values()))
            while other == player:
                other = random.choice(list(self.players.values()))
            
            self.__play_game(player, other)

        self.__remove_weak_players()
        self.__replicate_strong_players()
        self.__reset_player_points()

        print(self.players)

class Player:
    """"""
    
    def __init__(self, identifier, strategy):
        """Initialize the player with a provided strategy and ID."""

        self.identifier = identifier
        self.strategy = strategy
        self.points = 0


    def __gt__(self, other):
        """Greater than comparison to another player."""

        return self.points > other.points


    def __lt__(self, other):
        """Less than comparison to another player."""

        return self.points < other.points


    def __ge__(self, other):
        """Greater than or equal to comparison to another player."""

        return self.points >= other.points


    def __le__(self, other):
        """Less than or equal to comparison to another player."""

        return self.points <= other.points


    def play(self):
        """Return the result of the player's strategy, when executed.'"""

        return self.strategy.execute()


    def update_points(self, points, opponent):
        """Update the player's points and reflect on the results.'"""

        self.points += points
        self.strategy.reflect(opponent)


    def reset_points(self):
        self.points = 0


    ###
    def __repr__(self):
        return str(self.points) + " " + self.strategy.__str__()


simulation = Simulation(10, 100)
simulation.run()
simulation.run()
simulation.run()
simulation.run()
