# 2)Напишите функцию, которая принимает список, из списка выдает случайное значение из списка и записывает результат в txt файл. Список language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
import random

def test(language_list):
    random_value = random.choice(language_list)
    print(f"Случайное значение: {random_value}")
    
    # Записываем результат в файл
    with open("output.txt", "a") as file:
        file.write(random_value + "\n")

language = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]

test(language)

# 3)names = [“azat”, “zina”, “kuma”, “anna”, “sas”] Вывести с помощью lambda функции имена палиндромы
names = ["azat", "zina", "kuma", "anna", "sas"]

test = lambda s: s == s[::-1]

palindromes = list(filter(test, names))
print("Палиндромы:", palindromes)

# 4)Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
def test(rows):
    for i in range(1, rows + 1):
        print(f"Строка {i}: {'0' * 5}")
test(5)
