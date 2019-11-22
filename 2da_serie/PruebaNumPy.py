
x, y, h = 1.4, 2.1122, 0.1
k1 = 2 * x - 3 * y + 1
print(x, y)

a, b = x + (1/2) * h , y + (1/2) * h * - k1
k2 = 2 * a - 3 * b + 1
print(a, b)

c, d = a + (1/2) * h, b + (1/2) * h * k2
k3 = 2 * c - 3 * d + 1
print(c, d)

f, g = c + h, d + h * k3
k4 = 2 * f - 3 * g + 1
print(f, g)

print("k1: ", k1, "k2: ", k2, "k3: ", k3, "k4: ", k4)

RK = y + (h/6) * ( k1 + 2 * k2 + 2 * k3 + k4)
print("RK4: ", RK)