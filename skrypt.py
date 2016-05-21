if 5>2:
	print('5 jest większe od 2')
else:
	print('5 nie jest większe od 2')


name=input('podaj imie:')
if name=='Kasia':
	print('Cześć, Wielgo!')
elif name=='Paulina':
	print('Cześć, Pinson')
elif name=='Tomasz':
	print('Cześć, Mentorze!')
else:
	print('Hej, nieznajomy')

glosnoscstr = input('podaj glosnosc:')
glosnosc = int(glosnoscstr)
if glosnosc <20:
	print('Prawie nic nie slychac')
elif 20 <= glosnosc <40:
	print('O,muzyka leci w tle')
elif 40 <= glosnosc <60:
	print('Idealnie, moge uslyszec wszystkie detale')
elif 60 <= glosnosc <80:
	print('Dobre na imprezy')
elif 80 <= glosnosc <100:
	print('Troszeczke za glosno!')
else:
	print('Ojoj! Moje uszy!')

def hej():
	print('Hej!')
	print('Jak się masz?')
hej()

