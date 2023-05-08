import re

from constants import *

from venv.lib64 import frozendict


def to_json(obj):
    ans = ""
    ans_list = []
    flag = False
    if type(obj) == frozendict or type(obj) == dict:
        for key, value in obj.items():
            if key == VALUE_FIELD or key == TYPE_FIELD:
                ans_list.append("" + to_json(key) + ": " + to_json(value) + "")
                flag = True
            else:
                ans_list.append("[" + to_json(key) + ", " + to_json(value) + "]")
                flag = False
        ans += ", ".join(ans_list)
        if flag:
            ans = "{" + ans + "}"
        else:
            ans = "[" + ans + "]"
        return f"{ans}"
    elif type(obj) == tuple:
        serialized = []
        for i in obj:
            serialized.append(f"{to_json(i)}")
        ans = ", ".join(serialized)
        return f"[{ans}]"
    else:
        return f"\"{str(obj)}\""
    
def from_json(string):  # string to obj
    if string == '{}':
        return frozendict()
    elif string[0] == '{':
        ans = dict()
        string = string[1:len(string) - 1]
        if re.match(VALUE_REGEX1, string):
            temp = ""
            flag = False
            save_i = 0
            ans_list = []
            balance = 0
            balance2 = 0
            for i in range(8, len(string)):
                if string[i] == '[' and not flag:
                    balance2 += 1
                elif string[i] == ']' and not flag:
                    balance2 -= 1
                if string[i] == '[' and not flag and balance2 <= 2:
                    continue
                elif string[i] == ']' and not flag and balance2 < 2:
                    continue
                elif string[i] == '{' and not flag:
                    balance += 1
                elif string[i] == '}' and not flag:
                    balance -= 1
                elif string[i] == '\"':
                    flag = not flag
                elif string[i] == ',' and not flag and balance == 0 and balance2 != 0:
                    if temp != "" and temp != "[]":
                        ans_list.append(from_json(temp))
                    else:
                        ans_list.append({})
                    temp = ""
                    continue
                elif string[i] == ' ' and not flag and balance == 0:
                    continue
                elif string[i] == "," and not flag and balance2 == 0:
                    if temp != "" and temp != "[]":
                        ans_list.append(from_json(temp))
                    else:
                        ans_list.append({})
                    save_i = i
                    temp = ""
                    break
                temp += string[i]

            ans[VALUE_FIELD] = {}

            ans_list = tuple(ans_list)

            for i in range(0, len(ans_list), 2):

                ans[VALUE_FIELD][ans_list[i]] = ans_list[i + 1]

            temp = ""
            for i in range(save_i + 11, len(string)):
                if string[i] == '\"':
                    ans[TYPE_FIELD] = temp
                    temp = ""
                    break
                else:
                    temp += string[i]
        elif re.match(VALUE_REGEX2, string):
            temp = ""
            flag = False
            save_i = 0
            ans_list = []
            balance = 0
            for i in range(10, len(string)):
                if string[i] == '{' and not flag:
                    balance += 1
                elif string[i] == '}' and not flag:
                    balance -= 1
                if string[i] == '\"':
                    flag = not flag
                elif string[i] == ',' and not flag and balance == 0:
                    ans_list.append(from_json(temp))
                    temp = ""
                    continue
                elif string[i] == ' ' and not flag and balance == 0:
                    continue
                elif string[i] == "]" and not flag and balance == 0:
                    if temp != "":
                        ans_list.append(from_json(temp))
                    save_i = i
                    temp = ""
                    break
                temp += string[i]

            ans_list = tuple(ans_list)
            ans[VALUE_FIELD] = ans_list

            for i in range(save_i + 12, len(string)):
                if string[i] == '\"':
                    ans[TYPE_FIELD] = temp
                    temp = ""
                    break
                else:
                    temp += string[i]
        elif re.match(VALUE_REGEX3, string):
            temp = ""
            flag = False
            save_i = 0
            balance = 0
            for i in range(9, len(string)):
                if string[i] == '{' and not flag:
                    balance += 1
                elif string[i] == '}' and not flag:
                    balance -= 1
                elif string[i] == '\"':
                    flag = not flag
                elif string[i] == "," and not flag and balance == 0:
                    if temp != "":
                        ans[VALUE_FIELD] = from_json(temp)
                    save_i = i
                    temp = ""
                    break
                temp += string[i]

            for i in range(save_i + 11, len(string)):
                if string[i] == '\"':
                    ans[TYPE_FIELD] = temp
                    temp = ""
                    break
                else:
                    temp += string[i]
        else:
            temp = ""
            flag = False
            i = 10
            while i < len(string):
                if string[i] == '\"' and not flag:
                    ans[VALUE_FIELD] = temp
                    temp = ""
                    flag = True
                    i += 11
                elif string[i] == '\"' and flag:
                    ans[TYPE_FIELD] = temp
                    temp = ""
                    break
                else:
                    temp += string[i]
                i += 1

        return frozendict(ans)