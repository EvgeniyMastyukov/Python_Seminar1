# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

num_of_coordinate = int(input('Введите номер четверти: '))

if num_of_coordinate == 1:
    print('любой x > 0 and любой y > 0')
elif num_of_coordinate == 2:
    print('любой x < 0 and любой y > 0')
elif num_of_coordinate == 3:
    print('любой x < 0 and любой y < 0')
elif num_of_coordinate == 4:
    print('любой x > 0 and любой y < 0')
else:
    print('Введите корректно номер четверти (от 1 до 4)')
