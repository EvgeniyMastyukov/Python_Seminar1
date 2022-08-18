# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# not(x or y or z) == (not x and not y and not z)

def f(x, y, z):
    a = not (x or y or z)
    b = (not x and not y and not z)
    if a == b:
        return 'True'
    else:
        return 'False'

x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
print(f(x, y, z))

#Второй способ  
# a = not (x or y or z) 
# b = (not x and not y and not z)
# print(a==b)

# Третий способ 
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(not(x or y or z) == (not x and not y and not z))

