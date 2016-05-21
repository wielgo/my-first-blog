def hej(imie):
	if imie =='Kasia':
		print('Hej Kasia')
	elif imie =='Paulina':
		print('Hej Paulina!')
	else:
		print('Hej nieznajomy!')
hej('Kasia')

def siemka(imie):
	print('Siemka '+ imie +'!')
siemka('Andrzej')

dziewczyny = ['Kasia', 'Paulina', 'Dominika', 'Ada', 'Karolina']
for imie in dziewczyny:
 	hej(imie)
 	print('Kolejna dziewczyna')
for i in range(1, 7):
	print(i)
