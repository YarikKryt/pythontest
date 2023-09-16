import math

# Task A

# Розрахунок індексу першої значущої цифри (m)
def first_significant_digit_index(number):
    if number == 0:
        return 0
    abs_number = abs(number)
    if abs_number >= 1:
        m = 0
        while abs_number >= 1:
            abs_number /= 10
            m += 1
        return m - 1
    else:
        m = 0
        while abs_number < 1:
            abs_number *= 10
            m -= 1
        return m

# Розрахунок першої значущої цифри am
def first_significant_digit(number):
    str_number = str(abs(number))
    for char in str_number:
        if char != '.' and char != '0':
            return char
    return '0'

# Введення величин x1, x2, x3 та їх кількостей точних цифр n1, n2, n3
x1 = float(input("Введіть x1: "))
x2 = float(input("Введіть x2: "))
x3 = float(input("Введіть x3: "))

# Введення та перевірка точних цифр n1, n2, n3
n1 = 0
while n1 <= 0 or not isinstance(n1, int):
    try:
        n1 = int(input("Введіть кількість точних цифр для x1 (ціле додатне число): "))
        if n1 <= 0:
            print("Кількість точних цифр має бути додатнім цілим числом.")
    except ValueError:
        print("Введіть дійсне ціле число.")

n2 = 0
while n2 <= 0 or not isinstance(n2, int):
    try:
        n2 = int(input("Введіть кількість точних цифр для x2 (ціле додатне число): "))
        if n2 <= 0:
            print("Кількість точних цифр має бути додатнім цілим числом.")
    except ValueError:
        print("Введіть дійсне ціле число.")

n3 = 0
while n3 <= 0 or not isinstance(n3, int):
    try:
        n3 = int(input("Введіть кількість точних цифр для x3 (ціле додатне число): "))
        if n3 <= 0:
            print("Кількість точних цифр має бути додатнім цілим числом.")
    except ValueError:
        print("Введіть дійсне ціле число.")

# Розрахунок похибок Δx1, Δx2, Δx3
m1 = first_significant_digit_index(x1)
m2 = first_significant_digit_index(x2)
m3 = first_significant_digit_index(x3)

delta_x1 = 0.5 * 10 ** (m1 - n1 + 1)
delta_x2 = 0.5 * 10 ** (m2 - n2 + 1)
delta_x3 = 0.5 * 10 ** (m3 - n3 + 1)

# Розрахунок відносних похибок δx1, δx2, δx3
am1 = first_significant_digit(x1)
am2 = first_significant_digit(x2)
am3 = first_significant_digit(x3)

# Розрахунок δx1, δx2, δx3 з перевіркою умови та зміною формули, якщо n >= 2
if n1 >= 2:
    delta_x1_relative = (1 / (2 * int(am1))) * (1 / 10) ** (n1 - 1)
else:
    delta_x1_relative = (1 / int(am1)) * (1 / 10) ** (n1 - 1)

if n2 >= 2:
    delta_x2_relative = (1 / (2 * int(am2))) * (1 / 10) ** (n2 - 1)
else:
    delta_x2_relative = (1 / int(am2)) * (1 / 10) ** (n2 - 1)

if n3 >= 2:
    delta_x3_relative = (1 / (2 * int(am3))) * (1 / 10) ** (n3 - 1)
else:
    delta_x3_relative = (1 / int(am3)) * (1 / 10) ** (n3 - 1)

# Розрахунок похідних функції F
dF_dx1 = 16 * x1 + 7 * x3
dF_dx2 = (4 * x3) / (math.sqrt(x3 * x2)) + 12 * x2 - 5
dF_dx3 = (4 * x2) / (math.sqrt(x2 * x3)) + 14 * x3 + 7 * x1

# Розрахунок абсолютної похибки ΔF
delta_F = abs(dF_dx1) * delta_x1_relative + abs(dF_dx2) * delta_x2_relative + abs(dF_dx3) * delta_x3_relative

# Розрахунок відносної похибки δF
F = 8 * x1**2 + 6 * x2**2 + 7 * x3**2 + 7 * x1 * x3 - 5 * x2 + 8 * math.sqrt(x3 * x2)
delta_F_relative = delta_F / abs(F) * 100

# Виведення результатів завдання А
print("\nЗавдання А) ")
print(f"\nАбсолютні похибки:")
print(f"\nΔx1 = {delta_x1}")
print(f"Δx2 = {delta_x2}")
print(f"Δx3 = {delta_x3}")

print(f"\nВідносні похибки:")
print(f"\nδx1 = {delta_x1_relative * 100}%")
print(f"δx2 = {delta_x2_relative * 100}%")
print(f"δx3 = {delta_x3_relative * 100}%")

print(f"\nРезультат обчислення F = {F}")
print(f"Абсолютна похибка обчислення ΔF = {delta_F}")
print(f"Відносна похибка обчислення δF = {delta_F_relative}%")

#Task B

# Задана похибка Δ
delta = 15 * 10**-3

# Розрахунок n1
n1 = abs(m1 + 1 - math.log10(2 * delta))
n1 = round(n1)  # Округлення до найближчого цілого числа

# Розрахунок n1
n2 = abs(m2 + 1 - math.log10(2 * delta))
n2 = round(n2)  # Округлення до найближчого цілого числа

# Розрахунок n1
n3 = abs(m3 + 1 - math.log10(2 * delta))
n3 = round(n3)  # Округлення до найближчого цілого числа

delta_Fb = delta * (dF_dx1 + dF_dx2 + dF_dx3)

delta_F_relativeb = delta_Fb / F

# Виведення результатів завдання B

print("\nЗавдання B)")
print(f"\nn1 = {n1}")
print(f"n2 = {n2}")
print(f"n3 = {n3}")

print(f"\nВідносні похибки:")
print(f"\nδx1 = {delta_x1_relative * 100}%")
print(f"δx2 = {delta_x2_relative * 100}%")
print(f"δx3 = {delta_x3_relative * 100}%")

print(f"\nАбсолютна похибка обчислення ΔF = {delta_Fb}")
print(f"Відносна похибка обчислення δF = {delta_F_relativeb * 100}%")

print("\nГрупа: ОІ-11сп")
print("ПІБ студента: Куспісь Я-О. А.")
print("Номер ЛР: 1")
print("Варіант завдання: 15\n")