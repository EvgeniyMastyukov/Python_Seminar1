# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Пример: - 6 -> да
#         - 7 -> да
#         - 1 -> нет
numweek = int(input('Введите цифру, обозначающую день недели(от 1 до 7):  '))
while (1 > numweek or numweek > 7):
    numweek = int(input('Введите цифру, обозначающую день недели:  '))
if numweek == 1:
    print('нет')
elif numweek == 2:
    print('нет')
elif numweek == 3:
    print('нет')
elif numweek == 4:
    print('нет')
elif numweek == 5:
    print('нет')
elif numweek == 6:
    print('да')
elif numweek == 7:
    print('да')

