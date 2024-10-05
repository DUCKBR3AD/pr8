sum = 0

while True:
    inp = input("Введите число или 'stop' или 'end' для завершения ввода: ")

    if inp == "stop" or inp =="end"  :
        break

    try:
        num = float(inp)
        sum += num
    except ValueError:
        print("Ошибка: введите корректное число ")

print("Сумма введённых чисел: ", sum)

