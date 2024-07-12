calls = 0

def count_calls():      #подсчитывает вызовы остальных функций
    global calls
    calls +=1

def string_info():      # принимает аргумент - строку и возвращает кортеж из:
                        # длина строки, строка в верхнем регистре, и в нижнем регистре
    count_calls()
    string = input("произвольное слово: ")
    print((len(string), string.upper(), string.lower()))

def is_contains():
    count_calls()
    list_to_search = list()
    string = input("Слово: ")
    list_to_search.extend(list(input("Список слов: ").split(' ')))
    list_to_search = list(map(str.lower, list_to_search))

    if string.casefold() in list_to_search:
        print(True)
    else:
        print(False)

string_info()
is_contains()
is_contains()
print(calls)