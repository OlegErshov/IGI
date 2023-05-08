from Lab3.Parsers.JsonParser import ParserJson
from constants import *



def test_iterables():
    parser = ParserJson
    iterables = [test_list, test_tuple, test_set, test_dict]
    for iterable in iterables:
        assert iterable == parser.loads(parser.dumps(iterable))