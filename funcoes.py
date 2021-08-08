# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
------------------------------------------------------------------------------

ENUNCIADO:
    "Neste exercício você escreverá quatro função: primo(), goldbach(), 
    exponencial() e logistica(). O cabeçalho de cada função contém sua instrução."
    
------------------------------------------------------------------------------

    Nome: Ana Clara Oliveira Silva
    Data: 09/06/21

"""

#----------------------------------------------------    
def primo(n):
    '''(COMENTÁRIO DOS PROFESSORES) 
        (int) -> bool

       RECEBE um número inteiro n.
       RETORNA True se n é primo e False em caso contrário.
    '''
    # remova o print() e escreva sua função a seguir 
    
    i = 3
    
    if (n == 2 or n == 3):
        return True
    elif (n == 1 or n % 2 == 0 or n < 1):
        return False
    else:
        while (i < (n/2) + 1):
            if (n % i == 0):
                return False
            i += 2
        
    return True
         

#----------------------------------------------------        
def goldbach(n):
    '''(COMENTÁRIO DOS PROFESSORES)
        (int) -> bool, int, int 

       RECEBE um número inteiro n.
       RETORNA True, p, q se n é soma de dois números primos p e q.
       Se n não é soma de dois números primos a função retorna False, 1, 1.
    '''
    # remova o print() e escreva sua função a seguir 
    
    '''Todo número primo é ímpar, porque todo par é divisível por 2.
    Toda soma entre números ímpares é um número par, portanto, só é possível
    que b retorne verdadeiro se n é par; a não ser que (n-2) seja primo.
    Se todo primo é ímpar, o incremento da verificação de p pode ir de 2 em 2, 
    pois não é necessário verificar somas de números pares.
    '''
    
    
    b = False
    p = 2
    q =  n - p
    
    if(primo(q) and primo(p)):
        b = True
        return b, p, q

    p = 3
    q = n - p
    
    while (p < n//2 and b == False):
        if(primo(q) and primo(p)):
               b = True
               return b, p, q
        p += 2
        q = n - p
                
    if (not b):
        p = 1
        q = 1
        return b, p, q

#----------------------------------------------------    
def exponencial(n0, e, p, d):
    '''(COMENTÁRIO DOS PROFESSORES)
    (int, int, float, int) -> int 

       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * um inteiro d,  d >=  0. 

      RETORNA o número total de indivíduos infectados até o dia d 
      determinado por (n0, e, p).
    '''
    
    i = (1 + e * p)**d * n0
    i = int(i)
    
    return i
    
    
#--------------------------------------------------
def logistica(n0, e, p, n, d):
    '''(COMENTÁRIO DOS PROFESSORES)
    (int, int, float, int, int) -> int
 
       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * o número n de indivíduos na população; e
         * um inteiro d, d >= 0. 

       RETORNA o número total de indivíduos infectados até o dia d 
       determinado por (n0, e, p, n).

    '''
    diaAntes = 1 #diasAntes é como se fosse o n(d-1)
    anterior = 1 #anterior recebe 1 porque n0 = 1
    
    while (d != 1 and diaAntes <= (d - 1)):
        anterior = (1 + (e * p *(1 - anterior/n))) * anterior
        diaAntes += 1
    
        
    i = (1 + (e * p *(1 - anterior/n))) * anterior
    
    i = int(i)
    
    return i