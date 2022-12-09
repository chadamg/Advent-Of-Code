import os
from pathlib import Path


with open(os.path.join(Path(__file__).parent.absolute(), "input.txt"), "r") as f:
  input_file = f.read()
input_file_cleaned = input_file.split("\n")

total_size = 0
current_directory_size = 0

for i, line in enumerate(input_file_cleaned):
  words = line.split()
  if words[0].isdigit():
    try:
      if not input_file_cleaned[i+1].split()[0].isdigit():
        if not current_directory_size > 100000:
          total_size += current_directory_size
        current_directory_size = 0
      else:
        current_directory_size += int(words[0])
    except IndexError:
      current_directory_size += int(words[0])
      if not current_directory_size > 100000:
        total_size += current_directory_size

print(total_size)