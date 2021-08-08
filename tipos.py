# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
------------------------------------------------------------------------------
    ENUNCIADO:
        Faça um programa que leia:

        uma string s,
        um número inteiro i e
        um número real x
        e imprima as mensagens e os resultados das expressões como mostrado nos exemplos a seguir. 

        Exemplo:
            
            Digite uma string s: 2 * 5 + 7 

            Digite um inteiro i: 5 
        
            Digite um float x: 2.5 
            s = '2 * 5 + 7' (<class 'str'>)
            i = 5 (<class 'int'>)
            x = 2.5 (<class 'float'>)
            s + s = '2 * 5 + 7' + '2 * 5 + 7' = '2 * 5 + 72 * 5 + 7' (<class 'str'>)
            i + i = 5 + 5 = 10 (<class 'int'>)
            x + x = 2.5 + 2.5 = 5.0 (<class 'float'>)
            i * s = 5 * '2 * 5 + 7' = '2 * 5 + 72 * 5 + 72 * 5 + 72 * 5 + 72 * 5 + 7' (<class 'str'>)
            i * i = 5 * 5 = 25 (<class 'int'>)
            i * x = 5 * 2.5 = 12.5 (<class 'float'>)
            x / i = 2.5 / 5 = 0.5 (<class 'float'>)
            i / i = 5 / 5 = 1.0 (<class 'float'>)
            i // i = 5 // 5 = 1 (<class 'int'>)
            i / 2 * 3 = 5 / 2 * 3 = 7.5 (<class 'float'>)
            i // 2 * 3 = 5 // 2 * 3 = 6 (<class 'int'>)
            i % 3 = 5 % 3 = 2 (<class 'int'>)
                        
------------------------------------------------------------------------------

    Nome: Ana Clara Oliveira Silva
    Data: 11/05/21
    
'''
# escreva seu programa a seguir
    
s = input ("Digite uma string s: ")
i = int(input("Digite um inteiro i: "))
x = float(input("Digite um float x: "))


print (f"s = '{s}' ({type(s)})")
print (f"i = {i} ({type(i)})")
print (f"x = {x} ({type(x)})")
print (f"s + s = '{s}' + '{s}' = '{s + s}' ({type(s)})")
print (f"i + i = {i} + {i} = {i + i} ({type(i)})")
print (f"x + x = {x} + {x} = {x + x} ({type(x)})")
print (f"i * s = {i} * '{s}' = '{i * s}' ({type(i * s)})")
print (f"i * i = {i} * {i} = {i*i} ({type (i*i)})")
print (f"i * x = {i} * {x} = {i*x} ({type (i*x)})")
print (f"x / i = {x} / {i} = {x/i} ({type(x/i)})")
print (f"i / i = {i} / {i} = {i/i} ({type (i/i)})")
print (f"i // i = {i} // {i} = {i//i} ({type (i//i)})")
print (f"i / 2 * 3 = {i} / 2 * 3 = {i/2 * 3} ({type (i/2 * 3)})")
print (f"i // 2 * 3 = {i} // 2 * 3 = {i // 2 * 3} ({type (i // 2 * 3)})")
print (f"i % 3 = {i} % 3 = {i % 3} ({type(i % 3)})")




