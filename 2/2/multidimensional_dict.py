class MultidimensionalDict(dict):
    def __getitem__(self, key):
        if key in self.keys():
            return super(MultidimensionalDict, self).__getitem__(key)
        else:
            self[key] = MultidimensionalDict()
            return self[key]


a = MultidimensionalDict()
a['a']['b']['c'] = 15
a['a']['b']['d'] = 20
a['f'] = 77
print a
