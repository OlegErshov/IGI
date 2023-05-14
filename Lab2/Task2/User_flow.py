import sys 
  
from task2 import User
  
  
def main() -> None: 
     
    user: User =  User() 
    #user.init()
    try: 
        while True: 
            commands = input("Enter next command:\n").split(" ") 
            match commands[0]: 
                case "add": 
                    for value in commands[1:]: 
                        if len(value) == 0: 
                            continue 
                        user.add(value) 
                case "remove": 
                    for value in commands[1:]: 
                        if len(value) == 0: 
                            continue 
                        user.remove(value) 
                case "find": 
                    user.exists(commands[1:]) 
                case "list": 
                    print(user.elements) 
                case "grep": 
                    user.grep(commands[1]) 
                case "save": 
                    user.save() 
                case "load": 
                    user.load() 
                case "exit":
                    return
                case "switch": 
                    answer = str(input("Save data (Yes / No)?\n")) 
                    if answer == "Yes": 
                        user.save() 
                    user = User() 
                    #user.init()
    except KeyboardInterrupt: 
        answer = str(input("Save data (Yes / No)?\n")) 
        if answer == "Yes": 
            user.save() 
        sys.exit(0) 
  
  
if __name__ == '__main__':
    main()