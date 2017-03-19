class Xrange(object):
    def __init__(self, begin=0, to=0, step=1):
        self.begin = begin
        self.to = to
        self.step = step
        self.position = self.begin

        if self.to == 0 and self.step > 0:
            self.to, self.begin = self.begin, 0
            self.position = 0

    def __iter__(self):
        return self

    def next(self):
        if self.step > 0:
            if self.position < self.to:
                self.position += self.step
                return self.position - self.step
        else:
            if self.position > self.to:
                self.position += self.step
                return self.position - self.step

        raise StopIteration()

    def __getitem__(self, key):
        if key >= 0:
            return self.begin + key * self.step
        else:
            return self.to + key * self.step

    def __reversed__(self):
        if self.step > 0:
            self.step = -self.step
            self.begin, self.to = self.to - 1, self.begin - 1
            self.position = self.begin
        else:
            self.step = -self.step
            self.begin, self.to = self.to + 1, self.begin + 1
            self.position = self.begin

        return self

    def __len__(self):
        return abs((self.begin - self.to) / self.step)

    def __str__(self):
        return Xrange.__name__ + '({}, {}, {})'.format(self.begin, self.to, self.step)

for item in Xrange(0, 10, 2):
    print item

for item in Xrange(10, 0, -2):
    print item

print Xrange(10)[4]

print len(Xrange(15, -5, -2))

print str(Xrange(0, 10, 2))