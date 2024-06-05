from Carta import Carta, Naipe, Numero
from random import shuffle


class Baralho:
	def __init__(self):
		self.cartas:list[Carta] = []
		self.retiradas:list[Carta] = []
		self.gerarBaralho()


	def gerarBaralho(self):
		numeros = Numero.__members__
		naipes = Naipe.__members__
		for naipe in naipes:
			for numero in numeros:
				carta = Carta(Numero[numero], Naipe[naipe])
				self.cartas.append(carta)
		shuffle(self.cartas)
	
	def regerarBaralho(self):
		self.cartas.extend(self.retiradas)
		shuffle(self.cartas)
		self.retiradas.clear()


	def retirarCarta(self):
		carta = self.cartas.pop()
		self.retiradas.append(carta)
		return carta
	
	def __str__(self) -> str:
		return str(self.cartas)
