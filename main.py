# Quadratic calculator using the formula
# ax^2 + bx + c

import math

def main():
    print("ax^2 + bx + c")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    print(a, b, c)
    minusb = -b
    sr = math.sqrt((b * b)-(4 * a * c))
    total = (minusb + sr) / (2 * a)
    total2 = (minusb - sr) / (2 * a)
    print("x =", total, "or x =", total2)

if __name__ == '__main__':
    while True:
        main()

