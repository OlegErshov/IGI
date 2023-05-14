TYPE = "type"
VALUE = "value"

DICT = "dict"
LIST = "list"
BYTES = "bytes"
TUPLE = "tuple"
INT = "int"
BOOL = "bool"
STR = "str"
FLOAT = "float"
NONE_TYPE = "NoneType"
COMPLEX = "complex"
TRUE = "True"

PRIMITIVE_TYPES = [INT, FLOAT, BOOL, COMPLEX, NONE_TYPE, STR]
DEFAULT_COLLECTION_TYPES = [LIST, TUPLE, BYTES]

FUNCTION = "function"

CODE = "__code__"
CLOSURE = "__closure__"
NAME = "__name__"
DEFAULTS = "__defaults__"

FUNCTION_ATTRIBUTES = [
    CODE,
    NAME,
    DEFAULTS,
    CLOSURE
]

GLOBALS = "__globals__"
BUILTINS = "__builtins__"
DOC = "__doc__"
OBJECT = "object"
OBJECT_TYPE = "__object_type__"

CLASS = "class"
NOT_CLASS_ATTRIBUTES = [
    "__class__",
    "__getattribute__",
    "__new__",
    "__setattr__",
]

MODULE_NAME = "__module__name__"
FIELDS = "__fields__"

CODE_OBJECT_ARGS = [
    'co_argcount',
    'co_posonlyargcount',
    'co_kwonlyargcount',
    'co_nlocals',
    'co_stacksize',
    'co_flags',
    'co_code',
    'co_consts',
    'co_names',
    'co_varnames',
    'co_filename',
    'co_name',
    'co_firstlineno',
    'co_lnotab',
    'co_freevars',
    'co_cellvars'
]