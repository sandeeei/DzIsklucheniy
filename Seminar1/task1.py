# Реализуйте 3 метода, чтобы в каждом из них получить
# разные исключения
try:
    x = int(input("Введите первое число: "))
    print(x)
    b=int(input("Введите второе число не более 10: "))
    while (b > 10):
        print("Вы ввели не верное число")
        b=int(input("Введите второе число не более 10: "))

    a=x/b
    print(a)
        
except ValueError:
   print("Будте внимательны вы ввели не число: ")
except ZeroDivisionError:
    print("На ноль делить нельзя ")