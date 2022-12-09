from collections import Counter
import os
from pathlib import Path


with open(os.path.join(Path(__file__).parent.absolute(), "input.txt"), "r") as f:
  input_file = f.read()
input_file_cleaned = input_file.split("\n")

var = "a"
priority_levels={chr(ord(var)+i): i + 1 for i in range(26)}
var='A'
priority_levels.update({chr(ord(var)+i): i + 27 for i in range(26)})

def divide_chunks(l, n):
  for i in range(0, len(l), n):
    yield l[i:i + n]

rucksack_groups = list(divide_chunks(input_file_cleaned, 3))

common_badge_items = []
for [rucksack1, rucksack2, rucksack3] in rucksack_groups:
  dict1 = Counter(rucksack1)
  dict2 = Counter(rucksack2)
  dict3 = Counter(rucksack3)
  commonDict = dict1 & dict2 & dict3
  commonChars = set(commonDict.elements())
  common_badge_items.append(''.join(commonChars))

badge_item_priorities = []
for item in common_badge_items:
  item_priority = priority_levels[item]
  badge_item_priorities.append(item_priority)

print(sum(badge_item_priorities))