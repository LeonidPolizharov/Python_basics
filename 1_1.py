duration = -1
while duration < 0:
    duration = int(input('Введите положительное число секунд: '))


seconds = (duration % 60)
minutes = (duration // 60 % 60)
hours = (duration // 3600 % 24)
days = (duration // 86400)          # 3600 * 24

print(f"{days} дн {hours} ч {minutes} мин {seconds} сек")
