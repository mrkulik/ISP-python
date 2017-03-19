class Vector(object):
    def __init__(self, *args):
        self.vector = list(args)

    def __add__(self, vector2):
        if len(self.vector) != len(vector2):
            return None

        for i in range(len(self.vector)):
            self.vector[i] += vector2[i]
        return self.vector

    def __sub__(self, vector2):
        if len(self.vector) != len(vector2):
            return None

        for i in range(len(self.vector)):
            self.vector[i] -= vector2[i]
        return self.vector

    def __mul__(self, vector2):
        if not isinstance(vector2, Vector):
            for i in range(len(self.vector)):
                self.vector[i] *= vector2
            return self.vector

        if len(self.vector) != len(vector2):
            return False

        con = 0
        for i in range(len(self.vector)):
            con += self.vector[i] * vector2[i]
        return con

    def __eq__(self, vector2):
        if len(self.vector) != len(vector2):
            return False

        for i in range(len(self.vector)):
            if self.vector[i] != vector2[i]:
                return False
        return True

    def __str__(self):
        return str(self.vector)

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, item):
        return self.vector[item]


a = Vector(1, 2, 3)
b = Vector(4, 5, 6)
print a + b
print a - b
print a * b
print a == b