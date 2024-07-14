import random as rd
def alfa(li,lf): #alfabeto
    l=[]
    for c in range(ord(li),ord(lf) +1):
        l+= chr(c).upper()
        #l+= chr(c).lower()
    return l


def cifrar(mensagem,chave): #cifrando a mensagem
    alfabeto = alfa('A','Z')
    cifra = ''
    for letra in mensagem:
            # Transformar em número
            posicao = alfabeto.index(letra.upper())
            d = (posicao + chave)%26
            cifra +=alfabeto[d]
    return cifra


def deslocamento(palavra): #achar a chave
    cifra=palavra
    gemeo=''
    for j in range(1,26):
        gemeo= cifrar(m,j)

        if gemeo == cifra:
            return j



def descifrar(mensagem,chave): # decifrando utlizando a chave que achamos
    alfabeto = alfa('a','z')
    cifra = ''
    for letra in mensagem:
            posicao = alfabeto.index(letra.upper())
            d = (posicao - chave)%26
            cifra +=alfabeto[d]
    return cifra

m= 'Criptografia'
k = rd.randint(1,26)
cifrada= cifrar(m,k)
chave=deslocamento(cifrada)
descifrada = descifrar(cifrada,chave)
print(f'palavra {m} Cifrada : {cifrada}')
print(f'Chave encontrada {chave}')
print(f'Descifranda a palavra {cifrada}, utilizando a chave {chave} temos a palavra {descifrada}')