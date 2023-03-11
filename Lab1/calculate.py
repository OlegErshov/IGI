from constants import OPERATIONS


def calculate(op, a, b):
    return OPERATIONS[op](a, b)