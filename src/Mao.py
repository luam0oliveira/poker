from re import A
from Carta import Carta, Naipe, Numero


class Mao:
	def __init__(self, original: list[Carta] = []):
		self.cartasNumero: dict[int, list[Carta]] = {int(key.value): [] for key in list(Numero)}
		self.cartasNaipe: dict[int, list[Carta]] = {int(key.value): [] for key in list(Naipe)}
		self.cartas: list[Carta] = []

		for i in original:
			self.adicionaCarta(i)
	
	def adicionaCarta(self, carta: Carta):
		self.cartas.append(carta)
		self.cartasNumero[int(carta.numero.value)].append(carta)
		self.cartasNaipe[int(carta.naipe.value)].append(carta)
	
	def removerCartas(self):
		for i in self.cartasNaipe:
			self.cartasNaipe[i].clear()
		
		for i in self.cartasNumero:
			self.cartasNumero[i].clear()
		
		self.cartas.clear()
	
	def verificaMao(self) :
		return [
			self.highCard(),
			self.onePair(),
			self.twoPair(),
			self.threeOfKind(),
			self.straight(),
			self.flush(),
			self.full_house(),
			self.quadra(),
			self.straight_flush(),
			self.royal_flush()
		]
	
	# Maior carta
	def highCard(self):	
		maiorCarta = max(list(self.cartas))
		return maiorCarta
	
	# Um par
	def onePair(self):
		for numero in self.cartasNumero:
			if len(self.cartasNumero[numero]) == 2:
				return self.cartasNumero[numero][0]
		return False

	# Dois pares
	def twoPair(self):
		pares = []
		for numero in self.cartasNumero:
			if len(self.cartasNumero[numero]) == 2:
				pares.append(self.cartasNumero[numero][0])
		if len(pares) == 2:
			return sorted(pares)
		return False

	# Trinca
	def threeOfKind(self):
		for numero in self.cartasNumero:
			if len(self.cartasNumero[numero]) == 3:
				return self.cartasNumero[numero][0]
		return False
	
	# Sequencia
	def straight(self):
		numeros = []
		for numero in self.cartasNumero:
			if len(self.cartasNumero[numero]) != 0:
				numeros.append(self.cartasNumero[numero][0])
		
		if (len(numeros) == 5 and min(numeros).numero.value + 4 == max(numeros).numero.value):
			return max(numeros)
		return False
	
	# so ha cartas de uma naipe 
	def flush(self):
		naipes = []
		for naipe in self.cartasNaipe:
			if len(self.cartasNaipe[naipe]) != 0:
				naipes.append(self.cartasNaipe[naipe][0])
		if len(naipes) == 1:
			return naipes[0]
		return False

	# Par e trinca
	def full_house(self):
		cartas = []
		onePair = self.onePair()
		threeOfKind = self.threeOfKind()
		if onePair:
			cartas.append(onePair)
		if threeOfKind:
			cartas.append(threeOfKind)
		if len(cartas) == 2:
			return [self.onePair(), self.threeOfKind()]
		return False

	# Quatro cartas do mesmo numero 
	def quadra(self):
		for numero in self.cartasNumero:
			if len(self.cartasNumero[numero]) == 4:
				return self.cartasNumero[numero][0]
		return False

	# Straight e flush
	def straight_flush(self):
		straight = self.straight()
		if straight and self.flush():
			return straight
		return False

	# Straight e flush com as maiores cartas
	def royal_flush(self):
		straight_flush = self.straight_flush() 
		if (straight_flush and straight_flush.numero == Numero.A):
			return straight_flush
		return False
	# Traz somente as cartas na mao do jogador
	def __str__(self) -> str:
		return str(self.cartas)

		