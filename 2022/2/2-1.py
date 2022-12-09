from functools import reduce
import os
from pathlib import Path


with open(os.path.join(Path(__file__).parent.absolute(), "input.txt"), "r") as f:
  input_file = f.read()
input_file_cleaned = input_file.split("\n")

opponent_moves = {"A": "Rock", "B": "Paper", "C": "Scissors"}
player_moves = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
points_per_shape = {"Rock": 1, "Paper": 2, "Scissors": 3}

points_per_outcome = {
  "Rock": {
    "Rock": 3,
    "Paper": 0,
    "Scissors": 6,
  },
  "Paper": {
    "Rock": 6,
    "Paper": 3,
    "Scissors": 0,
  },
  "Scissors": {
    "Rock": 0,
    "Paper": 6,
    "Scissors": 3,
  }}
player_scores = []

for strategy_guide in input_file_cleaned:
  strategy_guide_cleaned = strategy_guide.split(" ")
  opponent = strategy_guide_cleaned[0]
  player = strategy_guide_cleaned[1]
  opponent_move = opponent_moves[opponent]
  player_move = player_moves[player]
  
  player_shape_points = points_per_shape[player_move]
  player_outcome_points = points_per_outcome[player_move][opponent_move]
  player_scores.append([player_shape_points, player_outcome_points])

print(sum([reduce(lambda x,y: x+y, outcome) for outcome in player_scores]))