print("----------------------")
print(".::Média Calculator::.")
print("----------------------")

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
materia = input("Qual a matéria? ")

n1 = float(input("Insira sua primeira nota? "))
n2 = float(input("Insira sua segunda nota? "))

media = n1 + n2 / 2

import os
os.system ('cls')

print("----------------------")
print(".::Média Calculator::.")
print("----------------------")
print("")
print("Nome: ", nome)
print("Idade: ", idade)
print("Matéria: ", materia)
print("A média final das duas notas é ", media)