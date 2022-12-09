import os
from pathlib import Path


with open(os.path.join(Path(__file__).parent.absolute(), "input.txt"), "r") as f:
  input_file = f.read()

for i in range(0, len(input_file)+1):
  if i > 12:
    unique_sequence = input_file[i-13:i+1]
    if len(set(unique_sequence)) == len(unique_sequence):
      first_marker = i + 1
      break

print(first_marker)