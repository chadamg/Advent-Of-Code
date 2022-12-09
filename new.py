from aoc import AdventOfCode
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


parser = ArgumentParser(description="Just an example", formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("year", help="Find or create folder for the year specified")
parser.add_argument("day", help="Find or create folder for the day specified")
args = parser.parse_args()

advent_of_code = AdventOfCode(year=args.year, day=args.day)
advent_of_code.create_folder()
advent_of_code.create_answer_files()
advent_of_code.download_input_file()