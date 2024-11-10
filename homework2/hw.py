while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        print(f'{a} + {b} =',a+b)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите число.")
