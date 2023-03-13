from calculate import calculate
from constants import OPERATIONS
from even_numbers import find_even

print("Hello world!")

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    
except:
    print("Please, enter correct numbers")


while True:
    try:
        supported_operations = ", ".join(list(OPERATIONS.keys()))
        operation = input(f"Enter operation ({supported_operations}): ")
    except:
        print("WTF")
    #if operation not in OPERATIONS:
     #   print("This operation is not supported")
    #else:
    break
    

try:
    print(calculate(operation, first_number, second_number))
except ZeroDivisionError:
    print("Yod devided by zero :)")


while True:
    try:
        numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        break
    except:
        print("Invalid input")

even_numbers = find_even(numbers)
print(f"even numbers: {even_numbers}")