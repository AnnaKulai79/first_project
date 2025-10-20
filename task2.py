# Ви придбали товар на певну суму s. Скільки купюр різного номіналу треба віддати продавцю, якщо починати платити з найбільших? У вас є 1, 2, 5, 10, 100, 500 гривень.
# summ_of_purchase = int(input("Enter the amount of your purchase: "))
# count_of_500 = summ_of_purchase // 500
# summ_of_purchase %= 500
# count_of_100 = summ_of_purchase // 100
# summ_of_purchase %= 100
# count_of_50 = summ_of_purchase // 50
# summ_of_purchase %= 50
# count_of_10 = summ_of_purchase // 10
# summ_of_purchase %= 10
# count_of_5 = summ_of_purchase // 5
# summ_of_purchase %= 5
# count_of_2 = summ_of_purchase // 2
# summ_of_purchase %= 2
# count_of_1 = summ_of_purchase

# print("You need to give", count_of_500 , " bills of 500 hryvna,",
#                           count_of_100 , " bills of 100 hryvna,",
#                           count_of_50 , " bills of 50 hryvna,",
#                           count_of_10 , " bills of 10 hryvna,",
#                           count_of_5 , " bills of 5 hryvna,",
#                           count_of_2 , " bills of 2 hryvna,",
#                           count_of_1 , " bills of 1 hryvna,")

# Розгалудження

# Напишіть програму, в якій користувач вводить пароль і якщо він співпадає із наперед визначеним паролем для цього користувача, то виводиться повідомлення Password accepted.. У іншому випадку повідомлення буде Sorry, that is the wrong password..
# password = "12345"
# input_password = input("Enter your pass: ")
# if password == input_password:
#     print("Password accepted")
# else: 
#     print("Sorry, that is the wrong password")
# Користувачем вводиться два імені. Використовуючи конструкцію розгалуження програма повинна вивести імена в алфавітному порядку.
# name1 = input("Enter first name: ")
# name2 = input("Enter second name: ")
# if name1 < name2:
#     print(name1, ", ", name2)
# else:
#     print(name2, ", ", name1)

# Напишіть програму, яка виводить назви введених чисел. Користувач вводить ціле число. Якщо це число або 1 або 2 або 3, то виводиться повідомлення - назва числа, відповідно, One, Two, Three. В усіх інших випадках виводиться слово Unknown.
# num1 = int(input("Enter your number: "))
# match num1:
#     case 1:             
#         print("Your number is one")
#     case 2:             
#         print("Your number is two")
#     case 3:             
#         print("Your number is three")
#     case _:
#         print("Your number is unknown")

# Користувач вводить дві різних англійські літери в окремих рядках. Напишіть програму, яка виводить повідомлення про місце розташування однієї літери відносно іншої у алфавіті.
# letter1 = input("Enter first letter: ")
# letter2 = input("Enter second letter: ")
# if letter1 < letter2:
#     print("In alphabetical order, first comes", letter1 , ", then", letter2)
# else:
#     print("In alphabetical order, first comes", letter2 , ", then", letter1)

# 5. Напишіть програму, в якій користувач вводить значення температури, і, якщо це значення менше або дорівнює 0 градусів Цельсія, необхідно вивести повідомлення A cold, isn’t it?. Якщо ж температура становить більше 0 і менше 10 градусів Цельсія повідомлення буде Cool., у інших випадках Nice weather we’re having..
# temperature = float(input("Enter your temperature: "))
# if temperature <= 0:
#     print("A cold, isn’t it?")
# elif (temperature > 0) & (temperature <= 10):
#     print("Cool")
# else:
#     print("Nice weather we’re having")

# Середній рівень

# Визначте назву геометричної фігури за введеною кількістю її сторін. Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін поза межами цього діапазону, програма повинна відображати відповідне повідомлення.
# number_of_sides = int(input("Input number of sides: "))
# match number_of_sides:
#     case 3:             
#         print("Your figure is triangle")
#     case 4:             
#         print("Your figure is rectangle")
#     case 5:             
#         print("Your figure is pentagon")
#     case 6:             
#         print("Your figure is hexagon")
#     case _:
#         print("Your figure is unknown")



# Ігрове поле рулетки поділено на номери від 0 до 36, які мають чорний, червоний або зелений кольори. Номер 0 має зелений колір, для номерів від 1 до 10, непарні номери - червоні, а парні - чорні. Непарні номери від 11 до 18 - чорні, а парні номери - червоні. Непарні номери від 19 до 28 - червоні, а парні номери - чорні. Непарні номери від 29 до 36 - чорні, а парні номери - червоні. Напишіть програму, яка отримує номер (число від 0 до 36) та показує, чи є номер зеленим, червоним або чорним. Програма повинна враховувати варіант, якщо користувач вводить номер, який знаходиться за межами діапазону від 0 до 36.
# numb1 = int(input("Enter your number from 0 to 36: "))
# if (numb1 >= 0) and (numb1 <= 36):
#     if numb1 == 0:
#         print("Your number is green")
#     elif numb1 % 2:
#         if ((numb1 > 0) and (numb1 <= 10)) or ((numb1 >= 19) and (numb1 <= 28)):
#             print("Your number is red")
#         else:
#             print("Your number is black")
#     else:
#         if ((numb1 > 0) and (numb1 <= 10)) or ((numb1 >= 19) and (numb1 <= 28)):
#             print("Your number is black")
#         else:
#             print("Your number is red")
# else:
#     print("The number you entered is out of range")

# Дано дві точки: A (x1, y1) і B (x2, y2). Напишіть програму, яка визначає, яка із точок знаходиться далі від початку координат.

#  Вхідні дані: 
#  1 
#  2 
#  3 
#  2 
#  4 
#  4 
#  4 
#  4 

#  Вихідні дані: 
#  B 
#  The distance is the same
# print("Input data: ") 
# numb11 = float(input())
# numb12 = float(input())
# numb21 = float(input())
# numb22 = float(input())
# value_of_print = "  "
# if ((numb11 == numb21) and (numb12 == numb22)) or ((numb11 == numb22) and (numb12 == numb21)):
#     value_of_print = " The distance is the same "
# elif numb11 > numb21:
#     value_of_print = "A"
# elif numb11 < numb21:
#     value_of_print = "B"
# else:
#     if numb12 > numb22:
#         value_of_print = "A"
#     elif numb11 < numb21:
#         value_of_print = "B"
# print(value_of_print)

# Вводяться координати (x, y) точки A і радіус кола (r). Визначити, чи належить дана точка колу,
#  якщо його центр знаходиться в початку координат.
# Вхідні дані:
# 3
# 4
# 5
# -2
# 5
# 3
# Вихідні дані:
# The point belongs to the circle
# The point is outside the circle
# print("Input data: ") 
# koord1 = float(input())
# koord2 = float(input())
# radius = float(input())
# value_of_print = " The point is outside the circle "
# d = (koord1 ** 2 + koord2 ** 2) ** 0.5
# if radius == d:
#     value_of_print = "The point belongs to the circle"
# print(value_of_print)


# Дано натуральное число. Визначити, чи закінчується число парною цифрою.
# Вхідні дані:
# 1234
# 35
# Вихідні дані:
# True
# False
# print("Input data: ") 
# number = float(input())
# print(bool(number%2 - 1))

# Напишіть програму для знаходження коренів квадратного рівняння a*x2 + b*x + c = 0. 
# Користувач вводить значення коефіцієнтів a, b, c. У вхідних даних наведено
# три пари вхідних значень коефіцієнтів, а у вихідних даних - відповідні 
# повідомлення про кількість коренів або їх відсутність.
# Вхідні дані:
# 8
# 4
# 2
# 3.6
# 10
# -3
# 2
# 4
# 2
# Вихідні дані:
# No roots.
# 0.27 and -3.05
# -1.00
# print("Input data: ") 
# number_a = float(input())
# number_b = float(input())
# number_c = float(input())
# diskriminant = number_b ** 2 - 4 * number_a * number_c
# if diskriminant == 0:
#     print(round((-(number_b / (2 * number_a))),2))
# elif diskriminant > 0:
#     print(round((-(number_b + diskriminant ** 0.5) / (2 * number_a)),2), "and ",
#           round((-(number_b - diskriminant ** 0.5) / (2 * number_a)),2))
# else:
#    print("No root")
 

# Відомі рік і номер місяця народження людини, а також рік і номер місяця 
# сьогоднішнього дня (січень - 1 і т. д.). Визначити вік людини (число повних років). 
# У разі збігу вказаних номерів місяців вважати, що пройшов повний рік.
# Вхідні дані:
# 1998
# 3
# 2018
# 2
# Вихідні дані:
# 19
# print("Input data: ") 
# year_of_birthday = int(input())
# month_of_birthday = int(input())
# year_of_today = int(input())
# month_of_today = int(input())
# age = year_of_today - year_of_birthday
# if month_of_today < month_of_birthday:
#     age -=1
# print(age)



# Дано чотирицифрове число. Замінити усі парні цифри числа на символ * і вивести число.
# Вхідні дані:
# 2358
# 2227
# 1353
# Вихідні дані:
# *35*
# ***7
# 1353
print("Input data: ") 
number = int(input())
number_print = ""
for i in range(4):
    if (number%10)%2:
        number_print = number_print + str(number % 10)
    else:
        number_print = number_print + '*'
    number //= 10 
print(number_print[::-1])