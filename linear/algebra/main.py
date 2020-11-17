from linear.algebra.Vector import Vector

a = Vector((8.218, -9.341))
b = Vector((-1.129, 2.111))
print(a.plus(b))
c = Vector((7.119, 8.215))
d = Vector((-8.223, 0.878))
print(c.minus(d))
e = Vector((1.671, -1.012, -0.318))
k = 7.41
print(e.times_scalar(k))

print("-------------------------------------------------------------------")

v1 = Vector((-0.221, 7.437))
print(v1.magnitude())
v2 = Vector((8.813, -1.331, -6.247))
print(v2.magnitude())
v3 = Vector((5.581, -2.136))
print(v3.normalized())
v4 = Vector((1.996, 3.108, -4.554))
print(v4.normalized())

print("-------------------------------------------------------------------")

v5 = Vector((7.887, 4.138))
v6 = Vector((-8.802, 6.776))
print(v5.dot_product(v6))
v7 = Vector((-5.955, -4.904, -1.874))
v8 = Vector((-4.496, -8.755, 7.103))
print(v7.dot_product(v8))

v5 = Vector((3.183, -7.627))
v6 = Vector((-2.668, 5.319))
print(v5.angle_in_rad(v6))
v7 = Vector((7.35, 0.221, 5.188))
v8 = Vector((2.751, 8.259, 3.985))
print(v7.angle_in_deg(v8))

print("-------------------------------------------------------------------")

v1 = Vector((-7.579, -7.88))
v2 = Vector((22.737, 23.64))
print(v1.is_parallel(v2))
print(v1.is_orthogonal(v2))
v3 = Vector((-2.029, 9.97, 4.172))
v4 = Vector((-9.231, -6.639, -7.245))
print(v3.is_parallel(v4))
print(v3.is_orthogonal(v4))
v5 = Vector((-2.328, -7.284, -1.214))
v6 = Vector((-1.821, 1.072, -2.94))
print(v5.is_parallel(v6))
print(v5.is_orthogonal(v6))
v7 = Vector((2.118, 4.827))
v8 = Vector((0, 0))
print(v7.is_parallel(v8))
print(v7.is_orthogonal(v8))

print("-------------------------------------------------------------------")
