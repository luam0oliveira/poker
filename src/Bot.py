from math import ceil
from random import randint
from Jogador import Jogador
from Mao import Mao


class Bot(Jogador):
	def __init__(self, id, nome, mao: Mao):
		super().__init__(id, nome, mao)
	
	def decisao(self):
		mao = self.mao.verificaMao()
		
		cont = 0
		for comb in mao:
			if comb != False:
				cont += 1
		
		if 3 < randint(0, 10):
			return -1
		else:
			if 5 + cont * 0.5 >= randint(0, 10):
				return int(ceil(cont * 0.2 * self.fichas))
			else:
				return 0
			
