from Serializer.Base.serialization import serialize
from Serializer.Base.deserialization import deserialize
from Serializer.Xml_Serialization.logic import serialize_to_xml, deserialize_xml


class XmlSerializer:
    @staticmethod
    def dumps(obj):
        obj = serialize(obj)
        return serialize_to_xml(obj)

    @staticmethod
    def loads(obj):
        obj = deserialize_xml(obj)
        return deserialize(obj)

    @staticmethod
    def dump(obj, f):
        f.write(XmlSerializer.dumps(obj))

    @staticmethod
    def load(f):
        str = f.read()
        return XmlSerializer.loads(str)