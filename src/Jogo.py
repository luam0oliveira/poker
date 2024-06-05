# Serao entregues somente 5 cartas a cada jogador e nenhuma sera compartilhada
# Havera somente 3 jogadores, sendo 2 bots e 1 jogador humano
# A partida sempre se inicia com o jogador a esquerda (posicao 0)
# O jogador sempre esta no meio dos jogadores (posicao 1)
# Todos os jogadores comecam com 300 fichas


from Baralho import Baralho
from Bot import Bot
from Jogador import Jogador
from Mao import Mao
from utils import clear


class Jogo:
	def __init__(self):
		self.jogadores: list[Jogador] = []
		self.baralho: Baralho = Baralho()
		self.jogadores.extend([Bot(0, "BOT#00", Mao()),Jogador(1, "Jogador", Mao()), Bot(2, "BOT#01", Mao())])
		self.vez = 0
		self.aposta_minima = 5
		self.main_loop()
	

	def main_loop(self):
		self.iniciar_rodada()
		rodada = 0
		print("Mesa de poker")
		while True:
			rodada += 1

			for i in range(3):
				for j in range(5):
					self.jogadores[i].mao.adicionaCarta(self.baralho.retirarCarta())

			self.jogadores[1].mostrarMao()
			self.avisoDeConfimacao()
			while True:
				clear()
				print("========== Rodada %d ============"%rodada)
				if self.jogadores[self.vez].ativo:
					print("VEZ DE %s"%self.jogadores[self.vez].nome)
					if (isinstance(self.jogadores[self.vez], Bot)):
						self.decisaoBot()
					else:
						self.menu()
					
					self.avisoDeConfimacao()
				else:
					self.vez = (self.vez+1) % 3

				print("APOSTA ATUAL: ", self.aposta_atual)
				
				if self.verificaTermino() == 3:
					ganhador = self.verificaGanhador()
					self.jogadores[ganhador].fichas += self.aposta_atual
					for jogador in self.jogadores:
						if jogador.ativo:
							print("Mão do jogador %s"%jogador.nome)
							jogador.mostrarMao()
					print("===================")
					print("Ganhador %s" %self.jogadores[ganhador].nome)
					input("Rodada terminada")
					clear()
					break

			self.iniciar_rodada()

			cont = 0
			for jogador in self.jogadores:
				if jogador.ativo:
					cont+=1
			if cont == 1 or cont == 0:
				print("Jogo terminado.")

	def menu(self):
		jogador = self.jogadores[self.vez]
		self.vez = (self.vez + 1) % 3

		while True:
			if self.aposta_minima != jogador.apostando:
				if self.aposta_minima >= jogador.fichas:
					print("1 - All in\n2 - Desistir")
					op = input()
					if op == '1':
						self.vez = (self.vez + 1) % 3
						self.aposta_atual += jogador.fichas
						jogador.apostando += jogador.fichas
						jogador.apostar(jogador.fichas)
						print("Pagando e passando a vez.")
						break
					elif op == '2':
						jogador.ativo = False
						print("Voltando na proxima rodada.")
						break
					else:
						print("Ação não reconhecida.")
				else:
					print("1 - Check (Pagar %d)\n2 - Apostar\n3 - Desistir"% (self.aposta_minima - jogador.apostando))
					op = input()
					if op == '1':
						self.aposta_atual += self.aposta_minima
						jogador.apostando += self.aposta_minima
						jogador.apostar(self.aposta_minima)
						print("Pagando e passando a vez.")
						break
					elif op == '2':
						quantia = int(input("Quantidade para apostar: "))
						if jogador.apostar(quantia):
							self.aposta_atual += quantia
							print("Apostado")
							self.aposta_minima = max(self.aposta_minima, quantia)
							jogador.apostando += quantia
							break
						else:
							print("É necessário ter mais fichas.")
					elif op == '3':
						jogador.ativo = False
						print("Voltando na proxima rodada.")
						break
					else:
						print("Ação não reconhecida.")
			else:
				print("1 - Check\n2 - Apostar\n3 - Desistir")
				op = input()
				if op == '1':
					print("Passando a vez.")
					break
				elif op == '2':
					quantia = int(input("Quantidade para apostar: "))
					if jogador.apostar(quantia):
						self.aposta_atual += quantia
						print("Apostado")
						self.aposta_minima = max(self.aposta_minima, quantia)
						jogador.apostando += quantia
						break
					else:
						print("É necessário ter mais fichas.")
				elif op == '3':
					jogador.ativo = False
					print("Voltando na proxima rodada.")
					break
				else:
					print("Ação não reconhecida.")
	

	def verificaTermino(self):
		cont = 0
		for jogador in self.jogadores:
			if (jogador.ativo and (jogador.fichas == 0 or jogador.apostando == self.aposta_minima)) or not jogador.ativo:
				cont+=1
		return cont

	def decisaoBot(self):
		bot = self.jogadores[self.vez]
		if not isinstance(bot, Bot):
			return
		decisao = bot.decisao()
		self.vez = (self.vez+1) % 3

		if decisao == -1:
			print("Bot desistiu da rodada.")
			bot.ativo = False
		elif bot.apostando < self.aposta_minima:
			decisao = 0
		if decisao == 0:
			if bot.apostando == self.aposta_minima:
				print("Bot passou a vez.")
			else:
				if bot.apostar(self.aposta_minima - bot.apostando):
					print("Bot deu check.")
					self.aposta_atual += self.aposta_minima - bot.apostando
					bot.apostando += self.aposta_minima - bot.apostando
				else:
					print("Bot deu all-in")
					self.aposta_atual += bot.fichas
					bot.apostando += bot.fichas
					self.aposta_minima = max(self.aposta_minima, bot.fichas)
					bot.apostar(bot.fichas)
		elif decisao != -1:
			print("O bot apostou %d fichas"%decisao )
			self.aposta_minima = max(self.aposta_minima, decisao)
			bot.apostando += decisao
			bot.apostar(decisao)

	def avisoDeConfimacao(self):
		input("Aperte ENTER para continuar")

	def iniciar_rodada(self):
		self.baralho.regerarBaralho()
		for jogador in self.jogadores:
			jogador.apostando = 0
			if jogador.fichas > 0:
				jogador.ativo = True
			else:
				jogador.ativo = False
			jogador.mao.removerCartas()
		self.aposta_atual = 0
		self.aposta_minima = 5
		self.vez = 0
	
	def verificaGanhador(self):
		pontMaos = {}
		ganhadores = {}
		for jogador in self.jogadores:
			if jogador.ativo:
				pontMaos[jogador.id] = jogador.mao.verificaMao()
		
		if len(pontMaos) == 1:
			return list(pontMaos)[0]

		for combinacoes in range(9, -1,-1):
			for jogador in pontMaos:
				if pontMaos[jogador][combinacoes] != False:
					ganhadores[jogador] = pontMaos[jogador][combinacoes]
			if len(ganhadores) != 0:
				break

		if len(ganhadores) == 1:
			return list(ganhadores.keys())[0]

		ganhadores = list(sorted(ganhadores.items(), key=lambda x:x[1]))
		if ganhadores[-1][1] != ganhadores[-2][1]:
			return ganhadores[-1][0]

		return 1
	
					





