"""A simulator for the Iterated Prisoner's Dilemma.

This was inspired by Richard Dawkins's discussion of the nature
game in his book, The Selfish Gene.

By Tiger Sachse.
"""

import heapq
import random
from strategies import STRATEGIES
from constants import COOPERATE, DEFECT, POINTS

class Simulation:
    """The simulator containing all necessary functions."""
    def __init__(self,
                 player_count,
                 generation_count,
                 interaction_count,
                 population_shift):
        """Initialize the simulation by creating all the players."""
        self.next_player_id = 0
        self.strategy_frequencies = self.__init_strategy_frequencies()
        self.players = self.__create_players(player_count)
        self.generation_count = generation_count
        self.population_shift = population_shift
        self.interaction_count = interaction_count


    def __init_strategy_frequencies(self):
        """Create a dictionary to track the frequencies of strategies."""
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
                player1.update(POINTS["REWARD"], player2, COOPERATE)
                player2.update(POINTS["REWARD"], player1, COOPERATE)
            elif player2_result == DEFECT:
                player1.update(POINTS["SUCKER"], player2, DEFECT)
                player2.update(POINTS["TEMPTATION"], player1, COOPERATE)
        elif player1_result == DEFECT:
            if player2_result == COOPERATE:
                player1.update(POINTS["TEMPTATION"], player2, COOPERATE)
                player2.update(POINTS["SUCKER"], player1, DEFECT)
            elif player2_result == DEFECT:
                player1.update(POINTS["PUNISHMENT"], player2, DEFECT)
                player2.update(POINTS["PUNISHMENT"], player1, DEFECT)


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


    def __reset_players(self):
        """Reset each player for the next generation."""
        for player in self.players.values():
            player.reset()


    def single_generation(self):
        """Run a single generation of the simulation."""
        self.__reset_players()
        for player_id, player in self.players.items():
            
            # For each player, execute multiple interactions with
            # other players.
            for interaction in range(self.interaction_count):
                other = random.choice(list(self.players.values()))
                while other == player:
                    other = random.choice(list(self.players.values()))
                
                self.__play_game(player, other)
        
        # Remove the weak and replicate the strong.
        self.__remove_weak_players()
        self.__replicate_strong_players()

        # Add a new generation for each strategy in the frequencies dictionary.
        for category in self.strategy_frequencies.keys():
            self.strategy_frequencies[category].append(0)

        # Count the frequencies of each strategy for this generation.
        for player in self.players.values():
            self.strategy_frequencies[player.strategy.NAME][-1] += 1


    def run(self, loud=True):
        """Run the simulation."""
        if loud:
            print("Welcome to the Iterated Prisoner's Dilemma.")
            print("Create by Tiger Sachse.\n")
            print("Running", end="", flush=True)

        for generation in range(self.generation_count):
            if loud:
                print(".", end="", flush=True)
            self.single_generation()

        if loud:
            print("\nDone!\n")

    
    def print_results(self):
        """Print the results of the simulation."""
        print("Results:")
        for category in self.strategy_frequencies.keys():
            print(category + ":")
            for generation, count in enumerate(self.strategy_frequencies[category], 1):
                line = "gen {0: >3}, count {1: <3} | {2}"
                print(line.format(generation, count, "X" * count))
            print()


class Player:
    """A player, who possesses a strategy for the game."""
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
        """Return the result of the player's strategy, when executed."""
        return self.strategy.execute(opponent)


    def update(self, points, opponent, opponent_action):
        """Update the player's points and reflect on the results."""
        self.points += points
        self.strategy.reflect(opponent, opponent_action)


    def reset(self):
        """Reset this player."""
        self.points = 0
        self.strategy.reset()


# Beginning of the program.
if __name__ == "__main__":

    # Change these constants to tinker with the simulation.
    PLAYERS = 50
    GENERATIONS = 50
    TURNOVER_MULTIPLIER = 10
    INTERACTION_MULTIPLIER = 100

    # Create and run the simulation.
    simulation = Simulation(PLAYERS,
                            GENERATIONS,
                            PLAYERS * INTERACTION_MULTIPLIER,
                            PLAYERS // TURNOVER_MULTIPLIER)
    simulation.run()
    simulation.print_results()
