﻿#Задача 6. Вариант 24.

#Создайте игру, в которой компьютер загадывает название одной из четырех основных мастей лошадей, а игрок должен ее угадать.

#Cheraneva A.S.
#25.03.2016

import random
m=('Вороная', 'Гнедая', 'Серая', 'Рыжая')
a=random.randint(0,2)
rand=m[a]
print('Как вы думаете, название какой из четырех основным мастей лошадей я загадал? Вороная, Гнедая, Серая или Рыжая?')

otvet=0
while (otvet)!=(rand):
	otvet=input('Введите название масти:')
	if (otvet)!=(rand):
		print('Вы не угадали,попробуйте снова.')
	elif (otvet)==(rand):
		print('Вы угадали.')
		break
input('Нажмите Enter для выхода.')


