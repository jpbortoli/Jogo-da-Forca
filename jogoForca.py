from funcoes import (limparTela, nomeCompetidor, nomeDesafiante, pedirDicas)

limparTela()
print ("Bem-vindo ao jogo da forca!")

desafiante = nomeDesafiante ("Informe o nome do desafiante: ")
competidor = nomeCompetidor ("Informe o nome do competidor: ")

limparTela()

palavraChave = input ("Desafiante informe a palavra chave aqui: ")
dicas = pedirDicas ("Desafiante informe três dicas:")

limparTela()
