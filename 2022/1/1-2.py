import os
from pathlib import Path


with open(os.path.join(Path(__file__).parent.absolute(), "input.txt"), "r") as f:
  input_file = f.read()
calorie_groups = input_file.split("\n\n")
all_calorie_group_sums = []

for calorie_group in calorie_groups:
  calorie_group_cleaned = calorie_group.split("\n")
  sum_of_calorie_group = sum([int(i) for i in calorie_group_cleaned if type(i) == int or i.isdigit()])
  all_calorie_group_sums.append(sum_of_calorie_group)

print(sum(sorted(all_calorie_group_sums, reverse=True)[0:3]))