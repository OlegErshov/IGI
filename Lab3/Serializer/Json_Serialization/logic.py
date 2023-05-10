def serialize_to_json(obj) -> str:
    
    if type(obj) == tuple:
        serialized = []
        for i in obj:
            serialized.append(f"{serialize_to_json(i)}")
        ans = ", ".join(serialized)
        return f"[{ans}]"
    else:
        return f"\"{str(obj)}\""


def deserialize_json(obj: str):
    if obj == '[]':
        return tuple()
    elif obj[0] == '[':
        obj = obj[1:len(obj) - 1]
        deserialized_obj = []
        depth = 0
        is_quote = False
        substr = ""
        for i in obj:
            if i == '[':
                depth += 1
            elif i == ']':
                depth -= 1
            elif i == '\"':
                is_quote = not is_quote
            elif i == ',' and not is_quote and depth == 0:
                deserialized_obj.append(deserialize_json(substr))
                substr = ""
                continue
            elif i == ' ' and not is_quote:
                continue

            substr += i

        deserialized_obj.append(deserialize_json(substr))
        return tuple(deserialized_obj)
    else:
        return obj[1:len(obj) - 1]