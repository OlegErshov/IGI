import re
import os
import json

class User:
    elements:set = set()
    username:str = str()

    def __init__(self):
        try:
            self.elements: set = set()
            self.username: str = str(input("Enter username: ")) 
            answer = str(input("Load data (Yes / No)?\n")) 

            if answer == "Yes": 
                self.load()

        except EOFError:
            print("Eror")
       
    
    def load(self)->None:
        try: 
            with open(os.path.join("/home/oleg/BSUIR/IGI/Lab2/Task2/data", self.username + ".json"), 'r') as file_stream:
                self.elements = self.elements.union(set(json.load(file_stream)))
            # file_stream = open( 
            #     os.path.join("./Task2/data", self.username + ".json"), "r", encoding="utf8"
            # ) 
            # self.elements = self.elements.union(set(json.load(file_stream))) 
        except FileNotFoundError: 
            pass 

    def save(self)->None:
        with open(os.path.join("/home/oleg/BSUIR/IGI/Lab2/Task2/data", self.username + ".json"), "w", encoding="utf8") as fp: 
            json.dump(list(self.elements), fp) 
    
    def add(self,obj):
        self.elements.add(obj)

    def remove(self,obj):
        try: 
            self.elements.remove(obj) 
        except KeyError: 
            pass 

    def exists(self,objects: list):
        found_any = False 
        for obj in objects: 
            if len(obj) == 0: 
                continue 
            if set(obj).issubset(self.elements): 
                print(f"{obj} - exists") 
                found_any = True 
        if not found_any: 
            print("No such elements") 

    def grep(self,expression: str) -> None:
        found_any = False 
        for value in self.elements: 
            if len(value) == 0: 
                continue 
            if re.fullmatch(expression, str(value)) is not None: 
                print(f"{value} - matches the expression") 
                found_any = True 
        if not found_any: 
            print("No such elements")