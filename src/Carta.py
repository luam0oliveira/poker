from enum import Enum

# Enums feitos para facilitar desenvolvimento
# Para naipe: 0: ouro, 1: espadas, 2: copa, 3: paus
class Naipe(Enum):
	OURO = 0
	ESPADAS = 1
	COPA = 2
	PAUS = 3

# Para numero da carta: 2 a 14, sendo 14 = As
class Numero(Enum):
	N2 = 2
	N3 = 3
	N4 = 4
	N5 = 5
	N6 = 6
	N7 = 7
	N8 = 8
	N9 = 9
	N10 = 10
	J = 11
	Q = 12
	K = 13
	A = 14

	def __lt__(self, other):
		return self.value < other.value


class Carta:
	def __init__(self, numero: Numero, naipe: Naipe):
		self.numero = numero
		self.naipe = naipe

	def __str__(self) -> str:
		return self.numero.name + " " + self.naipe.name

	def __repr__(self) -> str:
		return self.__str__()
	
	def __gt__(self, other):
		return self.numero.value > other.numero.value

	def __eq__(self, other) -> bool:
		if not isinstance(other, Carta):
			return False
		return self.numero.value == other.numero.value