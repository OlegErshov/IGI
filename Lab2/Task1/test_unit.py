import unittest

from task1 import get_amount_of_sentences_from_string
from task1 import get_average_len_of_sentences_str
from task1 import get_average_length_of_words_str
from task1 import get_amount_of_nondec_sentences_str
from task1 import get_top_K_repeated_N_grams
from task1 import is_input_valid

class TestCalculator(unittest.TestCase):

    def test_count_of_sentences(self):
      test = "abc abc abc. Oleza. Tima. Serega."
      self.assertEqual(get_amount_of_sentences_from_string(test),4)

    def test_count_of_sentences2(self):
      test = "abc abc... abc. Oleza!? Tima?! Serega."
      self.assertEqual(get_amount_of_sentences_from_string(test),4)

    def test_count_of_sentences3(self):
      test = "abc. Abc. Abc. I doesnt read this book! How about that?"
      self.assertEqual(get_amount_of_sentences_from_string(test),5)

    def test_count_of_sentences4(self):
      test = "abc abc abc abc olololololol abc!!!!! Mr. Anderson?! Ya... No, i am not."
      self.assertEqual(get_amount_of_sentences_from_string(test),4)



    def test_get_amount_of_non_declarative_sentences_0(self):
      text = ''
      assert get_amount_of_nondec_sentences_str(text) == 0


    def test_get_amount_of_non_declarative_sentences_1(self):
        text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?!'
        assert get_amount_of_nondec_sentences_str(text) == 1


    def test_get_amount_of_non_declarative_sentences_2(self):
        text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?! Blabla, "Qwe!"'
        assert get_amount_of_nondec_sentences_str(text) == 1


    def test_get_amount_of_non_declarative_sentences_3(self):
        text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?!'
        assert get_amount_of_nondec_sentences_str(text) == 1


    def test_get_amount_of_non_declarative_sentences_3(self):
        text = 'Hi, Mr. Tom. Goodbye, Mrs. Smith?! Some text... Some text!'
        assert get_amount_of_nondec_sentences_str(text) == 2


    def test_get_amount_of_non_declarative_sentences_4(self):
        text = 'Some text; some text...'
        assert get_amount_of_nondec_sentences_str(text) == 0


    def test_get_amount_of_non_declarative_sentences_5(self):
        text = 'Some text; some text... Some text!!!'
        assert get_amount_of_nondec_sentences_str(text) == 1
          
#
#
#
#

    def test_average_len_of_words1(self):
       test = "a1a2 1123 a1 O.B.R. Mr.Jone!!! Hi, im Batman"
       self.assertEqual(get_average_length_of_words_str(test),2.5)

    def test_average_len_of_words2(self):
       test = "abc abc abc abc olololololol abc!!!!! Mr. Anderson?! Ya... No, i am not."
       self.assertEqual(get_average_length_of_words_str(test),3.61)

    def test_average_len_of_words3(self):
       test = "abc abc abc abc 123 olololololol 321 abc!!!!! Mr. Anderson?! Ya... No, i am not."
       self.assertEqual(get_average_length_of_words_str(test),3.61)

    def test_average_len_of_words4(self):
       test = "abc abc abc abc olololololol abc!!!!! Mr. Anderson?! Ya... No, i am not. But who knows, he's not"
       self.assertEqual(get_average_length_of_words_str(test),3.61)
 
    def test_average_len_of_words5(self):
       test = "O.V.Ershov aorks on Nasa. But want to work on BSUIR"
       self.assertEqual(get_average_length_of_words_str(test),3.25)
    
#
#
#
#
    def test_average_len_of_sentences1(self):
       test ="abc abc abc abc olololololol abc!!!!! Mr. Anderson?! Ya... No, i am not."
       self.assertEqual(get_average_len_of_sentences_str(test),11.75)

    def test_average_len_of_sentences_2(self):
      text = 'Hi, Mr.Tom. Goodbye, Mrs.Smith! How r u, J.R.R.Tolkien?!'
      chars = [2, 2, 3, 7, 3, 5, 3, 1, 1, 1, 1, 1, 7]
      expected = round(sum(chars)/3, 2)
      assert get_average_len_of_sentences_str(text) == expected

    def test_average_len_of_sentences_3(self):
      text = "Hi, Mr.Tom. Goodbye, Dr.Strange 4114234. Ye no't!"
      chars = [2, 2, 3, 7, 2, 7, 2, 4]
      expected = round(sum(chars)/3, 2)
      assert get_average_len_of_sentences_str(text) == expected

#
#
#

    def test_get_top_K_repeated_N_grams_1(self):
      text = ''
      assert get_top_K_repeated_N_grams(text, 10, 2) == []


    def test_get_top_K_repeated_N_grams_2(self):
        text = 'Hi, Mr. Tom. Hi, Mr. 123 Tom.'
        expected = [('Hi Mr',2), ('Mr Tom', 1), ('Tom Hi',1)]
        assert get_top_K_repeated_N_grams(text, 10, 2) == expected


    def test_get_top_K_repeated_N_grams_3(self):
        text = 'Hi, Mr. Tom. Hi, Mr. Tom 123 123 123 123 123 123.'
        expected = [('Hi Mr',2), ('Mr Tom', 2), ('Tom Hi',1)]
        assert get_top_K_repeated_N_grams(text, 10, 2) == expected


    def test_get_top_K_repeated_N_grams_4(self):
        text = 'A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12'
        expected = [('A1 A2',1), ('A2 A3', 1), ('A3 A4', 1), ('A4 A5', 1), ('A5 A6', 1),
                    ('A6 A7', 1), ('A7 A8',1), ('A8 A9', 1), ('A9 A10', 1), ('A10 A11', 1)]
        assert get_top_K_repeated_N_grams(text, 10, 2) == expected

#
#
#
#
    def test_input_valid1(self):
       text = "#$%^"
       expected = False
       assert is_input_valid(text) == expected

    def test_input_valid2(self):
       text = "#привет"
       expected = False
       assert is_input_valid(text) == expected

    def test_input_valid3(self):
      text = "asdafв123dibh lw23 i;;p12=3-1024"
      expected = False
      assert is_input_valid(text) == expected
    
    def test_input_valid4(self):
      text = "asdaf123dibh lw23 i;;p123-1024"
      expected = True
      assert is_input_valid(text) == expected

    def test_input_valid5(self):
      text = "qweronrn njgvn rnjg ?!?!dkjn"
      expected = True
      assert is_input_valid(text) == expected

    def test_input_valid6(self):
      text = "qwero4324nrn njgwer12vn rn.j;g ?!?!d546kjn"
      expected = True
      assert is_input_valid(text) == expected
    
    


if __name__ == '__main__':
    unittest.main()