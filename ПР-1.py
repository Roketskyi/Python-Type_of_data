input_str = input("Введіть 5 невід'ємних дійсних чисел розділених пробілами: ")

values = input_str.split()

if len(values) != 5:
    print("Потрібно ввести рівно 5 чисел!")
    exit()

try:
    K1 = float(values[0])
    a1 = float(values[1])
    K2 = float(values[2])
    a2 = float(values[3])
    beta = float(values[4])
except:
    print("Введені значення повинні бути числами!")
    exit()


result = int(K1 * a1 + K2 * a2 - beta)

print("Результат обчислення формули: ", result)
