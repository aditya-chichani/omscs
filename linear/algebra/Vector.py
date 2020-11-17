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
        return Vector(tuple([round(x + y, 3) for x, y in zip(self.coordinates, other.coordinates)]))

    def minus(self, other):
        return Vector(tuple([round(x - y, 3) for x, y in zip(self.coordinates, other.coordinates)]))

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

    def parallel_projection(self, other):
        unit_vector = other.normalized()
        return unit_vector.times_scalar(self.dot_product(unit_vector))

    def orthogonal_projection(self, other):
        return self.minus(self.parallel_projection(other))

    def cross_product(self, other):
        if (len(self.coordinates) != 3 or len(other.coordinates) != 3):
            raise RuntimeError("Incorrect number of co-ordinates!")
        else:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = other.coordinates
            return Vector((round(y1 * z2 - y2 * z1, 3), round(-(x1 * z2 - x2 * z1), 3), round(x1 * y2 - x2 * y1, 3)))

    def area_parallelogram(self, other):
        return self.cross_product(other).magnitude()

    def area_triangle(self, other):
        return 0.5 * self.cross_product(other).magnitude()
