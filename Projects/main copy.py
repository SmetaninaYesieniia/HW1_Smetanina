числа_користувача = input("Введи цілі числа через пробіл: ")
numbers = [int(n) for n in числа_користувача.split()]
X = int(input("Введи число X: "))
Y = int(input("Введи множник Y: "))
result = []
for number in numbers:
    if number > X:
        result.append(number * Y)
    else:
        result.append(number)
print(result)