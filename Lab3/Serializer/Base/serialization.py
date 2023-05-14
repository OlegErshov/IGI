from . import constants
import inspect


def get_specific_serializer_function(obj):
    if isinstance(obj, int | float | str | bool | complex | type(None)):
        return serialize_primitive_type
    if isinstance(obj, dict):
        return serialize_dict
    if isinstance(obj, list | tuple | bytes):
        return serialize_default_collection
    if inspect.isfunction(obj):
        return serialize_function
    if isinstance(obj, type(type.__dict__)):
        return serialize_mappingproxy
    if inspect.ismethoddescriptor(obj) or inspect.isbuiltin(obj):
        return serialize_mappingproxy
    if inspect.isgetsetdescriptor(obj) or inspect.ismemberdescriptor(obj):
        return serialize_mappingproxy
    if inspect.isclass(obj):
        return serialize_class
    if inspect.iscode(obj):
        return serialize_code
    if inspect.ismodule(obj):
        return serialize_module
    return serialize_any_obj


def serialize(obj) -> tuple:
   
    serializer = get_specific_serializer_function(obj)
    serialized_obj = serializer(obj)
    result = tuple((k, serialized_obj[k]) for k in serialized_obj)
    return result


def serialize_primitive_type(obj: float | bool | int | complex | str | None) -> dict:
    
    serialized_primitive_type = dict()
    serialized_primitive_type[constants.TYPE] = type(obj).__name__
    serialized_primitive_type[constants.VALUE] = obj
    return serialized_primitive_type


def serialize_dict(obj: dict) -> dict:
    
    serialized_obj = dict()
    serialized_obj[constants.TYPE] = constants.DICT
    serialized_obj[constants.VALUE] = {}

    for k, v in obj.items():
        key = serialize(k)
        value = serialize(v)
        serialized_obj[constants.VALUE][key] = value

    serialized_obj[constants.VALUE] = tuple((k, serialized_obj[constants.VALUE][k])
                                            for k in serialized_obj[constants.VALUE])

    return serialized_obj


def serialize_default_collection(obj: tuple | list | bytes):
    
    serialized_obj = dict()
    serialized_obj[constants.TYPE] = type(obj).__name__
    serialized_obj[constants.VALUE] = tuple([serialize(i) for i in obj])
    return serialized_obj


def serialize_function(obj) -> dict:
    
    serialized_function = dict()
    serialized_function[constants.TYPE] = constants.FUNCTION
    serialized_function[constants.VALUE] = {}
    members = inspect.getmembers(obj)
    members = [i for i in members if i[0] in constants.FUNCTION_ATTRIBUTES]
    for i in members:
        key = serialize(i[0])
        if i[0] != constants.CLOSURE:
            value = serialize(i[1])
        else:
            value = serialize(None)

        serialized_function[constants.VALUE][key] = value
        if i[0] == constants.CODE:
            key = serialize(constants.GLOBALS)
            serialized_function[constants.VALUE][key] = {}
            names = i[1].__getattribute__("co_names")
            glob = obj.__getattribute__(constants.GLOBALS)
            glob_dict = {}
            for name in names:
                if name == obj.__name__:
                    glob_dict[name] = obj.__name__
                elif name in glob and not inspect.ismodule(name) and name not in __builtins__:
                    glob_dict[name] = glob[name]
            serialized_function[constants.VALUE][key] = serialize(glob_dict)

    serialized_function[constants.VALUE] = tuple((k, serialized_function[constants.VALUE][k])
                                                 for k in serialized_function[constants.VALUE])
    return serialized_function


def serialize_mappingproxy(obj) -> dict:
   
    serialized_obj = dict()
    serialized_obj[constants.TYPE] = type(obj).__name__

    serialized_obj[constants.VALUE] = {}
    members = inspect.getmembers(obj)
    members = [i for i in members if not callable(i[1])]
    for i in members:
        key = serialize(i[0])
        val = serialize(i[1])
        serialized_obj[constants.VALUE][key] = val
    serialized_obj[constants.VALUE] = tuple(
        (k, serialized_obj[constants.VALUE][k]) for k in serialized_obj[constants.VALUE])

    return serialized_obj


def serialize_class(obj) -> dict:
   
    serialized_obj = dict()
    serialized_obj[constants.TYPE] = constants.CLASS
    serialized_obj[constants.VALUE] = {}
    serialized_obj[constants.VALUE][serialize(
        constants.NAME)] = serialize(obj.__name__)
    members = []
    for i in inspect.getmembers(obj):
        if not (i[0] in constants.NOT_CLASS_ATTRIBUTES):
            members.append(i)

    for i in members:
        key = serialize(i[0])
        val = serialize(i[1])
        serialized_obj[constants.VALUE][key] = val
    serialized_obj[constants.VALUE] = tuple(
        (k, serialized_obj[constants.VALUE][k]) for k in serialized_obj[constants.VALUE])

    return serialized_obj


def serialize_code(obj) -> dict:
    
    if type(obj).__name__ is None:
        return None

    serialized_code = dict()
    serialized_code[constants.TYPE] = type(obj).__name__

    serialized_code[constants.VALUE] = {}
    members = inspect.getmembers(obj)
    members = [i for i in members if not callable(i[1])]
    for i in members:
        key = serialize(i[0])
        val = serialize(i[1])
        serialized_code[constants.VALUE][key] = val
    serialized_code[constants.VALUE] = tuple(
        (k, serialized_code[constants.VALUE][k]) for k in serialized_code[constants.VALUE])

    return serialized_code


def serialize_module(obj):
    serialized_module = dict()
    serialized_module[constants.TYPE] = constants.MODULE_NAME
    serialized_module[constants.VALUE] = obj.__name__

    return serialized_module


def serialize_any_obj(obj) -> dict:
   
    obj_type = type(obj)
    serialized_obj = dict()
    serialized_obj[constants.TYPE] = constants.OBJECT
    serialized_obj[constants.VALUE] = {}
    serialized_obj[constants.VALUE][serialize(
        constants.OBJECT_TYPE)] = serialize(obj_type)
    serialized_obj[constants.VALUE][serialize(
        constants.FIELDS)] = serialize(obj.__dict__)
    serialized_obj[constants.VALUE] = tuple(
        (k, serialized_obj[constants.VALUE][k]) for k in serialized_obj[constants.VALUE])

    return serialized_obj