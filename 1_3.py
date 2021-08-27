for num in range(1, 101):
    units = num % 100 % 10
    if units == 1 and num % 100 != 11:
        print(f"{num} процент")
    elif units in (2, 3, 4) and num % 100 not in (12, 13, 14):
        print(f"{num} процента")
    else:
        print(f"{num} процентов")


