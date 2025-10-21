# Beginner level

# Виведіть повідомлення Hello, Python! на екран n разів (n - ціле число, яке вводить користувач).
# number = int(input("Enter your number: "))
# a = 0
# while a < number:
#     a += 1
#     print("Hello, Python!")

# Дано два цілих числа a і b (a ≤ b). Виведіть всі числа від a до b включно.
# print("Enter two number(a<=b): ")
# a = int(input())
# b = int(input())
# print("*" * 20)
# for i in range(a,b+1):
#     print(i)


# Напишіть програму-таймер зворотного відліку, яка запитує у користувача кількість секунд n, з якої слід починати відлік.
# Вхідні дані:
# 5
# Вихідні дані:
# 5
# 4
# 3
# 2
# 1
# Start!
# input_sek = int(input("Enter the number of seconds: "))
# a = 0
# while a < input_sek:
#     a += 1
#     print(a)
# print("Start!")

# Користувач вводить кількість навчальних предметів n, а потім, відповідно, оцінки учня з n навчальних предметів. Визначте середню оцінку.
# count_of_subjects = int(input("Enter number of subjects: "))
# a = 0
# grades = 0
# while a < count_of_subjects:
#     print("Enter the name of subject: ")
#     input()
#     print("Enter grades: ")
#     grades  += int(input())
#     a += 1
# print("Average grade is", grades / count_of_subjects)


# Надрукувати у рядку m разів число n. Числа m і n - цілі числа, які вводить користувач у порядку n, m.
# Вхідні дані:
# 10
# 5
# Вихідні дані:
# 10 10 10 10 10
# n = int(input("Enter the number: "))
# m = int(input("Enter the number of repeats: "))
# print("*" * 20)
# for i in range(m):
#     print(n, end=" ")
# print("")

# Напишіть програму для друку цілих чисел від n до 0 із виведенням біля кожного числа кількості символів #, що дорівнює значенню числа.
# Вхідні дані:
# 6
# Вихідні дані:
# 6 ######
# 5 #####
# 4 ####
# 3 ###
# 2 ##
# 1 #
# num = int(input("Enter the number: "))
# for i in range(num):
#     print(num, "#" * num)
#     num -= 1


# Напишіть програму для побудови шаблону як у вихідних даних за введеним значенням n.
# Вхідні дані:
# 9
# Вихідні дані:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
# num = int(input("Enter the number: "))
# for i in range(num+1):
#     for j in range(i):
#         print(i, end="")
#     print("")
    

# Middle level

# Намалювати сходинки як у вихідних даних, використовуючи символи пропуску і решітки #, коли на вхід програми подається ціле число n - кількість сходинок.
# Вхідні дані:
# 4
# Вихідні дані:
# #
# ##
# ###
# ####
# num = int(input("Enter the number: "))
# for i in range(num):
#     print("#" * (i + 1))


# За даним цілим додатнім числом n обчисліть n! - значення факторіалу цього числа.
# Факторіал: n! = 1 * 2 * 3 * ... * (n-1) * n
# num = int(input("Enter the number: "))
# result = 1
# for i in range(num):
#     result *= i + 1
# print(f"{num}!= {result}")

# Автогонщик в перший день ралі проїхав d км. Кожен наступний день він збільшував пробіг на 10% від пробігу попереднього дня. Через скільки днів автоспортивних змагань сумарний пробіг автомобіля за всі дні перевищить t км і яке значення сумарного пробігу? Введення даних користувачем відбувається в порядку: d, t.
# Вхідні дані:
# 10
# 200
# Вихідні дані:
# 211.14 km, 33 days
# num_d = float(input("Enter d: "))
# num_t = float(input("Enter t: "))
# a = 0
# count = 0
# while a <= num_t:
#     a += num_d
#     num_d *= 1.1
#     count +=1
# print(a)
# print(count) 

# Дано ціле число n. З чисел 1, 4, 9, 16, 25, …​ надрукувати ті, які не перевищують n. (зверніть увагу на задану послідовність)
# num = int(input("Enter the number: "))
# a = 1
# step = 1
# while a < num:
#     print(a)
#     step += 2
#     a += step


# Дано цілі числа a і b. Обчислити a ^ b (a в степені b), не використовуючи операцію піднесення до степеня.
# num_a = int(input("Enter the number a: "))
# num_b = int(input("Enter the number b: "))
# res = 1
# for i in range(num_b):
#     res *= num_a
#     print(res)
# print(f"{num_a}^{num_b} = {res}")

# Hard level

# Дано натуральне число n. Визначити, чи є воно автоморфним числом.
# Примітка: Автоморфне число - число, квадрат якого рівний останнім розрядами квадрата цього числа: 5 - 25, 6 - 36, 25 - 625.
# Вхідні дані:
# 9376
# 26
# Вихідні дані:
# True
# False
# str_num = input("Enter your number: ")
# print(int(str_num) == ((int(str_num) ** 2) % (10 ** len(str_num))))


# Дано натуральне число n. Надрукуйте всі n-значні непарні натуральні числа в порядку спадання.
# Вхідні дані:
# 1
# 2
# Вихідні дані:
# 9 7 5 3 1
# 99 97 95 93 91 89 87 85 83 81 79 77 75 73 71 69 67 65 63 61 59 57 55 53 51 49 47 45 43 41 39 37 35 33 31 29 27 25 23 21 19 17 15 13 11
# num = int(input("Enter the number: "))
# a = 10 ** num - 1
# while a > 0:
#     print(a, end=" ")
#     a -= 2

# Написати програму для обчислення суми цифр цілого числа n. Програма має враховувати, що на вхід може подаватися ціле від’ємне число.
# num = int(input("Enter the number: "))
# if num < 0:
#     num *= -1

# str_num = str(num)
# res2 = 0
# for j in range(len(str_num)):
#     res2 += int(str_num[j])
# print(res2)

# res = 0
# for i in range(len(str(num))):
#     res += num % 10
#     num //= 10
# print(res)


# Напишіть програму для отримання рядка Фібоначчі від 0 до n, де n - ціле число.
# Послідовність Фібоначчі - це серія чисел 0, 1, 1, 2, 3, 5, 8, 13, 21, .... Кожне наступне число знайдено шляхом додавання двох номерів перед ним.
# Вхідні дані:
# 50
# Вихідні дані:
# 1 1 2 3 5 8 13 21 34
# num = int(input("Enter the number: "))
# a = 0
# set_fib = [0,1]
# count = 0
# while set_fib[count] <= num:
#     a += set_fib[count] + set_fib[count + 1]
#     set_fib.append (set_fib[count] + set_fib[count + 1])
#     print(set_fib[count], end=" ")
#     count += 1
 

# За введеним користувачем цілим числом n визначте n-е число Фібоначчі.
# Вхідні дані:
# 9
# 3
# 5
# Вихідні дані:
# 34
# 2
# 5
# num = int(input("Enter the index Fibonacci sequence: "))
# a = 0
# set_fib = [0,1]
# count = 0
# while count < num:
#     a += set_fib[count] + set_fib[count + 1]
#     set_fib.append (set_fib[count] + set_fib[count + 1])
#     count += 1 
# print(set_fib[num-1])