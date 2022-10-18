import os
def limparTela():
    os.system ("cls")

def loginDesafiante (nomeDesafiante):
    nome = input (nomeDesafiante)
    return nome

def loginCompetidor (nomeCompetidor):
    nome = input (nomeCompetidor)
    return nome

def pedirDicas (dicas):
    numero = 0
    while numero < 3:
        numero = numero + 1
        input (f"Informe a {numero}º dica\n")