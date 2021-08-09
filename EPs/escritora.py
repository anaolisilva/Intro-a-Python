# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''
------------------------------------------------------------------------------

ENUNCIADO:
    "Construir um dicionário de sucessores e gerar um processo aleatório que
    'imite' a escrita de Machado de Assis."

------------------------------------------------------------------------------

    Nome: Ana Oliveira Silva
    Data: 23/07/21

'''
#------------------------------------------------------------------
# MODULOS A SEREM UTILIZADOS NO PROGRAMA
import random # para random.choice(lista) na função gere_frase()

#------------------------------------------------------------------
# CONSTANTES

# ponto final, ponto de interrogação, ponto de exclamação
# não consideraremos reticências "..."
PONTUACAO_FINAL = ".?!"

# vírgula, ponto e vírgula, dois pontos, fecha parênteses
# não devem ser precedidos de espaço na frase gerada
PONTUACAO_SEM_ESPACO = ',;:)' + PONTUACAO_FINAL

# travesão, aspas, abre chaves
# devem ser precedidos de espaço na frase gerada
PONTUACAO_COM_ESPACO = '—"('

# todas juntas (reticências foram desconsideradas)
PONTUACAO = PONTUACAO_SEM_ESPACO + PONTUACAO_COM_ESPACO

# usado na função insira espacos
ESPACO = ' '

# semente para o gerador aleatório com o objetivo de reprodutibilidade
SEED = 1234

#------------------------------------------------------------------
#
def main():
    '''(None) -> None

    Para testar as funções juntas. Esta função não será avaliada, entretanto
    ela __não__ deve gerar erro de execução ou sintático. 
    Modifique-a se desejar.
    '''
    # Para efeitos de reprodutibilidade
    random.seed(SEED)

    print('ESCREVENDO "como" MACHADO DE ASSIS!\n')

    # 1 leia nome do arquivo 
    nome = input("Digite o nome do arquivo com o texto: ")

    # 2 leia o corpus
    try:
        with open(nome, "r", encoding="utf-8") as arq:
            texto = arq.read()
    except:
        print(f"main(): Erro na leitura do arquivo '{nome}'")
        return None
    
    # 3 insira espaços antes de pontuações
    texto = insira_espacos(texto)

    # 4 obtenha lista com itens léxicos
    lst_itens = texto.split()
    
    # 5 construa dicionario de sucessores
    dicio = dicio_sucessores(lst_itens)

    # 6 quantidade de frases que devem ser geradas
    n = int(input("Digite o numero de frases que devem ser geradas: "))

    # 7 gere as frase
    for i in range(n):
        # gere i-ésima frase
        print("---")

        # 7.1 pegue palavra inicial da frase a ser gerada
        palavra_inicial = input(f"Digite a palavra inicial da frase {i+1}: ")

        # 7.2 gere uma frase começando com palavra_inicial 
        frase = gere_frase(palavra_inicial, dicio)
        print("Frase gerada:", frase)

    print("\nFIM")

#------------------------------------------------------------------
def insira_espacos(txt):
    '''(str) -> str

    RECEBE uma string `txt`.
    RETORNA a string resultante da inserção de um ESPACO antes e depois de 
    __cada sinal__ em PONTUACAO que estiver em texto.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    
    txtres = ""
    
    i = 0
    
    
    while i < len(txt):
        txtres = txt
        if (txt[i] in PONTUACAO):                
            txtres = txt[:i] + ESPACO + txt[i] + ESPACO + txt[i+1:]
            i+=2
                      
        txt = txtres
        i += 1

    
    if txt[len(txt)-1] in PONTUACAO:
        txt = txt + ESPACO
    
    return txt
    
#------------------------------------------------------------------
def dicio_sucessores(lst):
    '''(list) -> dict

    RECEBE uma lista `lst`.
    RETORNA um dicionário em que 

        - as __chaves__ são os itens que ocorrem em lst e 
        - o  __valor__ associado a cada chave é a lista dos 
          itens que ocorrem imediatamente após a chave na lista lst.

    Por convenção a lista correspondente ao valor do último item 
    na lst (=lst[-1]) contém o primeiro item da lista (=lst[0]).

    Se a `lst` é a lista vazia a função deve retornar o dicionário vazio.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    
    
    dic = {}
    
    for i in range(0, len(lst), 1):
        
        if lst[i] in dic:
            if (i != len(lst)-1):
                dic[lst[i]] += [lst[i+1]]
            else:
                dic[lst[i]] += [lst[0]]
        else:
            if (i != len(lst)-1):
                dic[lst[i]] = [lst[i+1]]
            else:
                dic[lst[i]] = [lst[0]]
                    
    
    return dic

#------------------------------------------------------------------
def gere_frase(p_inicial, dicio):
    '''(str, dict) -> str

    RECEBE uma palavra `p_inicial` e um dicionário `dicio`.

    O dicionário foi criado a partir de um texto com uma ou 
    mais frase; como nos textos de Machado de Assis.

    Cada chave do dicionário é um item (str). O valor no dicionário 
    correspondente a uma chave é uma lista (list) de itens (str). 

    RETORNA uma string representando uma frase.

    A frase retornada deve começar com a string p_inicial e ser gerada 
    segundo o __processo aleatório__ descrito no enunciado.
    
    Os itens na frase devem ser precedidos de um ESPACO, exceto:

        - a palavra inicial e
        - e os sinais de pontuação na string PONTUACAO_SEM_ESPACO.

    Se p_inicial não está no dicionário a função deve retornar a string vazia.
    
    Coloca a chave no final da frase que está sendo gerada. 
    Em seguida, examina no dicionário o valor correspondente a essa chave, 
    obtendo assim a lista dos itens sucessores da chave. 
    Depois, seleciona aleatoriamente um item dessa lista para ser a nova 
    chave. O processo é repetido com a nova chave no papel da antiga.
    A função deve repetir o processo acima até chegar a um item que seja uma 
    pontuação final, ou seja, um caractere em ".!?".
    '''
    # modifique o código abaixo para conter a sua solução.
    
    if p_inicial not in dicio:
        return ""
    
    p = p_inicial
    frase = p_inicial
    
    while frase[len(frase)-1] not in PONTUACAO_FINAL:
        p = random.choice(dicio[p])
        
        if p in PONTUACAO_SEM_ESPACO:
            frase += p
        else:
            frase += ESPACO + p


    return frase

#######################################################
###                 FIM                             ###
#######################################################
#
# Não modifique as linhas abaixo
#
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático
# COMENTE as linhas a seguir durante os testes das suas
# funções no Python Shell

if __name__ == '__main__':
    main()
