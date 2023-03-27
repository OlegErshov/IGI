import re
import os
from collections import Counter

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

def get_amount_of_sentences_from_string(st) -> int:
    text = str(st)
    pattern = r"(?<![A-Z\.])(?<!Mr)(\.+|\!+|\?+|\!\?|\?\!|\;)(?=\s[A-Z]+|\n|\t|\s*$)"
    match = re.findall(pattern, text)
    return len(match)

def get_amount_of_nondec_sentences_str(a) -> int:
    text = a
    pattern = r"(?<![A-Z\.])(?<!Mr)(\!+|\?+|\!\?|\?\!|\;)(?=\s[A-Z])"
    match = re.findall(pattern, text)
    return len(match)

def get_amount_of_nondec_sentences() -> int:
    """Get the amount of non-declarative sentences

    Declarative sentence is a sentence ending with '.' or '...' separators."""

    f = open(os.path.join(os.getcwd(), "text.txt"), "r", encoding="utf-8")

    text = f.read()
    pattern = r"(?<![A-Z\.])(?<!Mr)(\.+|\!\?|\?\!|\;)(?=\s[A-Z])"
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

def get_average_len_of_sentences_str(a) -> int:
    text = a
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

def get_average_length_of_words_str(a)->int:
    text = a
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
    return int((length - no_word_length) * 100 / (words_count - no_words_count)) / 100

def get_top_K_repeated_N_grams(text, k=10, n=4):
    sentences = get_amount_of_sentences_from_string(text)

    patern = r"(\w+|\d+)"
    match = re.findall(patern,text)

    not_word_pattern = r"(?<=\s)(\d+)(?=\s)"
    no_word_match = re.findall(not_word_pattern,text)
    
    all_words = match - no_word_match
    
    words_by_sentence = [all_words.findall(
        sent) for sent in sentences]

    n_grams = []
    for words in words_by_sentence:
        n_grams.extend(list(zip(*[words[i:] for i in range(n)])))

    counter = Counter()

    for n_gram in n_grams:
        counter[' '.join(n_gram)] += 1

    return dict(counter.most_common(k))
