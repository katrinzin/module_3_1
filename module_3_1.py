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
    string = str(input("Слово: "))
    list_to_search = list(str(input("Список слов: ")))

    if string in list_to_search:
        print(True)
    else:
        print(False)

string_info()
is_contains()
is_contains()
print(calls)