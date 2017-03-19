import types


class FilterList(object):
    types_list = (frozenset, set, tuple, list)

    def __init__(self, iterable_obj=None):
        if iterable_obj is None:
            self.base = list()
        else:
            for item_type in self.types_list:
                if isinstance(iterable_obj, item_type) is False:
                    continue
                else:
                    self.base = iterable_obj
            if self.base is None:
                self.base = list()

    def __iter__(self):
        return iter(self.base)

    def filter(self, func=bool):
        if isinstance(func, types.FunctionType):
            for item in self.base:
                if func(item) is True:
                    yield item
                else:
                    continue

    def __str__(self):
        return str(self.base)


l = FilterList([1, 2, 3, 4])
for x in l.filter(lambda x: x >= 2):
    print(x)
