import json


class DKType(Exception):
    def __init__(self, obj):
        self.message = "DK Type: " + str(type(obj))
        super(DKType, self).__init__(self.message)


def to_json(obj, unknown=False):
    def not_list_and_dict(obj):

        if isinstance(obj, list):
            return obj.__str__()

        if isinstance(obj, str):
            for literal in '\\\"':
                if literal in obj:
                    obj = obj.replace(literal, '\\' + literal)

            literals = '\b\f\n\r\t'
            literals_letters = 'bfnrt'
            for literal in literals:
                if literal in obj:
                    obj = obj.replace(literal, '\\' + literals_letters[literals.index(literal)])

            for literal in '\a\v':
                if literal in obj:
                    obj = obj.replace(literal, '\\u{0:04x}'.format(ord(literal)))

            return '\"' + obj + '\"'

        if isinstance(obj, bool):
            return str(obj).lower()

        if isinstance(obj, int):
            return obj.__str__()

        if isinstance(obj, float):
            return obj.__str__()

        if obj is None:
            return "null"

        if unknown:
            raise DKType(obj)

    if isinstance(obj, dict):
        dict_str = '{'

        last_key = None

        if obj.keys():
            last_key = obj.keys()[-1]

        for key, value in obj.iteritems():
            if isinstance(value, dict):
                dict_str += '\"' + key.__str__() + '\": ' + to_json(value)
            else:
                dict_str += '\"' + key.__str__() + '\": ' + not_list_and_dict(value)

            if key is not last_key:
                dict_str += ', '

        dict_str += '}'
        return dict_str
    elif isinstance(obj, list):
        lst_str = '['

        for elem in obj:
            lst_str += to_json(elem)

            if elem is not obj[-1]:
                lst_str += ', '

        lst_str += ']'
        return lst_str
    else:
        return not_list_and_dict(obj)


print json.dumps('\\\'\"\a\b\f\n\r\t\v')
print to_json('\\\'\"\a\b\f\n\r\t\v')

print to_json({1: {'a': 56}, 2: True, 3: None})
print json.dumps({1: {'a': 56}, 2: True, 3: None})

print to_json('\\\n')
print json.dumps('\\\n')