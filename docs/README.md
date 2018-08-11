# prisoners
This project simulated the Iterated Prisoner's Dilemma from Richard Dawkins's book *The Selfish Gene*. It was produced in a day
on a whim, and therefore is not particularly polished. It's still fun though!

The simulator has several behavioral strategies, all located in the [strategies.py](https://github.com/tgsachse/prisoners/blob/master/source/strategies.py)
file. Included strategies are as follows:
- Random
- Always Cooperate
- Always Defect
- Tit For Tat
- Grudger
- Exploiter
- Burn The Bridge

Descriptions for each strategy can be found in the strategies file.

# usage
To use, download with `git` and run the `run.sh` script. Use these commands:
```
git clone https://www.github.com/tgsachse/prisoners
cd prisoners
./run.sh
```
If you would like to adjust any of the simulation parameters, edit the constants located at the bottom of the
[game.py](https://github.com/tgsachse/prisoners/blob/master/source/game.py#L220) file.
