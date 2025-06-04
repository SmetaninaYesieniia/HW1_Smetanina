#завдання1
vitannia="Hello, Python World!"
print(vitannia)

#завдання2
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
print("Додавання:", a + b)
print("Віднімання:", a - b)
print("Множення:", a * b)
print("Ділення:", a / b)

#завдання3
рядок1 = "Кирило Ясуда - "
рядок2 = "топ!"
mix = рядок1 + рядок2
print(mix)
print("Довжина:", len(mix))

#завдання4
number = float(input("Введіть число: "))
if number % 2 == 0:
    print("Парне")
else:
    print("Непарне")

#завдання5
for i in range(1, 11):
    print(i)


#завдання6
num = float(input("Введіть число: "))
if num > 0:
    print("Позитивний")
elif num < 0:
    print("Негативний")
else:
    print("Нуль")


#завдання7
for i in range(1, 11):
    if i % 2 == 0:
        print(i)


#завдання8
n = int(input("Введіть пліз число n: "))
total = 0
for i in range(1, n+1):
    total += i
print("Сума від 1 до", n, "дорівнює", total)


#завдання9
print("Зворотний відлік від 10 до 1:")
for i in range(10, 0, -1):
    print(i)


#завдання10
for i in range(1, 11):
    if i == 5:
        continue
    if i == 7:
        break
    print(i)