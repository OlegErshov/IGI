import re
import os
import json

class User:
    elements:set = set()
    username:str = str()

    def init(self):
        self.elements: set = set()
        self.username: str = str(input("Enter username: ")) 
        answer = str(input("Load data (Yes / No)?\n")) 
        if answer == "Yes": 
            self.load()
    
    def load(self):
        try: 
            file_stream = open( 
                os.path.join("data", self.username + ".json"), "r", encoding="utf8" 
            ) 
            self.elements = self.elements.union(set(json.load(file_stream))) 
        except FileNotFoundError: 
            pass 

    def save(self):
        with open(os.path.join("data", self.username + ".json"), "w", encoding="utf8") as fp: 
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