import json
import os
from pathlib import Path
import requests
from settings import SESSION_COOKIE


class AdventOfCodeAPI:
  base_url = "https://adventofcode.com"
  cookies = {"session": SESSION_COOKIE}

  def __init__(self, year, day):
    self.year = year
    self.day = day
  
  def fetch_input(self) -> str:
    try:
      url = f"{self.base_url}/{self.year}/day/{self.day}/input"
      response = requests.get(url, cookies=self.cookies)
      input = response.text.rstrip()
      return input
    except Exception as e:
      print(e)
  
  def post_answer(self, level: int, answer) -> str:
    try:
      url = f"{self.base_url}/{self.year}/day/{self.day}/answer"
      data = {"answer": answer, "level": level, "MIME Type": "application/x-www-form-urlencoded"}
      response = requests.post(url, data=data, cookies=self.cookies)
      content = response.content.decode()
      return content
    except Exception as e:
      print(e)


class AdventOfCode:
  root_path = Path(__file__).parent.absolute()

  def __init__(self, year, day):
    self.year = year
    self.day = day
    self.api = AdventOfCodeAPI(self.year, self.day)

  def create_folder(self) -> None:
    path = os.path.join(self.root_path, self.year, self.day)
    try:
      Path(path).mkdir(parents=True)
      print(f"Folder '{path}' created")
    except FileExistsError:
      print(f"Folder '{path}' already exists")
    
  def create_file(self, path: str) -> None:
    file_path = path
    try:
      f = open(file_path, "x")
      f.close()
      print(f"File '{f.name}' created")
    except FileExistsError:
      print(f"File '{file_path}' already exists")
  
  def write_file(self, path: str, content: str) -> None:
    try:
      with open(path, "w") as f:
        f.write(content)
        f.close()
      print(f"File '{f.name}' written")
    except Exception as e:
      print(e)

  def file_exists(self, path: str) -> bool:
    try:
      file_path = path
      f = open(file_path, "r")
      f.close()
      print(f"File '{f.name}' already exists")
      return True
    except OSError:
      return False
    
  def create_answer_files(self) -> None:
    try:
      path = os.path.join(self.root_path, self.year, self.day)
      for i in range(1, 3):
        filename = f"{self.day}-{i}.py"
        file_path = os.path.join(path, filename)
        if not self.file_exists(file_path):
          self.create_file(file_path)
    except Exception as e:
      print(e)
    
  def download_input_file(self) -> None:
    try:
      path = os.path.join(self.root_path, self.year, self.day)
      filename = "input.txt"
      file_path = os.path.join(path, filename)
      if not self.file_exists(file_path):
        self.create_file(file_path)
        input = self.api.fetch_input()
        self.write_file(file_path, input)
    except Exception as e:
      print(e)
    
  def get_star_count(self) -> int:
    try:
      file_path = os.path.join(self.root_path, self.year, "star_count.json")
      f = open(file_path)
      data = json.load(f)
      star_count = data["star_count"]
      return star_count
    except Exception as e:
      print(e)
    
  def update_star_count(self, star_count) -> None:
    try:
      file_path = os.path.join(self.root_path, self.year, "star_count.json")
      f = open(file_path)
      data = json.load(f)
      print(f"Updated star count from {data['star_count']}* to {star_count}*")
      data["star_count"] = star_count
      with open(file_path, "w") as f:
        json.dump(data, f)
    except Exception as e:
      print(e)
    
  def answer_exists(self, level) -> bool:
    try:
      file_path = os.path.join(self.root_path, self.year, "star_count.json")
      f = open(file_path)
      data = json.load(f)
      if self.day in data["answers"]:
        if str(level) in data["answers"][self.day]:
          print(f"Answer for question {self.day} part {level} already exists")
          return True
        else:
          return False
      else:
        return False
    except Exception as e:
      print(e)
    
  def update_answers(self, level, answer) -> None:
    try:
      file_path = os.path.join(self.root_path, self.year, "star_count.json")
      f = open(file_path)
      data = json.load(f)
      data["answers"][self.day].update({level: answer})
      with open(file_path, "w") as f:
        json.dump(data, f)
    except Exception as e:
      print(e)
  
  def find_star_count(self, content: str) -> int:
    try:
      index = content.find("star-count")
      star_count = content[index+len("star-count")+2:index+len("star-count")+4]
      star_count = int(star_count.strip("*"))
      return star_count
    except Exception as e:
      print(e)
  
  def submit_answer(self, level) -> None:
    try:
      if not self.answer_exists(level):
        file_path = os.path.join(self.root_path, self.year, "star_count.json")
        f = open(file_path)
        data = json.load(f)
        
        # if self.day in data["answers"]:
        #   if str(level) in data["answers"][self.day]:
        #     if answer == data["answers"][self.day][str(level)]:
        #       print(f"Question {self.day} part {level} already correctly answered with '{answer}'. Star count: {data['star_count']}*")
        # else:
        content = self.api.post_answer(level, answer)
        star_count = self.find_star_count(content)
        
        if star_count > data["star_count"]:
          print(f"'{answer}' was the correct answer. Star count: {star_count}*")
        else:
          print(f"'{answer}' was incorrect. Try again in 1 minute. Star count: {star_count}*")
    except Exception as e:
      print(e)