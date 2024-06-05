from Carta import Carta, Naipe, Numero
from Mao import Mao


class Jogador:
	def __init__(self, id, nome, mao: Mao):
		self.id = id
		self.nome = nome
		self.mao: list[Carta] = mao
		self.ativo = True
		self.apostando = 0
		self.fichas = 300
	
	def apostar(self, fichas: int):
		if fichas <= self.fichas:
			self.fichas -= fichas
			return True
		return False

	def mostrarMao(self):
		print("Cartas na mão: ")
		for carta in self.mao.cartas:
			print("%s%s"%(self.mostrarNumero(carta.numero), self.mostrarNaipe(carta.naipe)))

	
	def mostrarNumero(self, numero:Numero):
		match numero:
			case Numero.A:
				return "A"
			case Numero.N2:
				return "2"
			case Numero.N3:
				return "3"
			case Numero.N4:
				return "4"
			case Numero.N5:
				return "5"
			case Numero.N6:
				return "6"
			case Numero.N7:
				return "7"
			case Numero.N8:
				return "8"
			case Numero.N9:
				return "9"
			case Numero.N10:
				return "10"
			case Numero.J:
				return "J"
			case Numero.Q:
				return "Q"
			case Numero.K:
				return "K"
			case _:
				return ""
	def mostrarNaipe(self, naipe: Naipe):
		if naipe == Naipe.COPA:
			return "♥"
		elif naipe == Naipe.ESPADAS:
			return "♠"
		elif naipe == Naipe.OURO:
			return "♦"
		return "♣"
	
	def __str__(self) -> str:
		return str(self.fichas)
		
					