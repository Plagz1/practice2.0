def print_pack_report(n):
    for num in range (n, 0, -1):
        if num % 3 == 0 and num % 5 == 0:
            print(f"{num} - расфасуем по 3 или по 5")
        elif num % 5 == 0:
            print(f"{num} - расфасуем по 5")
        elif num % 3 == 0:
            print(f"{num} - расфасуем по 3")
        else:
            print(f"{num} - не заказываем!")

print_pack_report(54)