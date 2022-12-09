from aoc import AdventOfCode
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
from pathlib import Path
import runpy


parser = ArgumentParser(description="Just an example", formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("year", help="Specify which AOC year")
parser.add_argument("day", help="Specify which AOC day within the specified year")
parser.add_argument("level", help="1 or 2 (Corresponds to part 1 or 2 of question)")
parser.add_argument("-a", "-answer", action="store_true", help="Submit answer for the level (question part) specified")
args = parser.parse_args()

advent_of_code = AdventOfCode(year=args.year, day=args.day)
answer_file = f"{args.day}-{args.level}"
file_path = os.path.join(Path(__file__).parent.absolute(), args.year, args.day, answer_file)
runpy.run_path(path_name=file_path)
# import importlib.util
# import sys
# spec = importlib.util.spec_from_file_location("module.name", "/path/to/file.py")
# foo = importlib.util.module_from_spec(spec)
# sys.modules["module.name"] = foo
# spec.loader.exec_module(foo)
# foo.MyClass()

if args.answer:
  advent_of_code.submit_answer(args.level)

# import sys

# sys.path.insert(0, '/Users/adam/Downloads/Advent Of Code')

# from aoc import AdventOfCode

# day4 = AdventOfCode("2022", "5")
# day4.api.post_answer(part, answer)