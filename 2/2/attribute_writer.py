import json


def AttributeWriter(filename):
    class AttWriter(type):
        def __new__(mcs, name, bases, dct):
            try:
                attr_str = open(filename, 'r').read()
                attributes = json.loads(attr_str)
            except IOError:
                return super(AttWriter, mcs).__new__(mcs, name, bases, dct)

            for key, value in attributes.iteritems():
                mcs.__setattr__(mcs, key, value)
            return super(AttWriter, mcs).__new__(mcs, name, bases, dct)
    return AttWriter


class Auto(object):
    __metaclass__ = AttributeWriter('../attributes.txt')


print Auto.some_str
print Auto.some_var