import re
import os


def print_text():
    """Prints the text in the file"""

    os.chdir(r"D:\BSUIR\IGI\lab2")
    f = open("text.txt", "r", encoding="utf-8")

    text = f.read()
    print(text)

def get_amount_of_sentences() -> int:
    """Get the amount of sentences"""

    os.chdir(r"D:\BSUIR\IGI\lab2")
    f = open("text.txt", "r", encoding="utf-8")

    text = f.read()
    pattern = r"(?<![A-Z\.])(?<!Mr)(\.+|\!+|\?+|\!\?|\?\!|\;)(?=\s[A-Z]+|\n|\t|\s*$)"
    match = re.findall(pattern, text)
    return len(match)

def get_amount_of_nondec_sentences_str(a) -> int:
    text = a
    pattern = r"(?<![A-Z\.])(?<!Mr)(\!+|\?+|\!\?|\?\!|\;)(?=\s[A-Z])"
    match = re.findall(pattern, text)
    return len(match)