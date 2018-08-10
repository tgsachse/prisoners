""""""

import heapq
import random
from strategies import STRATEGIES
from constants import COOPERATE, DEFECT, POINTS

class Simulation:
    """"""
    def __init__(self, player_count, generation_count, population_shift=5):
        """Initialize the simulation by creating all the players."""
        self.next_player_id = 0
        self.strategy_frequencies = self.__init_strategy_frequencies()
        self.players = self.__create_players(player_count)
        self.generation_count = generation_count
        self.population_shift = population_shift


    def __init_strategy_frequencies(self):
        frequencies = {}

        for strategy in STRATEGIES.keys():
            frequencies[strategy] = []

        return frequencies


    def __create_players(self, player_count):
        """Create all the players using an even distribution of strategies."""
        players = {}
        players_per_strategy = player_count / len(STRATEGIES)

        if players_per_strategy < 1:
            players_per_strategy = 1
        else:
            players_per_strategy = int(players_per_strategy)

        # Create a balanced number of players for each strategy.
        for name, Strategy in STRATEGIES.items():
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
            Strategy = random.choice(list(STRATEGIES.values()))
            players[self.next_player_id] = Player(self.next_player_id, Strategy())
            self.next_player_id += 1

        return players

    
    def __play_game(self, player1, player2):
        """Play the game between two players."""
        player1_result = player1.play(player2)
        player2_result = player2.play(player1)
        
        if player1_result == COOPERATE:
            if player2_result == COOPERATE:
                player1.update_points(POINTS["REWARD"], player2, COOPERATE)
                player2.update_points(POINTS["REWARD"], player1, COOPERATE)
            elif player2_result == DEFECT:
                player1.update_points(POINTS["SUCKER"], player2, DEFECT)
                player2.update_points(POINTS["TEMPTATION"], player1, COOPERATE)
        elif player1_result == DEFECT:
            if player2_result == COOPERATE:
                player1.update_points(POINTS["TEMPTATION"], player2, COOPERATE)
                player2.update_points(POINTS["SUCKER"], player1, DEFECT)
            elif player2_result == DEFECT:
                player1.update_points(POINTS["PUNISHMENT"], player2, DEFECT)
                player2.update_points(POINTS["PUNISHMENT"], player1, DEFECT)


    def __remove_weak_players(self):
        """Remove the weakest players from the simulation."""
        weakest_players = heapq.nsmallest(self.population_shift, self.players.values())

        for player in weakest_players:
            del self.players[player.identifier]
        

    def __replicate_strong_players(self):
        """Allow the strongest players to replicate in the simulation."""
        strongest_players = heapq.nlargest(self.population_shift, self.players.values())

        for player in strongest_players:
            Strategy = STRATEGIES[player.strategy.NAME]
            self.players[self.next_player_id] = Player(self.next_player_id,
                                                       Strategy())
            self.next_player_id += 1

    def __reset_player_points(self):
        """Reset the points for each player."""
        for player in self.players.values():
            player.reset_points()


    def single_generation(self):
        for player_id, player in self.players.items():
            other = random.choice(list(self.players.values()))
            while other == player:
                other = random.choice(list(self.players.values()))
            
            self.__play_game(player, other)

        self.__remove_weak_players()
        self.__replicate_strong_players()

        for category in self.strategy_frequencies.keys():
            self.strategy_frequencies[category].append(0)

        for player in self.players.values():
            self.strategy_frequencies[player.strategy.NAME][-1] += 1

        self.__reset_player_points()

    def run(self):
        """Run the simulation."""
        for generation in range(self.generation_count):
            self.single_generation()
        
        for category in self.strategy_frequencies.keys():
            print(category + ": ", end="")
            print(self.strategy_frequencies[category])


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


    def play(self, opponent):
        """Return the result of the player's strategy, when executed.'"""
        return self.strategy.execute(opponent)


    def update_points(self, points, opponent, opponent_action):
        """Update the player's points and reflect on the results.'"""
        self.points += points
        self.strategy.reflect(opponent, opponent_action)


    def reset_points(self):
        """Reset this player's points.'"""
        self.points = 0


simulation = Simulation(50, 100)
simulation.run()
