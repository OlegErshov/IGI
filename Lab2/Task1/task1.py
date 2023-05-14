import re
import os
from collections import Counter

def print_text():
    

    os.chdir(r"/home/oleg/BSUIR/IGI/Lab2")
    f = open("text.txt", "r", encoding="utf-8")

    text = f.read()
    print(text)

def read_from_file(path = "home/oleg/BSUIR/IGI/Lab2/Task1"):

    os.chdir(path)
    f = open("text.txt", "r", encoding="utf-8")
    text = f.read()
    return text

def find_length_of_something(str,text):
    pattern = re.compile(str)
    match = re.findall(pattern, text)
    return len(match)

def find_list_of_comething(str,text):
    pattern = re.compile(str)
    match = re.findall(pattern, text)
    return match

def is_input_valid(input :str):
    pattern = r"([A-Za-z]+|\d+|\s+|\!+|\?+|\.+|;|_|'|\"|-)"
    match = re.findall(pattern,input)
    length = 0
    for el in match:
        length += len(el)
    a = len(input)
    if len(input) != length:
        return False
    return True

def get_amount_of_sentences() -> int:
 
    text = read_from_file()
    return find_length_of_something("(?<![A-Z\.])(?<!Mr)(?<!Mrs)(?<!Dr)(\.+|\!+|\?+|\!\?|\?\!|\;)(?=\s[A-Z]+|\n|\t|\s*$)",text)
  
def get_amount_of_sentences_from_string(st) -> int:
    text = str(st)
    return find_length_of_something("(?<![A-Z\.])(?<!Mr)(?<!Mrs)(?<!Dr)(\.+|\!+|\?+|\!\?|\?\!|\;)(?=\s[A-Z]+|\n|\t|\s*$)",text)
    

def get_amount_of_nondec_sentences_str(a) -> int:
    text = a
    pattern = r"(?<![A-Z\.])(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Mss)(\!+|\?+|\!\?|\?\!|\;)(?=$|\s[A-Z])"
    match = re.findall(pattern, text)
    return len(match)

def get_amount_of_nondec_sentences() -> int:
   
    text = read_from_file()
    return find_length_of_something("(?<![A-Z\.])(?<!Mr)(\!\?|\?\!|\;)(?=\s[A-Z])",text)
  

def get_average_length_of_sentences() -> int:

    text = read_from_file()
    words = find_list_of_comething("[\w']+",text)
    no_words = find_list_of_comething("(?<=\s)(\d+)(?=\s)",text)
   
    no_word_length = 0
    for val in no_words:
        no_word_length += len(val)
    length = 0
    for val in words:
        length += len(val)
    if length - no_word_length == 0:
        return "eroor"
    return (length - no_word_length)/get_amount_of_sentences_from_string(text)

def get_average_len_of_sentences_str(a) -> int:
    text = a
   
    words = find_list_of_comething("[\w']+",text)
    no_words = find_list_of_comething("(?<=\s)(\d+)(?=\s|\.|\!|\?|;)",text)

    no_word_length = 0
    for val in no_words:
        no_word_length += len(val)
    length = 0
    for val in words:
        length += len(val)
    return round((length - no_word_length)/get_amount_of_sentences_from_string(text),2)


def get_average_length_of_words()->int:

    text = read_from_file()

    words = find_list_of_comething("(\w+|'+)",text)
    no_words = find_list_of_comething("(?<=\s)(\d+)(?=\s)",text)

    no_word_length = 0
    no_words_count = 0
    for val in no_words:
        no_word_length += len(val)
        no_words_count += 1
    
    length = 0
    words_count = 0
    for val in words:
        length += len(val)
        words_count += 1
    return (length - no_word_length) / (words_count - no_words_count)

def get_average_length_of_words_str(a)->int:
    text = a
    words = find_list_of_comething("[\w']+",text)
    no_words = find_list_of_comething("(?<=\s)(\d+)(?=\s)",text)

    no_word_length = 0
    no_words_count = 0
    for val in no_words:
        no_word_length += len(val)
        no_words_count += 1
    
    length = 0
    words_count = 0
    for val in words:
        length += len(val)
        words_count += 1
    return int((length - no_word_length) * 100 / (words_count - no_words_count)) / 100

def get_top_K_repeated_N_grams(text, k=10, n=4):
    patern = r"[\w']+"
    match = re.findall(patern,text)

    not_word_pattern = r"(?<=\s)(\d+)(?=\s)"
    no_word_match = re.findall(not_word_pattern,text)
    
    
    for elem in match:
        for item in no_word_match:
            if(elem == item):
                match.remove(elem)


   
    n_gramms = {}
    n_gramm = ""

    for i in range(0, int(len(match)) - int(n)):

        for j in range(0, int(n)):
            n_gramm +=  match[i + j] + " "
        n_gramm = n_gramm[0:len(n_gramm)-1]

        if n_gramm in n_gramms:
            n_gramms[n_gramm] += 1
        else:
            n_gramms[n_gramm] = 1
        n_gramm = ""

    sorted_n_gramms = list(sorted(n_gramms.items(), key=lambda x: x[1], reverse=True))

    return sorted_n_gramms[:k]

text = "Hi, Mr.Tom. Goodbye, Dr.Strange 4114234. Ye no't!"

print(get_average_len_of_sentences_str("Hi, Mr.Tom. Goodbye, Dr.Strange 4114234. Ye no't!"))
#print(get_top_K_repeated_N_grams(text,13,2))
#print(get_average_length_of_words_str(text))
#print(get_amount_of_sentences_from_string(text))
#print(is_input_valid(text))
