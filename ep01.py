# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
    --------------------------------------------------------------------------
    ENUNCIADO: "Vamos trabalhar alguns conceitos que vimos nas primeiras reuniões 
    tais como variáveis, valores e seus tipos e expressões. Este EP utiliza atribuições, 
    a função de entrada input(), de saída print(), as função de conversão de 
    valores int() e float().
    Faça um programa que leia uma string s, um número inteiro i e um número 
    real r e imprima, os resultados de algumas expressões envolvendo s, i e r 
    de maneira idêntica a dos exemplos a seguir."
    
    Exemplo:
    
    Digite uma string s: 2+13  

    Digite um inteiro i: 3  

    Digite um real r: 4  
    s+s = 2+132+13
    i+i = 6
    r+r = 8.0
    i*s = 2+132+132+13
    i*i = 9
    i*r = 12.0
    r/i = 1.3333333333333333
    2*i/i = 2.0
    i/i*2 = 2.0
    
    --------------------------------------------------------------------------

    Autora: Ana Clara Oliveira Silva
    Data: 27/04/21

'''

# escreva seu programa a seguir

string = input ('Digite uma string s: ')
inteiro = int (input ('Digite um inteiro i: '))
real = float (input ('Digite um real r: '))

print (f"s+s = {string + string}")
print (f"i+i = {inteiro + inteiro}")
print(f"r+r = {real + real}")
print (f"i*s = {inteiro * string}")
print (f"i*i = {inteiro * inteiro}")
print (f"i*r = {inteiro * real}")
print (f"r/i = {real / inteiro}")
print (f"2*i/i = {2 * inteiro / inteiro}")
print (f"i/i*2 = {inteiro / inteiro * 2}")
