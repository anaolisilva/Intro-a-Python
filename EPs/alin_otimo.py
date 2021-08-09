# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
------------------------------------------------------------------------------

ENUNCIADO:
    "Nesse exercício daremos continuidade ao EP10 encontrando alinhamentos de 
    maior pontuação entre variações de duas sequências de DNA. Para usar as 
    funções pontuacao() e gera_gaps() do arquivo alinhamento.py, o arquivo 
    alin_otimo.py carrega as funções definidas no alinhamento.py usando o 
    comando import alinhamento as alin."

------------------------------------------------------------------------------

    Nome: Ana Oliveira Silva
    Data: 06/07/21

'''

# módulo alinhamento: alin.gera_gaps(), alin.pontuacao()
import alinhamento as alin

# Constantes
# use essas constantes caso desejar
DNA = 'ATCG'
GAP = '_'

#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''

    ## exemplos de chamada da função do módulo alinhamento
    print('Testes das funções do módulo alinhamento:')
    print(alin.gera_gaps( 'T' ))
    print(alin.gera_gaps( 'CA' ))
    print(alin.gera_gaps( 'AT_G' ))

    print(alin.pontuacao('T_', 'CT', 1, 5, 6, 3))
    print(alin.pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3))
    print(alin.pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4))
    print(alin.pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2))
    print()

    ## Escreva aqui os testes para a função gera_n_gaps()
    print()
    print()
    print('Testes da função gera_n_gaps:')
    print(gera_n_gaps('T', 2))
    print(gera_n_gaps( 'CA', 2 ))
    print(gera_n_gaps( 'AT_G', 2 ))

    ## Escreva aqui os testes para a função pontuacao_max()
    print()
    print()
    print('Testes da função pontuacao_max:')
    print(pontuacao_max('T_CG', 'ATCG', 5, 4, 3, 2))
    print(pontuacao_max('T_CGTAC', 'ATCG_T_', 0, 1, 4, 3, 2))
    print(pontuacao_max('AT_', 'A_T', 2, 5, 1, 0, 2))
    
    

    
    print("Fim dos meus testes.")

#------------------------------------------------------------------
#
def gera_n_gaps( dna, n = 1 ):
    '''( str, int ) -> list

    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (gap), e um número inteiro positivo `n`.
 
    RETORNA uma lista sem repetições com todas as variações de `dna` 
    com até `n` gaps extras.

    EXEMPLOS:
 
    In [1]: gera_n_gaps( 'T', 2 )
    Out[1]: ['T', '_T', 'T_', '__T', '_T_', 'T__']
    
    In [2]: gera_n_gaps( 'CA', 2 )
    Out[2]: ['CA', '_CA', 'C_A', 'CA_', '__CA', '_C_A', '_CA_', 'C__A', 'C_A_', 'CA__']
    
    In [3]: gera_n_gaps( 'C_A', 2)
    Out[3]: ['C_A', '_C_A', 'C__A', 'C_A_', '__C_A', '_C__A', '_C_A_', 'C___A', 'C__A_', 'C_A__']
    '''
    # modifique o código abaixo para conter a sua solução.
    
    lista = [dna]
    copia = dna
    nova = []
    final = dna + (n * GAP)
    i = 0
    
    
    while final not in lista:
        alin.gera_gaps(copia)
        nova = alin.gera_gaps(copia)[:]
        j = 0
        while (j < len(nova) - 1):
            if (nova[j] in lista):
                nova = nova[:j] + nova[j+1:]
                j -= 1
            j += 1
                
                
        lista += nova
        copia = lista[i+1]
        i += 1
        

    return lista

#------------------------------------------------------------------
#
def pontuacao_max(s, t, ga, la, ldif, lgap, n = 1):
    '''(str, str, int, int, int, int, int) -> int, list de list

    RECEBE:

        - duas strings `s` e `t` de mesmo comprimento representando fitas de DNA 
          com os símbolos 'A', 'T', 'C', 'G' e '_' (gap); e
        - quatro números inteiros `ga`, `la`, `ldif` e `lgap` como no EP10;
        - mais um número inteiro positivo `n`.

    RETORNA 

        - a maior pontuação entre pares de variações de s e t que têm:

              * o mesmo comprimento; 
              * até `n` gaps extras.

        - uma lista com todos os pares de variações de s e t que têm 
          esta maior pontuação; cada par é uma lista com duas variações.

    Exemplos:

    In [1]: pontuacao_max('T_CG', 'ATCG', 5, 4, 3, 2)
    Out[1]: (15, [['_T_CG', 'AT_CG']])

    In [2]: pontuacao_max('T_CGTAC', 'ATCG_T_', 0, 1, 4, 3, 2)
    Out[2]: (-5, [['_T_CG_TAC', 'AT_CG_T__']])

    In [3]: pontuacao_max('AT_', 'A_T', 2, 5, 1, 0, 2)
    Out[3]: (16, [['_A_T_', '_A_T_'], 
                  ['A__T_', 'A__T_'], 
                  ['A_T__', 'A_T__']])
    '''
    # modifique o código abaixo para conter a sua solução.
    #Gerar as duas listas
    #Pontuar os pares
    #Fazer a comparação de se for maior
    
    ss = gera_n_gaps(s, n)[:]
    tt = gera_n_gaps(t, n)[:]
    par = []
    pmax = alin.pontuacao(ss[0], tt[0], ga, la, ldif, lgap)
    lista = []   
    
    for i in range(1, len(ss), 1):
        for j in range(1, len(tt), 1):
            if len(ss[i]) == len(tt[j]):
                p = alin.pontuacao(ss[i], tt[j], ga, la, ldif, lgap)
                
                if (p == pmax):
                    par = [ss[i]]
                    par += [tt[j]]
                    lista += [par]
                    
                elif (p > pmax):
                    par = [ss[i]]
                    par += [tt[j]]
                    lista = [par]
                    pmax = p
                
    
    return pmax, lista
    

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
