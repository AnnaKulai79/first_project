# Сума двох чисел: Написати програму, яка зчитує два цілих числа та виводить їх суму.
n1 = int(input("Enter first integer number1: "))
n2 = int(input("Enter second integer number2: "))
print("The sum of your numbers is", n1 + n2)

# Гіпотенуза: За двома катетами прямокутного трикутника знайти довжину його гіпотенузи.
leg1 = int(input("Enter first leg1: "))
leg2 = int(input("Enter second leg2: "))
print("The hypotenuse is", ( leg1 ** 2 + leg2 ** 2 ) ** 0.5)

# Двічі: Написати програму, яка зчитує ціле число та виводить його двічі.
num = int(input("Enter integer number: "))
print(num,",",num)

# Привіт, <ім'я>: Написати програму, яка запитує ім'я користувача і виводить привітання.
name1 = input("Enter your name: ")
print("Hello ", name1, "!")

# Прощавай, <ім'я>: Написати програму, яка запитує ім'я користувача і виводить прощання.
name1 = input("Enter your name: ")
print("Goodbye ", name1, "!")

# Вік через рік: Напишіть програму, яка запитує ім'я користувача та його вік. Потім виведіть повідомлення, яке повідомляє, скільки йому буде років через рік.
name1 = input("Enter your name: ")
age1 = int(input("Enter your age: "))
print("Hello ", name1, "! Your age after 1 year will be", age1)

# Площа прямокутника: Напишіть програму, яка запитує довжину та ширину прямокутника, а потім обчислює та виводить його площу.
height1 = int(input("Enter height of a rectangle: "))
width1 = int(input("Enter width of a rectangle: "))
print("The area is", height1 * width1)

# Конвертер валют: Запропонуйте користувачеві ввести суму в одній валюті (наприклад, доларах), а потім виведіть цю суму в іншій валюті (наприклад, євро), використовуючи заздалегідь визначений коефіцієнт обміну.
currency = int(input("Enter your amount in dollars: "))
koef = 1.17
print("Your amount in euros will be ",  currency * koef)

# Вартість покупки: Запитайте користувача назву товару, його ціну та кількість. Обчисліть загальну вартість покупки та виведіть її на екран.
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
product_quantity = int(input("Enter quantity: "))
print("The cost of your",product_name, " purchase is", product_price * product_quantity, " Euros")

# Температура: Напишіть програму, яка перетворює температуру з градусів Цельсія на Фаренгейт. Запитайте користувача температуру в градусах Цельсія.
temp_in_celsius =  float(input("Enter temperature in Celsius: "))
print("Your temperature in Fahrenheit is", (temp_in_celsius * 1.8 +32))