# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.    
#     Примеры:    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90
# n = 0
# numbers = [0,0,0,0,0]
# length = 5
# index = 0
# while(n != length):
#     numbers[index] = int(input(f'Введите {index + 1} число + Enter  '))                                     
#     index += 1
#     n +=1
# print(numbers)    

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
num4 = int(input('Введите четвертое число: '))
num5 = int(input('Введите пятое число: '))
max = num1
if max < num2:
    max = num2
if max < num3:
    max = num3
if max < num4:
    max = num4
if max < num5:
    max = num5  
    
print(f"max = {max}")             

