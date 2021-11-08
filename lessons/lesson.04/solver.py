class Solver:

    EXC_TYPE_ERROR_ON_MUL = "a and b must be int or float"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def check_params(self):
        if not (
            isinstance(self.a, (int, float))
            and isinstance(self.b, (int, float))
        ):
            raise TypeError(self.EXC_TYPE_ERROR_ON_MUL)

    def add(self):
        self.check_params()
        return add(self.a, self.b)

    def mul(self):
        self.check_params()
        return self.a * self.b


def add(a, b):
    return a + b
