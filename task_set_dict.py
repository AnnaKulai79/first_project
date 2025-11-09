# # Tasks for lesson on the topic of "set() | dict()"
# ```
# new_set = set()
# new_set2 = {1, 5, 2}
# ```
# ```
# new_dict = {}
# new_dict2 = {"key": "value", "key2": "value2"}
# ```


# *Beginner level*
# 1. Створіть словник зі списками добрих справ на сьогодні і на завтра. Надрукуйте із словника добрі справи, які плануєш зробити сьогодні і взавтра.
def task1():
    good_things = {
        "today" : ["read", "clean", "dog"],
        "tomorrow" : ["read", "call"]
        }
    print("Today :")
    for i in good_things["today"]:
        print("-", i)
    print("Tomorrow :")
    for i in good_things["tomorrow"]:
        print("-", i)

# 2. Припустимо, що у нас є словник, в якому ключі є ідентифікаторами, а значення – іменами користувачів. Напишіть програму, яка виводить вітальне повідомлення користувачу на основі його ідентифікатора. Якщо ідентифікатор відсутній у словнику, виводиться вітання для усіх користувачів.
#     Вхідні дані:
#     232
#     550
#     190
#     500
#     Вихідні дані:
#     Hi, Alice!
#     Hi, Bob!
#     Hi, Jack!
#     Hi, to all!
def task2():
    users = {
        0: "Alice",
        1: "Bob",
        2: "Jack"
        }
    id = int(input("Enter id: \n"))
    if id in users:
        print(f"Hi, {users[id]}!")
    else:
        print("Hi, to all!")

# 3. Напишіть програму для сортування за зростанням (за алфавітом) словника за ключами. Словник зберігає пари ключ-значення у вигляді «назва фільму: рік релізу». Інформація виводиться як у вихідних даних: сортування має бути проведено за назвами фільмів.
#     Вихідні дані:
#     ('Avengers: Endgame', 2019) ('Guardians of the Galaxy', 2014) ('Iron Man', 2008) ('Thor', 2011)
def task3():
    films = {
        'Thor': 2011,
        'Avengers: Endgame': 2019,
        'Iron Man': 2008,
        'Guardians of the Galaxy': 2014
        }
    sorted_films = dict(sorted(films.items()))
    for i in sorted_films.items():
        print(f"{i}", end=" ")
# task3()


# 4. Надрукуйте елементи словника, де ключі - це числа від '1' до 'n' (обидва числа включно), а значення - квадрати ключів. 'n' – ціле число, яке вводить користувач.
def task4():
    num = int(input("Enter number: \n"))
    # dict_num = {}
    # for i in range(1,num + 1):
    #     dict_num.update({i: i ** 2})
    dict_num = {i: i ** 2 for i in range(1, num +1)}
    print(dict_num)


# 5. Створіть словник, в кому ключі – назви днів тижня, а значення - цілі числа, що позначають порядковий номер дня тижня від 0 до 6. Надрукуйте назву дня за введеним порядковим номером дня. Якщо введений номер виходить за межі, програма жодних повідомлень не друкує і не повідомляє про помилку.
def task5():
    week = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
        }
    num = int(input("Enter number(0-6): \n"))
    key = next((k for k, v in week.items() if v == num), None)
    if key != None:
        print(key)


# 6. Напишіть програму для створення словника із введеного рядка символів для підрахунку кількості символів.
#     Вхідні дані:
#     Lorem ipsum dolor sit amet
#     Вихідні дані:
#     {'L': 1, 'o': 3, 'r': 2, 'e': 2, 'm': 3, ' ': 4, 'i': 2, 'p': 1, 's': 2, 'u': 1, 'd': 1, 'l': 1, 't': 2, 'a': 1}
def task6():
    str1 = list(input("Enter text: \n"))
    # symb = {i : str1.count(i) for i in str1}
    symb = {}
    for i in str1:
        symb[i] = symb.get(i, 0) + 1
    print(symb)
# task6()

# 7. Напишіть програму, яка приймає рядок символів, і обчислює кількість букв і цифр.
#     Вхідні дані:
#     Project Gutenberg offers over 59,000 free eBooks
#     Вихідні дані:
#     LETTERS 36
#     DIGITS 5
def task7():
    str1 = list(input("Enter text: \n"))
    symb = {
        "DIGITS": 0,
        "LETTERS": 0
    }
    for i in str1:
        if i.isdigit():
            symb["DIGITS"] += 1
        elif i.isalpha():
            symb["LETTERS"] += 1
    [print(k, v) for k, v in symb.items()]
# task7()


# *Middle level*
# 8. Напишіть програму для видалення дублікатів зі списку цілих чисел.
def task8():
    num1 = input("Enter list of numbers: \n")
    num1 = " ".join(list(set(num1.split())))
    print(num1)


# 9. Дано список словників. Кожен словники має 2 пари елементів: ключ 'name' і значення імені студента, ключ 'points' і значення - список балів з різних дисциплін (цілі двоцифрові числа). Надрукуйте найменші значення балів, отримані кожним студентом, в один рядок з пропуском.
def task9():
    students = [
        {"name": "Alan", "points": [10, 12, 9, 8, 10]},
        {"name": "Jack", "points": [11, 6, 12, 3, 4]},
        {"name": "Alla", "points": [12, 12, 5, 9, 9]}
        ]
    min_scores = [min(st["points"]) for st in students]
    print(*min_scores)

# 10. Дано два списки чисел. Порахуйте, скільки унікальних цифр міститься в обох з них.
def task10():
    lst1 = [1, 4, 5, 8, 9, 4]
    lst2 = [6, 7, 3, 11, 2, 1, 7]
    print(len(set(lst1 + lst2)))
# lst1.union(lst2)     lst1 | lst2
# lst1.difference(lst2)     lst1 - lst2
# lst1.symetric_difference(lst2)     lst1 ^ lst2
# lst1.intersection(lst2)     lst1 & lst2



# 11. Дано три словники, в яких ключами є малі букви латинського алфавіту, а значеннями - цілі числа. Ключі у всіх словниках – різні, їх є по 3 в кожному словнику. Об’єднайте всі три словники в один і виведіть його вміст. Підказка. скористайтеся оператором **, що використовується для об’єднання довільної кількості словників.
def task11():
    dict1 = {'L': 1, 'o': 3, 'r': 2}
    dict2 = {'e': 2, 'm': 3, 'y': 4}
    dict3 = {'i': 2, 'p': 1, 's': 2}
    dict4 = {**dict1, **dict2, **dict3}
    print(dict4)

# 12. Створіть словник, який відображає ідентифікатори акцій на біржі. Ключами словника є ідентифікатори акцій, а значеннями - дійсні числа - ціни акцій. Надрукуйте ціни акцій та ідентифікатори у порядку зростання ціни.
#     Вихідні дані:
#     10.75 FB
#     37.2 HPQ
#     45.23 ACME
#     205.55 IBM
#     612.78 AAPL
def task12():
    stocks = {
        "AAPL": 178.25,
        "GOOGL": 134.50,
        "MSFT": 320.10,
        "TSLA": 256.75,
        "AMZN": 145.30
        }
    sort_dict = dict(sorted(stocks.items(), key=lambda x:x[1]))
    [print(v, k) for k, v in sort_dict.items()]


# 13. В рядку записаний текст. Словом вважається послідовність непробільних символів, які йдуть підряд, слова розділені одним або більшим числом пропуском або символами кінця рядка. Для кожного слова з цього тексту підрахуйте, скільки разів воно зустрічалося в цьому тексті раніше.
#     Вхідні дані:
#     var list set tuple list tuple tuple dict var
#     Вихідні дані:
#     0 0 0 0 1 1 2 0 1
def task13():
    str1 = "var list set tuple list tuple tuple dict var".split()
    res = []
    for i in range(len(str1)):
        res.append(str1[:i].count(str1[i]))
    print(*res)



# *Hard level*
# 14. Напишіть програму, яка зможе підрахувати слова у введеному рядку, розділені пропуском і вивести отриману статистику: для кожного унікального слова обчислити число його повторень (без урахування регістру), слова не повинні повторюватися, порядок слів довільний.
#     Вхідні дані:
#     a bb acD bb abc ac BCD a
#     Вихідні дані:
#     a 2
#     bb 2
#     acd 1
#     abc 1
#     ac 1
#     bcd 1
def task14():
    str1 = "a bb acD bb abc ac BCD a"
    str1 = str1.lower().split()
    dict1 = {}
    for i in str1:
        dict1[i] = dict1.get(i, 0) + 1
    [print(k, v) for k, v in dict1.items()]



# 15. Дано два списки чисел. Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх у порядку зростання.
#     Вхідні дані:
#     2 5 8 11 10 9
#     11 3 7 6 8 5
#     Вихідні дані:
#     5 8 11
def task15():
    lst1 = set(map(int, "2 5 8 11 10 9".split()))
    lst2 = set(map(int, "11 3 7 6 8 5".split()))
    lst1 = list(lst1 & lst2)
    print(*sorted(lst1))


# --------------------------
# 16. Напишіть програму, яка вміє шифрувати і розшифровувати використовуючи шифр підстановки. Програма приймає на вхід два рядки однакової довжини, у першому рядку записані символи початкового алфавіту, у другому рядку - символи кінцевого алфавіту (шифр підстановки), після чого йде рядок, який потрібно зашифрувати переданим шифром підстановки, і ще один рядок, який потрібно розшифрувати. Нехай, наприклад, на вхід програми передано:
#     abcd
#     *d%#
#     abacabadaba
#     #*%*d*%
#     Це означає, що символ a вхідного повідомлення замінюється на символ `*` в шифрі, `b` замінюється на `d`, `c` - на `%` і `d` - на `#`. Потрібно зашифрувати рядок abacabadaba і розшифрувати рядок `#*%*d*%` за допомогою цього шифру. Отримуємо наступні рядки, які і передаємо на виведення програми:
#     *d*%*d*#*d*
#     dacabac
#     Вхідні дані:
#     abcd
#     1234
#     ababcdcd
#     44332211
#     Вихідні дані:
#     12123434
#     ddccbbaa
def task16():
    str1 = list("abcd")
    str2 = list("1234")
    str3 = list("ababcdcd")
    str4 = list("44332211")
    dict1 = dict(zip(str1, str2))
    dict2 = dict(zip(str2, str1))
    res1, res2 = "", ""
    for i in str3:
        res1 += dict1[i]
    for i in str4:
        res2 += dict2[i]
    print(res1)
    print(res2)
task16()