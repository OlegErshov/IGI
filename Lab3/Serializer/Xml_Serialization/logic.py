def serialize_to_xml(obj) -> str:
    if type(obj) == tuple:
        serialized = []
        for i in obj:
            if type(i) != tuple:
                serialized.append(
                    f"<str>{serialize_to_xml(i)}</str> ")
            else:
                serialized.append(
                    f"{serialize_to_xml(i)}")
        ans = "".join(serialized)
        return f"<{type(obj).__name__}>{ans}</{type(obj).__name__}> "
    else:
        return obj


def deserialize_xml(obj: str):
    if obj == '<tuple></tuple>':
        return tuple()
    elif obj[:7] == '<tuple>':
        obj = obj[7:-9]
        if obj[-1] == ' ':
            obj = obj[:-1]

        parsed = []
        depth = 0
        substr = ""
        for i in obj:
            if i == '<' or i == '>':
                depth += 1
            elif i == '/':
                depth -= 4
            elif depth == 0:
                parsed.append(deserialize_xml(substr))
                substr = ""
                continue

            substr += i
        parsed.append(deserialize_xml(substr))
        return tuple(parsed)

    elif obj[:5] == '<str>':
        parsed = []
        ind = obj.find('</str>')
        if obj[ind + 6:] != "":
            parsed.append(deserialize_xml(obj[5:ind]))
            parsed.append(deserialize_xml(obj[ind + 6:]))
        else:
            return obj[5:ind]
        return tuple(parsed)
    else:
        return obj