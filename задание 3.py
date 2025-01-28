def calculate_lace_length(a, b, l, N):
    s = 2 * l + (N - 1) * 2 * b + N * 2 * a**0.5
    return s

a = int(input("Введите расстояние между рядами (a): "))
b = int(input("Введите расстояние между дырочками в ряду (b): "))
l = int(input("Введите длину свободного конца шнурка (l): "))
N = int(input("Введите количество дырочек в каждом ряду (N): "))

print(f"Длина шнурка: {calculate_lace_length(a, b, l, N):.2f}")
