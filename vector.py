class Vector:

    def __init__(self, init_x=0, init_y=0):
        if not isinstance(init_x, (int, float)):
            raise ValueError('X must be number')
        self.x = init_x
        if not isinstance(init_y, (int, float)):
            raise ValueError('Y must be number')
        self.y = init_y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def mul_on_num (self, num):
        if not isinstance(num, (int, float)):
            raise ValueError('Can multiply only on number')
        return Vector(self.x * num, self.y*num)

    def scalar_mul (self, other):
        return self.x * other.x + self.y * other.y

    def get_len (self):
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return '<{}, {}>'.format(self.x, self.y)

    def __repr__(self):
        return '<{}, {}>'.format(self.x, self.y)





