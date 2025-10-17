# Домашнє завдання:

# Задача 1. Середнє трьох чисел
# Користувач вводить три числа. Обчисли середнє арифметичне.
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))
print("The average of your three numbers is", ((num1 + num2 + num3) / 3 ))

# Задача 2. Остача від ділення
# Користувач вводить два числа. Знайди остачу від ділення першого на друге.
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print("The remainder of dividing your first number by the seconds is", (num1 % num2))


# Задача 3. Подвоєне число
# Користувач вводить число. Виведи подвоєне значення цього числа.
num = float(input("Enter your number: "))
num *= num
print("Double the value of this number is", num )

# Задача 4. Конвертація хвилин у секунди
# Користувач вводить кількість хвилин. Обчисли, скільки це буде секунд.
minutes = int(input("Enter minutes: "))
print(minutes," minutes is", minutes*60 , " seconds" )

# Задача 5. Кількість яблук на кожного
# Є n яблук і k учнів. Скільки яблук отримає кожен учень, якщо ділити порівну, і скільки залишиться?
count_of_student = int(input("Enter count of students: "))
count_of_apples = int(input("Enter count of apples: "))
if (count_of_apples % count_of_student) == 0:
    print("Each student will receive", count_of_apples // count_of_student , " apples without any remainder")
else: 
    print("Each student will receive", count_of_apples // count_of_student , " apples and" , count_of_apples % count_of_student , "apples will remain")


# Задача 6. Остання цифра числа
# Користувач вводить число. Виведи його останню цифру.
num = int(input("Enter integer number: "))
num %= 10
print("The last digit of your number is", num)


# Задача 7*. Обмін змінних
# Користувач вводить два числа. Після цього потрібно “поміняти” їх місцями і вивести результат.
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num1 , num2 = num2 , num1
print("After the exchange, the first number is", num1 , " and the second is ",  num2)