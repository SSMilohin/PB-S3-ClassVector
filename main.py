class Vector:
    def __init__(self, x=0, *other):
        if isinstance(x, (list, tuple)):
            self.x, self.y, self.z = x
        elif isinstance(x, (int, float)) and len(other) == 0:
            self.x, self.y, self.z = int(x), int(x), int(x)
        elif x == 0:
            self.x, self.y, self.z = 0, 0, 0
        else:
            self.x, self.y, self.z = int(x), int(other[0]), int(other[1])

    def length(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __abs__(self):
        return self.length()

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector(int(self.x * scalar), int(self.y * scalar), int(self.z * scalar))
        elif isinstance(scalar, Vector):
            return self.dot_product(scalar)
        else:
            return self

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def __xor__(self, other):
        return self.cross_product(other)

    @staticmethod
    def triple_product(a, b, c):
        return a.dot_product(b.cross_product(c))

    def are_complanar(a, b, c):
        determinant = a.dot_product(b.cross_product(c))
        return determinant == 0

    def __or__(self, other):
        return self.are_collinear(other)

    def are_collinear(self, other):
        return self.cross_product(other).length() < 1e-10

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


v1 = Vector(1, 2, 3)
v2 = Vector((4, 5, 6))
v3 = Vector([0, 3, 4])
v4 = Vector(5)
v5 = Vector()

print(v1, v2, v3, v4, v5, '\n', sep='\n', end='')

print('Сумма v1 и v2:', v1 + v2)
print('Разность v3 и v1:', v3 - v1)
print('Унарный минус на v1:', -v1)
print('Умножение вектора v4 на число:', v4 * 2)
print('Скалярное произведение векторов v1 и v2:', v1 * v2)
print('Векторное произведение векторов v1 и v2:', v1 ^ v2)
print('Длина вектора v3:', abs(v3), v3.length())
print('Смешанное произведение векторов v1, v2, v3:', Vector.triple_product(v1, v2, v3))
print('Коллинеарность векторов v1 и v2:', v1 | v2)
print('Компланарность векторов v1, v2, v3:', Vector.are_complanar(v1, v2, v3))
print('Компланарность векторов v1, v2, v4:', Vector.are_complanar(v1, v2, v4))
