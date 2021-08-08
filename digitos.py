# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
------------------------------------------------------------------------------

ENUNCIADO:
    "Faça um programa que leia um número inteiro n maior que zero e imprima os 
    dígitos verificadores de n. 
    
    Dígitos verificadores (DVs, check digit) são dígitos concatenados a valores 
    numéricos a fim de verificar a autenticidade ou detectar erros de digitação 
    como um algarismo digitado incorretamente ou alguma permutação de algarismos 
    adjacentes.
    
    No exercício, a lógica dos DVs utilizada foi a mesma que é utilizada para 
    verificar o CPF:
        dv1 = resto da divisão (1 × d1 + 2 × d2 + 3 × d3 + ⋯ + k × dk)/11
        
        dv2 = resto da divisão (0 × d1 + 1 × d2 + 2 × d3 + 3 × d4 + ⋯ + (k − 1) × dk + k × dv1)/11

        (caso o resto de alguma das divisões seja 10, o dv é 0)
    
    O programa pode supor,     sem verificar, que o dígito mais significado 
    de n é diferente de zero. Isso significa que seu programa pode supor que n 
    não é um número como 007, 012345678, 0009"
    
------------------------------------------------------------------------------

    Nome: Ana Oliveira Silva
    Data: 23/05/21

'''

# escreva seu programa a seguir


num = int(input("Digite n: "))
n = num
casas = 1
dv1 = 0
dv2 = 0
i = 1
j = 0
soma1 = 0
soma2 = 0
dec = 1

while (num // 10 != 0):
    dec = dec * 10
    num = num // 10
    casas = casas + 1

while (casas > 0):
    intermediario = n // dec
    soma1 = (i * intermediario) + soma1
    soma2 = (j * intermediario) + soma2
    i = i + 1
    j = j + 1
    n = n - ((n // dec) * dec)
    dec = dec // 10
    casas = casas - 1
    
dv1 = soma1 % 11

if (dv1 == 10):
    dv1 = 0

soma2 = soma2 + (j * dv1)

dv2 = soma2 % 11

if (dv2 == 10):
    dv2 = 0
    
print(f"DVs = {dv1} {dv2}")