# НАПИШИТЕ ПРОГРАММУ КОТОРАЯ НА ВХОД ПРИНИМАЕТ 5 ЧИСЕЛ И НАХОДИТ МАКСИМАЛЬНОЕ ИЗ НИХ 

#ПРИМЕР 7,2,4,8,9,6,23,1
raw = input('Введите последовательность чисел через пробел: ')
int_array = [int(i) for i in raw.split(' ') if i.isdigit()]
max=0
for i in range(len(int_array)):
    if max<int_array[i]:
        max=int_array[i]

print(max)
