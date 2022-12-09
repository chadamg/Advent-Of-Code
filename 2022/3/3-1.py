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

rucksacks = []
for rucksack in input_file_cleaned:
  compartment1 = rucksack[:(len(rucksack)//2)]
  compartment2 = rucksack[(len(rucksack)//2):]
  rucksacks.append([compartment1, compartment2])

common_items = []
for [compartment1, compartment2] in rucksacks:
  dict1 = Counter(compartment1)
  dict2 = Counter(compartment2)
  commonDict = dict1 & dict2
  commonChars = set(commonDict.elements())
  common_items.append(''.join(commonChars))

item_priorities = []
for item in common_items:
  item_priority = priority_levels[item]
  item_priorities.append(item_priority)

print(sum(item_priorities))