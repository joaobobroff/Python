import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print('Bem-vindo ao detector automático de COH-PIAH.')
    print('Informe a assinatura típica de um aluno infectado:\n')

    wal = float(input('Entre o tamanho médio de palavra: '))
    ttr = float(input('Entre a relação Type-Token: '))
    hlr = float(input('Entre a Razão Hapax Legomana: '))
    sal = float(input('Entre o tamanho médio de sentença: '))
    sac = float(input('Entre a complexidade média da sentença: '))
    pal = float(input('Entre o tamanho medio de frase: '))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input('\nDigite o texto ' + str(i) +' (aperte enter para sair): ')
    while texto:
        textos.append(texto)
        i += 1
        texto = input('\nDigite o texto ' + str(i) +' (aperte enter para sair): ')

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(ass_a, ass_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range (0, 6):  # i vai da posição 0 a posição 5, resultando em 6 traços linguísticos
        soma = soma + (abs(ass_a[i] - ass_b[i]))  # abs é para devolver o valor absoluto de um cálculo

    return soma/6


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    soma_car_sentenca = 0
    soma_car_frase = 0
    soma_pal = 0

    for sentenca in sentencas:      
        soma_car_sentenca += len(sentenca)        
        l_frases = separa_frases(sentenca)
        for f in l_frases:
            frases.append(f)

    for frase in frases:
        soma_car_frase += len(frase)
        l_pal = separa_palavras(frase)
        for palavra in l_pal:
            palavras.append(palavra)    
    
    for palavra in palavras:
        soma_pal += len(palavra)
    
    meia_palavras = soma_pal/len(palavras)
    type_token = n_palavras_diferentes(palavras)/len(palavras)
    hapax = n_palavras_unicas(palavras)/len(palavras)
    meio_sentencas = soma_car_sentenca / len(sentencas)
    comp_sentenca = len(frases) / len(sentencas)
    tam_meio_frase = soma_car_frase / len(frases)

    return [meia_palavras, type_token, hapax, meio_sentencas, comp_sentenca, tam_meio_frase]



def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos (que estão em le_textos (recebe o return textos)) e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    infec = []

    for texto in textos:
        ass_texto = calcula_assinatura(texto)  # Calcula a assinatura do prieiro texto
        infec.append(compara_assinatura(ass_texto, ass_cp))  # Adiciona os resultados de compara_assinatura a esta lista criada

    menor_grau = infec[0]  # É definido como o menor grau de similaridade (quanto menor grau, maior similaridade)
    infectado = 1

    for i in range(1, len(infec)):  # Todos os textos são avaliados na similaridade
        if menor_grau < infec[i]:  # Se o texto analisado tem menor grau que o armazenado, o valor é substituído
            infectado = i  # O texto infectado é alterado

    return infectado


def start():  # cp = COH-PIAH
    ass_cp = le_assinatura()  # Lê a assinatura do aluno infectado com COH-PIAH e retorna a assinatura, que é uma lista contendo os 6 traços linguísticos
    textos = le_textos()  # Lê os textos e retorna uma lista de textos que serão comparados com a assinatura do aluno infectado
    infectado = avalia_textos(textos, ass_cp)
    print('\nO autor do texto', infectado,'está infectado com COH-PIAH')  # Todos os textos serão comparados com a assinatura do aluno infectado, para ver qual é mais parecido

start()
