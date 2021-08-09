# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS 
#------------------------------------------------------------------
     
'''
------------------------------------------------------------------------------

ENUNCIADO:
    "Sequenciamento é o processo para determinar a ordem precisa de nucleotídeos 
    de uma determinada molécula de DNA. É usado para determinar a ordem das 
    quatro bases adenina ('A'), guanina ('G'), citosina ('C') e timina ('T'), 
    em uma fita de DNA. Assim, (fitas de) DNAs são representados por strings 
    dos caracteres 'A', 'C', 'G' e 'T'.
    
    Um alinhamento de duas sequências de DNA s e t é obtido adicionando-se os 
    chamados gaps, representados pelo caractere ‘_’ (underscore), a essas strings 
    de modo que fiquem com um mesmo comprimento."
    
------------------------------------------------------------------------------

    Nome: Ana Oliveira Silva
    Data: 06/07/21
    
'''
# Constantes
# use essas constantes caso desejar
DNA = 'ATCG'
GAP = '_'


#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    
    print("main(): início dos testes")
    print ("gera_gaps: ")
    print (gera_gaps( 'T' ))
    print (gera_gaps( 'CA' ))
    print (gera_gaps( 'AT_G' ))
    print (gera_gaps( 'TTAC_G' ))

    print("\npontuacao: ")
    print(pontuacao('T_', 'CT', 1, 5, 6, 3)) #-9
    print(pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3)) #12
    print(pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4)) #-10
    print(pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2))   #9 
      
    print("main(): fim dos testes")


#------------------------------------------------------------------
#
def gera_gaps( dna ):
    ''' ( str ) -> list

    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (GAP).

    RETORNA uma lista com todas as variações de dna com um símbolo GAP 
    a mais e sem repetições.

    exemplos: 
    In  [1]: gera_gaps( 'T' )
    Out [1]: ['_T', 'T_']
    
    In  [2]: gera_gaps( 'CA' )
    Out [2]: ['_CA', 'C_A', 'CA_']
    
    In  [3]: gera_gaps( 'AT_G')
    Out [3]: ['_AT_G', 'A_T_G', 'AT__G', 'AT_G_'] 
    '''
    # modifique o código abaixo para conter a sua solução.
    
    ini = 0
    fim = len(dna)
    meio = 1
    lista = []
    
    if(len(dna) == 1 or dna[0] != GAP):
        lista = [GAP + dna]    
    
    for meio in range(1, len(dna), 1):
        novo = dna[ini:meio] + GAP + dna[meio:fim]
        if novo not in lista:
            lista += [novo]
        
    
    if(dna[len(dna)-1] != GAP):
        lista += [dna + GAP]
        
        
    return lista

#------------------------------------------------------------------
#
def pontuacao(s, t, ga, la, ldif, lgap):
    ''' (str, str, int, int, int, int) -> int

    RECEBE duas strings `s` e `t` de mesmo tamanho com zero ou mais gaps 
    representando fitas de DNA; e quatro inteiros `ga`, `la`, `ldif`, `lgap`.
 
    RETORNA a pontuação do alinhamento entre `s` e `t` calculada da seguinte 
    forma:

       * dois gaps alinhados contam `ga` pontos,
       * duas letras iguais alinhadas contam `la` pontos, 
       * duas letras diferentes alinhadas contam `-ldif` pontos (subtrai ldif pontos) e 
       * uma letra alinhada com um gap contam `-lgap` pontos (subtrai lgap pontos).

    Exemplos:

    In  [1]: pontuacao('T_', 'CT', 1, 5, 6, 3)
    Out [1]: -9

    In  [2]: pontuacao('T_CGTAC', 'T_CG_TC', 1, 5, 6, 3)
    Out [2]: 12
    
    In  [3]: pontuacao('T_CGTAC', 'A_CG_T_', 2, 3, 5, 4)
    Out [3]: -10
    
    In  [4]: pontuacao('T_CGTA',  'A_CGT_', -1, 5, 3, 2)
    Out [4]: 9
    '''
    # modifique o código abaixo para conter a sua solução.
    
    pontuacao = 0
    
    for i in range(len(s)):
        if s[i] in DNA:
            if s[i] == t[i]:
                pontuacao += la
            elif t[i] == GAP:
                pontuacao -= lgap
            else:
                pontuacao -= ldif
        elif s[i] == GAP:
            if t[i] == GAP:
                pontuacao += ga
            elif t[i] in DNA:
                pontuacao -= lgap
            
           
    
    return pontuacao
    

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
