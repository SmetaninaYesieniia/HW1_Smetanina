#1. Сума чисел: обчисліть суму чисел у списку.
числа_користувача= input("Введи цілі числа через пробіл: ")
numbers = числа_користувача.split()
numbers = [int(number) for number in numbers]
total = 0
for number in numbers:
    total += number
print("Сума чисел:", total)


#2. Знайти мінімум: Визначити найменше число в списку.
числа_користувача= input("Введи цілі числа через пробіл: ")
numbers = числа_користувача.split()
numbers = [int(number) for number in numbers]
minimum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
print("Мінімум:", minimum)

#3. Перевертання списку: перевертання елементів у списку.
числа_користувача= input("Введи цілі числа через пробіл: ")
список = числа_користувача.split()
список = [int(number) for number in список]
повернений_список = []
for number in список:
    повернений_список = [number] + повернений_список
print("Перевернутий список:", повернений_список)

#4. Друкувати непарні числа: відобразити всі непарні числа зі списку.
числа_користувача= input("Введи цілі числа через пробіл: ")
список = числа_користувача.split()
numbers = [int(number) for number in список]
print("Непарні числа: ")
for число in numbers:
    if число %2 != 0:
        print(число)

#5. Помножити список: помножити кожен елемент у списку на задане число.
числа_користувача= input("Введи цілі числа через пробіл: ")
numbers = числа_користувача.split()
numbers = [int(number) for number in numbers]
множник = int(input("Введи цілe числo - множник: "))
result = []
for number in numbers:
    result.append(number * множник)
print("Результат множення:", result)

#1. Фільтрувати за умовою: витягувати зі списку числа, більші за X.
числа_користувача = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
X = int(input("Введи X: "))
результат = [число for число in список if число > X]
print("Числа більші за", X, ":", результат)

#2. Середнє додатних чисел: Знайдіть середнє додатних чисел.
числа_користувача  = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
додатні = [x for x in список if x > 0]
if додатні:
    середнє = sum(додатні) / len(додатні)
    print("Середнє додатних чисел:", середнє)
else:
    print("Немає додатних")

#3. Максимум у відфільтрованому списку: знайдіть максимальну кількість чисел, менших за X.
числа_користувача = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
X = int(input("Введи X: "))
менші = [x for x in список if x < X]
if менші:
    максимум = max(менші)
    print("Максимум серед чисел, менших за", X, ":", максимум)
else:
    print("Таких нема")

#4. Агрегована умовна сума: сума чисел, які діляться на Y.
числа_користувача = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
Y = int(input("Введи дільник Y: "))
сума = sum([x for x in список if x % Y == 0])
print(f"Сума чисел, які діляться на {Y}:", сума)

#5. Список квадратів: створіть список квадратів кожного числа.
числа_користувача = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
квадрати = [x**2 for x in список]
print("Квадрати чисел:", квадрати)

#6. Витяг додатних чисел: створіть новий список лише з додатними числами з заданого списку.
числа_користувача = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
додатні = [x for x in список if x > 0]
print("Додатні числа:", додатні)

#7. Фільтрувати рядки за префіксом: знайти всі рядки в списку, які починаються з указаного префікса.
слова_користувача = input("Введи слова через пробіл: ")
слова = слова_користувача.split()
префікс = input("Введи префікс: ")
відфільтровані = [слово for слово in слова if слово.startswith(префікс)]
print("Слова з префіксом", префікс, ":", відфільтровані)

#8. Сума перших N чисел: обчисліть суму перших N чисел у списку.
числа_користувача = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
N = int(input("кількість перших чисел: "))
if N <= len(список):
    сума = sum(список[:N])
    print(f"Сума перших {N} чисел:", сума)
else:
    print("N завелике")

#9. Знайти всі паліндроми: видобути всі паліндромні рядки зі списку.


#10. Перевірка подільності: зі списку чисел створіть новий список логічних значень, де кожен елемент вказує, чи ділиться відповідне число на даний дільник.
числа_користувача = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
дільник = int(input("Введи дільник: "))
логічні_значення = [x % дільник == 0 for x in список]
print("Результати:", логічні_значення)

#1. Фільтрувати за кількома умовами: числа, які діляться на X, але не діляться на Y.
числа_користувача = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
X = int(input("Введи дільник X: "))
Y = int(input("Введи число Y на яке не ділитеметься число: "))
результат = [num for num in список if num % X == 0 and num % Y != 0]
print(результат)

#2. Зведення вкладених списків: зведення списку списків в єдиний список.

#3. Складна маніпуляція рядками: виділіть і введіть великі літери в окремих підрядках.
текст = input("Введи текст: ")
великі_літери = ""
for символ in текст:
    if символ.isupper():
        великі_літери += символ
print("Великі літери:", великі_літери)

#4. Багаторівневе сортування: сортування за спаданням, потім за частотою.
числа_користувача = input("Введи числа через пробіл: ")
список = [int(x) for x in числа_користувача.split()]
список_сортований = sorted(список, reverse=True)
print( список_сортований)

#5. Об’єднати списки умовно: об’єднати два списки на основі умов.

#6. Агрегація словника: сума значень у словнику за ключем.

#7. Умовна заміна елементів: заміна елементів на основі стану.
числа_користувача= input("Введи цілі числа через пробіл: ")
список = числа_користувача.split()
список = [int(number) for number in список]
n=int(input("Введи число для умови"))
for i in range(len(список)):
    if список[i] > n:
        список[i] = 0
print(список)

#8. Підрахувати довжину рядків: підрахувати кількість рядків довжиною більше X.
n = int(input("Скільки рядків хочеш ввести? "))
рядки = []
for і in range(n):
    рядок = input("Введи рядок: ")
    рядки.append(рядок)
X = int(input("Введи число X: "))
total = 0
for рядок in рядки:
    if len(рядок) > X:
        total += 1
print(total)

#9. Об’єднати чергування: об’єднувати рядки по черзі з двох списків.
n1 = int(input("Скільки рядків буде в першому списку? "))
список1 = []
for і in range(n1):
    рядок = input("Введи рядок для першого списку: ")
    список1.append(рядок)
n2 = int(input("Скільки рядків буде в другому списку? "))
список2 = []
for і in range(n2):
    рядок = input("Введи рядок для другого списку: ")
    список2.append(рядок)
результат = []
довжина = max(len(список1), len(список2))
for i in range(довжина):
    if i < len(список1):
        результат.append(список1[i])
    if i < len(список2):
        результат.append(список2[i])
print("Об’єднаний список:")
for рядок in результат:
    print(рядок)

#10. Помножити, якщо: помножити числа на Y, якщо вони більші за X.
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