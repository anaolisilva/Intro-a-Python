# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
------------------------------------------------------------------------------

ENUNCIADO: 
    "Três números inteiros positivos a, b e c, a < b < c, formam um trio pitagoreano 
    se a2 + b2 = c2 . Por exemplo, os números 3, 4, e 5 formam um trio pitagoreano 
    pois 32 + 42 = 52.
    Alguns números inteiros positivos podem ser escritos como a soma de um 
    trio pitagoreano. Chamamos esses número de pitagoreanos. Por exemplo, 12 é 
    um número pitagoreago ja que 12 = 3 + 4 + 5 e 3, 4 e 5 é um trio pitagoreano.
    
    Escreva um programa que leia um número inteiro positivo n e verifique se 
    ele é soma de um trio Pitagoreano. Em caso afirmativo, o seu programa deve 
    imprimir a mensagem n é pitagoreano (a,b,c). onde onde os valores a, b e c 
    formam um trio pitagoreano. Em caso contrário, o seu programa deve imprimir 
    a mensagem n não é pitagoreago.
    
    Se n é a soma de mais de um trio pitagoreano, então o trio (a,b,c) exibido 
    pelo seu programa deve ser aquele em que o valor de a é o maior. Por exemplo, 
    para n = 60 os trios pitagoreanos (10,24,26) e (15,20,25) são os únicos que 
    comprovam que 60 é pitagoreano. Nesse caso seu programa deve exibir a mensagem 
    60 é pitagoreano (15,20,25)."
    
------------------------------------------------------------------------------

    Nome: Ana Oliveira Silva
    Data: 01/06/21
   
"""

# Escreva seu programa a seguir

n = int(input("Digite n: "))
a = n//3
b = n//2
c = n - a - 1
pitagoreano = False
pitA = 1
pitB = 1
pitC = 1

    
while (c > 1):
    b = c - 1
    
    while (b > 1):
        a = n - c - b 
        
        if (a**2 + b**2 == c**2 and a > 0 and a + b + c == n):
            pitagoreano = True
            if (pitA < a and a < b and b < c):
                pitA = a
                pitB = b
                pitC = c
            
        b -= 1
    c -= 1
        

if (pitagoreano):
    print(f"{n} é pitagoreano ({pitA},{pitB},{pitC})")
else: 
    print(f"{n} não é pitagoreano")