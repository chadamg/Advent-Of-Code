import os
from pathlib import Path


with open(os.path.join(Path(__file__).parent.absolute(), "input.txt"), "r") as f:
  input_file = f.read()
input_file_cleaned = input_file.split("\n")

assignments_pairs = []
for assignments in input_file_cleaned:
  assignments1 = assignments.split(",")[0]
  assignments2 = assignments.split(",")[1]
  assignments_pairs.append([assignments1, assignments2])

assignments_ranges_pairs = []
for [assignments_pair1, assignments_pair2] in assignments_pairs:
  assignments_range1 = range(int(assignments_pair1.split("-")[0]), int(assignments_pair1.split("-")[1])+1)
  assignments_range2 = range(int(assignments_pair2.split("-")[0]), int(assignments_pair2.split("-")[1])+1)
  assignments_ranges_pairs.append([assignments_range1, assignments_range2])

def range_subset(range1, range2):
  if not range1:
      return True  # empty range is subset of anything
  if not range2:
      return False  # non-empty range can't be subset of empty range
  if len(range1) > 1 and range1.step % range2.step:
      return False  # must have a single value or integer multiple step
  return range1.start in range2 and range1[-1] in range2

range_subset_evaluations = []
for [assignments_range1, assignments_range2] in assignments_ranges_pairs:
  is_subset = range_subset(assignments_range1, assignments_range2) or range_subset(assignments_range2, assignments_range1)
  range_subset_evaluations.append(is_subset)

print(sum(range_subset_evaluations))