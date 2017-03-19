import types


class MetaLoggerInfo(type):
    @classmethod
    def logger_decorator(cls, func):
        def function(*args, **kwargs):
            result = func(*args, **kwargs)
            message = "function: {}; arguments: {}; result: {};\n".format(func.__name__, args, result)
            self = args[0]
            self.log_info += message
            return result

        return function

    def __new__(cls, name, bases, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, types.FunctionType):
                dictionary[key] = cls.logger_decorator(value)
        dictionary["log_info"] = ""
        dictionary["__str__"] = lambda self: self.log_info
        return super(MetaLoggerInfo, cls).__new__(cls, name, bases, dictionary)


class Logger(object):
    __metaclass__ = MetaLoggerInfo


class Example(Logger):
    def __init__(self, number):
        self.example = "I`m example string!"
        self.number = number

    def change(self, string):
        self.example = string
        return self.example


ex = Example(123)
ex1 = Example(4567)
ex.change("Yo yo yo!")
ex1.change("I`m second string!")
print ex
print ex1
