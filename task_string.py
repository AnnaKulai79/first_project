# name = "Alica"
# print(f"Hello, {name}! How are you")

# String (рядки)
# Напишіть програму, яка приймає від користувача рядок, і відображає цей рядок
#  у верхньому і нижньому регістрах.
# string1 = input("Enter data: ")
# print(string1.lower())
# print(string1.upper())


# Скласти програму, яка запитує назву баскетбольної команди і повторює її на 
# екрані зі словами: 
# This is a champion!.
# string1 = input("Enter the name of a basketball team: ")
# print(string1.capitalize(), "!!! This is a champion!")

# Дано натуральне число. Знайти число, що отримується при прочитанні його цифр справа наліво.
# string1 = input("Enter the natural number: ")
# print(string1[::-1])

# Дано рядок. Змініть регістр символів в цьому рядку так, щоб перша буква кожного слова була великою, а інші літери - малими. (метод s.title())
# string1 = input("Enter the string: ")
# print(string1.title())

# Дано рядок. Визначити порядковий номер першої вказаної букви. Якщо такої літери немає, вивести нуль.
# string1 = input("Enter the string: ")
# letter1 = input("Enter the letter: ")
# if string1.find(letter1) == -1:
#     print("0")
# else:    
#     print(string1.index(letter1) + 1)

# Напишіть програму, яка по введеному числу n від 1 до 9 виводить на екран n 
# пінгвінів з відповідним номером - число від 1 до n. Зображення одного 
# пінгвіна має розмір 5 x 9 символів, між двома сусідніми пінгвінами також є
# порожній (з пропусків) стовпець. Дозволяється вивести порожній стовпець 
# після останнього пінгвіна. Для спрощення малювання скопіюйте пінгвіна із 
# вихідних даних. Врахуйте, що виведення на екран виконується порядково, а не
#  «попінгвінно».
#  Вхідні дані: 
#  4 
#  Вихідні дані: 
#     _~_        _~_        _~_        _~_ 
#    (o o)      (o o)      (o o)      (o o) 
#   /  V  \    /  V  \    /  V  \    /  V  \ 
#  /(  1  )\  /(  2  )\  /(  3  )\  /(  4  )\ 
#    ^^ ^^      ^^ ^^      ^^ ^^      ^^ ^^
# count = int(input("Enter number of penguins(1-9): "))
# print("    _~_    " * count)
# print("   (o o)   " * count)
# print("  /  V  \  " * count)
# str4 = ""
# for i in range(count):
#     str4 = str4 + f" /(  {i + 1}  )\ "
# print(str4)
# print("   ^^ ^^   " * count)


# У рядку є кілька слів, розділених одним або декількома пропусками. Потрібно прибрати з тексту зайві пропуски: два і більше пропусків поспіль, а також всі пропуски на початку і в кінці рядка. На вхід програмі подається рядок, що складається не більше ніж з 255 символів. Надрукувати новий рядок.
# Вхідні дані:
#    Beyond the green     swelling hills of the     Mittel Land rose mighty slopes of forest    up    to the lofty steeps of the Carpathians    themselves
# Вихідні дані:
# Beyond the green swelling hills of the Mittel Land rose mighty slopes of forest up to the lofty steeps of the Carpathians themselves
# s = input("Enter string: ")
# print(" ".join(s.split()))


# Дано рядок, що складається з n цифр (тобто одноцифрових чисел), між якими стоїть n-1 знаків операцій, кожна з яких може бути або +, або -. Обчисліть значення цього виразу. Програма має надрукувати результат обчислення цього виразу.
# Вхідні дані:
# 5-3+1
# 6+3-2
# Вихідні дані:
# 3
# 7
# s = input("Enter data: ")
# print(eval(s))

# Напишіть програму, на вхід якої даються чотири числа a, b, c і d, кожне у своєму рядку. Програма повинна вивести фрагмент таблиці множення для всіх чисел відрізка [a; b] на всі числа відрізка [c; d]. Числа a, b, c і d є натуральними і не перевищують 10, a ≤ b, c ≤ d. Дотримуйтесь формату виведення як у вихідних даних. Для поділу елементів всередині рядка використовуйте \t - символ табуляції. Зауважте, що лівим стовпчиком і верхнім рядком виводяться самі числа із заданих відрізків.
# Вхідні дані:
# 1
# 4
# 2
# 5
# Вихідні дані:
# 	2	3	4	5
# 1	2	3	4	5
# 2	4	6	8	10
# 3	6	9	12	15
# 4	8	12	16	20
# print("Enter data: ")
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a > 9) or (b > 9) or (c > 9) or (d > 9) or (a > b) or (c > d):
#     print("Invalid data!")
# else:
#     for i in range(a-1,b + 1):
#         str_print = ""
#         if i == (a - 1):
#             str_print = str_print + " \t"
#             ind = 1
#         else:
#             str_print = str_print + str(i) + "\t"
#             ind = i
#         for j in range(c,d + 1):
#             str_print = str_print + str(j * ind) + "\t"
#         print(str_print)
          



# Напишіть програму для друку літери A за допомогою введеного користувачем символа.
#  Вхідні дані: 
#  * 
#  Вихідні дані: 
#    *** 
#   *   * 
#   *   * 
#   ***** 
#   *   * 
#   *   * 
#   *   * 
# print("Enter symbol: ")
# symbol = input()
# print(f"   {symbol}{symbol}{symbol} ")
# print(f"  {symbol}   {symbol} ")
# print(f"  {symbol}   {symbol} ")
# print(f"  {symbol}{symbol}{symbol}{symbol}{symbol} ")
# print(f"  {symbol}   {symbol} ")
# print(f"  {symbol}   {symbol} ")
# print(f"  {symbol}   {symbol} ")

# Напишіть програму, яка визначає, чи є у введеному рядку десяткові цифри, і виводить найбільше число, яке можна скласти з цих цифр. Провідних нулів у числі бути не повинно (за винятком числа 0, запис якого містить рівно одну цифру). Гарантовано, що у рядку є принаймні одна цифра. Вхідний рядок містить довільні символи. Програма повинна вивести найбільше число, яке можна скласти з присутніх в рядку десяткових цифр.
# Вхідні дані:
# Release Date: July 27, 2008
# Last Updated: February 22, 2018
# Вихідні дані:
# 872200
# 822210
# print("Enter data: ")
# string1 = input()
# num_str = ""
# for i in string1:
#     if i.isdigit():
#         num_str = num_str + i
# print(''.join(sorted(num_str))[::-1])
