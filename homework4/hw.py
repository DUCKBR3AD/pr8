a = int(input("Введите значение нижней границы: "))
b = int(input("Введите значение верхней границы: "))
try:
    except ValueError:
        print("Ошибка:некорректный ввод")
        break
if a > b:
    for i in range(a+1,b):
        print(i)
    else:
        print("Ошибка: нижняя граница не может быть больше верхней")
        break
