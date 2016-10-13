#Задача 5. Вариант 11.
#Напишите программу, которая бы при запуске случайным образом 
#отображала имя одного из девяти оленей Санта Клауса.

#Крутова Дарья
#15.09.2016

import random

oleni = ['Dasher',
		'Prancer',
		'Vixen',
		'Comet',
		'Cupid',
		'Donder',
		'Blitzen',
		'Rudolph']
olen = random.choice(oleni)
print('Программа случайным образом отображает имя одного из оленей Саны.')
print(olen)
input("\n\nHaжмитe Enter. чтобы выйти.")