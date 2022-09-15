# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

file = '-3, -2, -1, 1, 2, 3'
with open('file.txt', 'w') as file:
    file.write('1 = -3 \n')
    file.write('2 = -2 \n')
    file.write('3 = -1 \n')
    file.write('4 = 1 \n')
    file.write('5 = 2 \n')
    file.write('6 = 3 \n')

position_1 = input('Введите номер первой позиции для поиска произведения: ')
position_2 = input('Введите номер второй позиции для поиска произведения: ')

for position_1 in file:
    print(position_1)

for position_2 in file:
    print(position_2)

composition = position_1 * position_2
print(composition)

#надеюсь, что хоть частично решала правильно, пусть даже код не работает((

