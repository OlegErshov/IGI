from abc import ABC, abstractmethod
from Serialization.json_serializer import Json_Serializer

class Parser(ABC):

    def __init__(self):
        self.serializer = Json_Serializer()

    @abstractmethod
    def dump(self, obj, file):  # obj to file

        pass

    @abstractmethod
    def dumps(self, obj):  # obj to string

        pass

    @abstractmethod
    def load(self, file):  # file to obj

        pass

    @abstractmethod
    def loads(self, string):  # string to obj

        pass