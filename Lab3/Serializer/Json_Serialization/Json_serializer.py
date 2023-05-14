from ..Base.serialization import serialize
from ..Base.deserialization import deserialize
from logic import serialize_to_json
from .logic import deserialize_json


class JsonSerializer:
    @staticmethod
    def dumps(obj) -> str:
       
        serialized_obj = serialize(obj)
        return serialize_to_json(serialized_obj).replace('\n', '\\n')

    @staticmethod
    def dump(obj, file) -> None:
      
        file.write(JsonSerializer.dumps(obj))

    @staticmethod
    def loads(obj: str):
        obj = deserialize_json(obj.replace("\\n", "\n"))
        return deserialize(obj)

    @staticmethod
    def load(file):
        return JsonSerializer.loads(file.read())