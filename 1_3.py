for num in range(1, 101):
    units = num % 100 % 10
    if units == 1 and num % 100 != 11:
        print(f"{num} процент")
    elif (units == 2 or units == 3 or units == 4) and (num % 100 != 12 and num % 100 != 13 and num % 100 != 14):
        print(f"{num} процента")
    else:
        print(f"{num} процентов")


