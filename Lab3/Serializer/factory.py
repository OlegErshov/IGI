from Serializer.Json_Serialization.Json_serializer import JsonSerializer
from Serializer.Xml_Serialization.xml_serializer import XmlSerializer


class SerializersFactory:
    @staticmethod
    def create_serializer(name: str):
        match name.lower():
            case "json":
                return JsonSerializer
            case "xml":
                return XmlSerializer
            case _:
                raise ValueError(f"{name} is not supported!")