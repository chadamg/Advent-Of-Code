import os
from pathlib import Path


with open(os.path.join(Path(__file__).parent.absolute(), "input.txt"), "r") as f:
  input_file = f.read()
input_file_cleaned = input_file.split("\n\n")

container_arrangement = input_file_cleaned[0].split("\n")
instructions = [line.split(" ") for line in input_file_cleaned[1].split("\n")]

containers = {k:[] for k in container_arrangement[-1].split(" ") if k.strip()}
for k, v in containers.items():
  i = container_arrangement[-1].find(k)
  for line in container_arrangement:
    if line[i] not in [k, " "]:
      v.append(line[i])

for i, instruction in enumerate(instructions):
  quantity = int(instruction[1])
  from_col = instruction[3]
  to_col = instruction[5]
  containers[to_col][0:0] = reversed(containers[from_col][:quantity])
  del containers[from_col][:quantity]

answer = "".join([container[0] for container in containers.values()])
print(answer)