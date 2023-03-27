import unittest

from task1 import get_amount_of_sentences_from_string
from task1 import get_average_len_of_sentences_str
from task1 import get_average_length_of_words_str
from task1 import get_amount_of_nondec_sentences_str

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
    

    def test_average_len_of_words(self):
       test = "a1a2 1123 a1 O.B.R. Mr.Jone!!! Hi, im Batman"
       self.assertEqual(get_average_length_of_words_str(test),2.5)

    def test_average_len_of_words2(self):
       test = "abc abc abc abc olololololol abc!!!!! Mr. Anderson?! Ya... No, i am not."
       self.assertEqual(get_average_length_of_words_str(test),3.61)

    def test_average_len_of_sentences(self):
       test = ""
       self.assertEqual(get_average_len_of_sentences_str(test),"error")

    def test_average_len_of_sentences(self):
       test ="abc abc abc abc olololololol abc!!!!! Mr. Anderson?! Ya... No, i am not."
       self.assertEqual(get_average_len_of_sentences_str(test),11.75)


if __name__ == '__main__':
    unittest.main()