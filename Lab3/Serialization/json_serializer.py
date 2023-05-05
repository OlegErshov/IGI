from constants import *


def serialize_types(self, obj):
        result = {VALUE_FIELD: str(obj)}

        return result

def deserialize_types(self, obj):
        result = object
        if obj[TYPE_FIELD] == TYPES_NAMES[0]:
            result = int(obj[VALUE_FIELD])
        elif obj[TYPE_FIELD] == TYPES_NAMES[1]:
            result = float(obj[VALUE_FIELD])
        elif obj[TYPE_FIELD] == TYPES_NAMES[2]:
            result = complex(obj[VALUE_FIELD])
        elif obj[TYPE_FIELD] == TYPES_NAMES[3]:
            result = (obj[VALUE_FIELD] == "True")
        elif obj[TYPE_FIELD] == TYPES_NAMES[5]:
            result = None
        else:
            result = obj[VALUE_FIELD]

        return result