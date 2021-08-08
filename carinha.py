# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
------------------------------------------------------------------------------
    ENUNCIADO:
        "Escreva um programa que leia 2 números reais que correspondem às 
        coordenadas x e y de um ponto e imprima azul se o ponto (x, y) for azul 
        e branco se o ponto (x, y) for branco
        Os pontos nos contornos em linhas sólidas entre regiões azuladas e 
        brancas são azuis. Já, os pontos nos contornos em linhas tracejadas 
        são brancos."
        [A imagem está presente no repositório com o nome carinhaimg.png 
         e referenciada no README]
------------------------------------------------------------------------------

    Nome: Ana Clara Oliveira Silva
    Data: 21/05/21
    
"""

##################################################################
## ESCREVA SEU PROGRAMA ABAIXO


x = float(input("Digite x: "))
y = float(input("Digite y: "))
cor = "branco"

if 0 <= x <= 8 and 0 <= y <= 8:
    cor = "azul"

if (0 <= x < 1 or 7 < x <=8) and 0 <= y < 2:
    cor = "branco"
elif (1 <= x <= 3 or 5 <= x <= 7) and 7.25 <= y <= 7.75:
    cor = "branco"
elif 3.5 <= x <= 4.5 and 3.5 <= y <= 4.5:
    cor = "branco"
elif 3 <= x <= 5 and 1.5 < y < 2.5:
    cor = "branco"
elif 5 <= y <= 8 and 0 < x < 4:
    #olho esquerdo
    if ((x - 2)**2) + ((y - 6)**2) <= 1 and (x - 2)**2 + (y - 6)**2 > 0.5**2:
        cor = "branco"     
elif 5 <= y <= 8 and 4 < x < 8:
    #olho direito
    if ((x - 6)**2) + ((y - 6)**2) <= 1 and (x - 6)**2 + (y - 6)**2 > 0.5**2:
        cor = "branco"
elif 1 <= y < 5 and 0 < x < 8:
    #cantos da boca
    if ((x - 3)**2/0.5**2) + ((y - 2)**2) < 0.5**2:
        cor = "branco"
    elif ((x - 5)**2) + ((y - 2)**2) < 0.5**2:
        cor = "branco"

print (cor)
