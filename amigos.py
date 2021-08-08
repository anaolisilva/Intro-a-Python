
# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
#------------------------------------------------------------------

'''
------------------------------------------------------------------------------

ENUNCIADO:
    "Implementar funções que verifiquem se sorteios de listas são circulares,
    utilizando o exemplo de um amigo secreto."
    
------------------------------------------------------------------------------

    Nome: Ana Oliveira Silva
    Data: 21/06/21

'''
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
# random.shuffle(lst) embaralha os elementos da lista lst.
import random 

#####################################################################
def circular(amigo_de):
    ''' (list) -> bool 
    RECEBE uma lista amigo_de (de "amigos secretos")
    RETORNA True se a lista for circular e False em caso contrário.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    i = 0
    cont = 0
    listaC = True
    
    while (cont < len(amigo_de) and listaC):
        i = amigo_de[i]
        cont += 1
        
        if amigo_de[i] == 0 and cont != (len(amigo_de) - 1):
            listaC = False
        
    
    return listaC

###################################################################
def experimento(N, T, debug=False):
    ''' (int, int) -> float
    RECEBE um inteiro N > 0, um inteiro T > 0 e um booleano debug.
    RETORNA a probabilidade de uma lista de "amigo secretos" com
        N participantes ser circular.

    Esta probabilidade deve ser calculada a partir de T sorteios 
    de listas de tamanho N, e calculando a frequência das listas 
    circulares.

    Se a opção debug é True a função deve imprimir todas as 
    listas sortedas que forem circulares, como mostrado no
    enunciado.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    i = 0
    s = 0
    
    while (i < T):
        lista = sorteie_amigos(N)
        if (circular(lista)):
            s += 1
            if (debug):
                print (f"{s} : {lista}")
        i += 1
    
    p = s / T
    
    
    return p

#####################################################################
def main():
    '''
    Essa função auxilia no teste das funções pedidas para o EP08.
    Se desejar, escreva mais testes.
    
    Atenção: a tabulação das linhas foi removida e deve ser consertada 
    antes que a função possa ser utilizada.
    '''
    print("INÍCIO DOS TESTES")
    
    # testes da função circular()
    print("Função circular()")
    amigos1 = [1,2,3,4,0]
    amigos2 = [1,2,0,4,3]
    print(f"circular({amigos1}) = {circular(amigos1)}")
    print(f"circular({amigos2}) = {circular(amigos2)}")
    
    # testes da função experimento()
    print("Função experimento()")
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)
    MINN  = int(input("Qual o número mínimo de pessoas: "))
    MAXN  = int(input("Qual o número máximo de pessoas: "))
    passo = int(input("Qual o passo: "))
    T     = int(input("Qual o número de tentativas em cada experimento: "))
    SHOW  = input("Você quer ver as listas que são circulares [s/n]: ")
    
    debug = False
    if SHOW == 'S' or SHOW == 's':
        debug = True
    
    N = MINN
    
    while N <= MAXN:
        pN = experimento(N, T, debug)
        print(f"p({N}) = {pN}")
        N = N + passo
    
    print("TESTES ENCERRADOS")    

###################################################################
def sorteie_amigos( N ):
    ''' (IMPLEMENTADA PELOS PROFESSORES)
    (int) -> list
    RECEBE um inteiro N > 0.
    RETORNA uma lista de tamanho N, contendo os números de 0 a N em 
        ordem aleatória.
    
    ATENÇÃO: a tabulação das linhas foi removida e a ordem de algumas 
    linhas alterada. Ela deve ser consertada antes possa ser utilizada.
    '''
    i = 0
    
    amigos = []
    
    while i < N:
        amigos += [i]
        i += 1
    
    random.shuffle(amigos)
    
    return amigos  



#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para executar a main() dentro do Spyder
# e não atrapalhar o avaliador
if __name__ == '__main__':
    main()
