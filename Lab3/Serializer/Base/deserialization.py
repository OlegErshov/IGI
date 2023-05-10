from . import constants
from pydoc import locate
from types import CodeType, FunctionType


def create_deserializer(obj_type):
    if obj_type == constants.DICT:
        return deserialize_dict
    if obj_type == constants.FUNCTION:
        return deserialize_function
    if obj_type in constants.DEFAULT_COLLECTION_TYPES:
        return deserialize_default_collection
    if obj_type == constants.CLASS:
        return deserialize_class
    if obj_type in constants.PRIMITIVE_TYPES:
        return deserialize_primitive_type
    if obj_type == constants.OBJECT:
        return deserialize_any_obj
    if obj_type == constants.MODULE_NAME:
        return deserialize_module


def deserialize(obj):
    obj = dict((a, b) for a, b in obj)
    obj_type = obj[constants.TYPE]
    deserializer = create_deserializer(obj_type)

    if deserializer is None:
        return

    return deserializer(obj_type, obj[constants.VALUE])


def deserialize_primitive_type(obj_type, primitive=None):
    if obj_type == constants.NONE_TYPE:
        return None

    if obj_type == constants.BOOL and isinstance(primitive, str):
        return primitive == constants.TRUE

    return locate(obj_type)(primitive)


def deserialize_default_collection(obj_type, default_collection):
    match obj_type:
        case constants.LIST:
            return [deserialize(i) for i in default_collection]

        case constants.TUPLE:
            return tuple([deserialize(i) for i in default_collection])

        case constants.BYTES:
            return bytes([deserialize(i) for i in default_collection])


def deserialize_dict(_, dict):
    deserialized_dict = {}
    for i in dict:
        value = deserialize(i[1])
        deserialized_dict[deserialize(i[0])] = value

    return deserialized_dict


def deserialize_function(_, function):
    func = [0] * 4
    code = [0] * 16
    glob = {constants.BUILTINS: __builtins__}

    for i in function:
        key = deserialize(i[0])

        if key == constants.GLOBALS:
            glob_dict = deserialize(i[1])
            for glob_key in glob_dict:
                glob[glob_key] = glob_dict[glob_key]
        elif key == constants.CODE:
            val = i[1][1][1]

            for arg in val:
                code_arg_key = deserialize(arg[0])
                if code_arg_key != constants.DOC and code_arg_key != 'co_linetable':
                    code_arg_val = deserialize(arg[1])
                    index = constants.CODE_OBJECT_ARGS.index(code_arg_key)
                    code[index] = code_arg_val

            code = CodeType(*code)
        else:
            index = constants.FUNCTION_ATTRIBUTES.index(key)
            func[index] = (deserialize(i[1]))

    func[0] = code
    func.insert(1, glob)

    deserialized_function = FunctionType(*func)
    if deserialized_function.__name__ in deserialized_function.__getattribute__(constants.GLOBALS):
        deserialized_function.__getattribute__(constants.GLOBALS)[
            deserialized_function.__name__] = deserialized_function

    return deserialized_function


def deserialize_class(_, class_dict):
    dct = deserialize_dict(constants.DICT, class_dict)
    name = dct[constants.NAME]
    del dct[constants.NAME]
    return type(name, (object,), dct)


def deserialize_module(_, module_name):
    return __import__(module_name)


def deserialize_any_obj(_, obj):
    obj_dict = deserialize_dict(constants.DICT, obj)
    deserialized_obj = obj_dict[constants.OBJECT_TYPE]()
    for _, value in obj_dict[constants.FIELDS].items():
        deserialized_obj.key = value
    return deserialized_obj