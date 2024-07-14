# Autokey Cipher
def alfa(li,lf):
    l=[]
    for c in range(ord(li),ord(lf) +1):
        l+= chr(c).lower()
    return l

def gerar_matriz_alfabeto():
    alfabeto = alfa('a','z')
    matriz = []

    for letra in alfabeto:
        linha = [letra]
        for i in range(ord(letra), ord('z') + 1):
            linha.append(chr(i))
        for i in range(ord('a'), ord(letra)):
            linha.append(chr(i))
        matriz.append(linha)

    return matriz

matriz_alfabeto = gerar_matriz_alfabeto()
def auto_key_cifrar(mensagem,chave,palavra):
    posicao_l = 0
    coluna = 0
    while len(chave) < len(mensagem):
        for i in chave:
            chave+=i
    for i in range(len(mensagem)):
            letra1 = mensagem[i]
            letra2 = chave[i]
            for j in range(len(matriz_alfabeto)):
                linha= matriz_alfabeto[j]
                if letra1 == linha[0]:
                    posicao_l= j
            for c in range(len(matriz_alfabeto[posicao_l])):

                    letra_atual=matriz_alfabeto[0][c]
                    if letra_atual == letra2:
                        coluna= c
            palavra += matriz_alfabeto[posicao_l][coluna]

    return palavra



def auto_key_descifrar(mensagem_cripto,chave,palavra_descripto):
    posicao_l = 0
    coluna = 0
    while len(chave) < len(mensagem):
        for i in chave:
            chave+=i
    for i in range(len(mensagem_cripto)):
            letra1 = chave [i]
            letra2 = mensagem_cripto[i]
            for j in range(len(matriz_alfabeto)):
                linha= matriz_alfabeto[j]
                if letra1 == linha[0]:
                    posicao_l= j
            for c in range(len(matriz_alfabeto[posicao_l])):

                    letra_atual=matriz_alfabeto[posicao_l][c]
                    if letra_atual == letra2:
                        coluna= c
            palavra_descripto += matriz_alfabeto[0][coluna]

    return palavra_descripto

mensagem='FORTIFICATIONDEFENDTHEEASTWA'.lower()
chave= 'DEFENDTHEEASTWALLOFTHECASTLE'.lower()
palavra=""
cripto= auto_key_cifrar(mensagem,chave,palavra)
palavra_descripto=''
descripto= auto_key_descifrar(cripto,chave,palavra_descripto)
print(f"Frase normal: {mensagem}. Frase cifrada: {cripto}")
print(f"Frase Cifrada: {cripto}. Frase Descifrada: {descripto}")