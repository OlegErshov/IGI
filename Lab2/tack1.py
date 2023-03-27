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

def get_average_length_of_sentences() -> int:
    f = open(os.path.join(os.getcwd(), "text.txt"), "r", encoding="utf-8")

    text = f.read()
    patern = r"(\w+|\d+)"
    match = re.findall(patern,text)

    not_word_pattern = r"(?<=\s)(\d+)(?=\s)"
    no_word_match = re.findall(not_word_pattern,text)

    no_word_length = 0
    for val in no_word_match:
        no_word_length += len(val)
    length = 0
    for val in match:
        length += len(val)
    return (length - no_word_length)/get_amount_of_sentences()


def get_average_length_of_words()->int:
    f = open(os.path.join(os.getcwd(), "text.txt"), "r", encoding="utf-8")

    text = f.read()
    patern = r"(\w+|\d+)"
    match = re.findall(patern,text)
    not_word_pattern = r"(?<=\s)(\d+)(?=\s)"
    no_word_match = re.findall(not_word_pattern,text)

    no_word_length = 0
    no_words_count = 0
    for val in no_word_match:
        no_word_length += len(val)
        no_words_count += 1
    
    length = 0
    words_count = 0
    for val in match:
        length += len(val)
        words_count += 1
    return (length - no_word_length) / (words_count - no_words_count)

