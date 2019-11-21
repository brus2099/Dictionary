
x = int(input("Valor incial en X: "))
y = int(input("Valor incial en Y: "))
h = float(input("Incrementos: "))
print()

for i in range (0, 5):
    k1 = 2 * x - 3 * y + 1
    print("K1:", "f(", x, ",", y, "):", k1)
    
    a, b = x + (1/2) * h , y + (1/2) * h * k1
    k2 = 2 * a - 3 * b + 1
    print("K2:", "f(", a, ",", b, "):", k2)
    
    c, d = x + (1/2) * h, y + (1/2) * h * k2
    k3 = 2 * c - 3 * d + 1
    print("K3:", "f(", c, ",", d, "):", k3)
    
    f, g = x + h, y + h * k3
    k4 = 2 * f - 3 * g + 1
    print("K4:", "f(", f, ",", g, "):", k4)
    
    RK = y + (h/6) * ( k1 + 2 * k2 + 2 * k3 + k4)
    print("RK4: ", RK)
    h += 0.1
    print()
