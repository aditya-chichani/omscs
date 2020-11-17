from math import sqrt, acos, pi


class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.dimension = len(coordinates)

    def __str__(self):
        return "Vector has {} dimensions and is represented as: {}".format(self.dimension, self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def plus(self, other):
        return Vector(tuple([x + y for x, y in zip(self.coordinates, other.coordinates)]))

    def minus(self, other):
        return Vector(tuple([x - y for x, y in zip(self.coordinates, other.coordinates)]))

    def times_scalar(self, k):
        return Vector(tuple([round(k * x, 3) for x in self.coordinates]))

    def magnitude(self):
        sum = 0
        for vi in self.coordinates:
            sum += vi * vi
        return round(sqrt(sum), 3)

    def normalized(self):
        return self.times_scalar(1 / self.magnitude())

    def dot_product(self, other):
        sum = 0
        for vi, wi in zip(self.coordinates, other.coordinates):
            sum += vi * wi
        return round(sum, 3)

    def angle_in_rad(self, other):
        return round(acos(self.dot_product(other) / (self.magnitude() * other.magnitude())), 3)

    def angle_in_deg(self, other):
        return round((acos(self.dot_product(other) / (self.magnitude() * other.magnitude())) * 180) / pi, 3)

    def is_parallel(self, other):
        return (abs(self.dot_product(other)) == (self.magnitude() * other.magnitude()))

    def is_orthogonal(self, other):
        return (self.dot_product(other) == 0)
