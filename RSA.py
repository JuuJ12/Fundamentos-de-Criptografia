import random as rd
import math as mat
def num_p(n):
    lista_primos = []
    for i in range(2, n + 1):
        primo = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                primo = False
                break
        if primo:
            lista_primos.append(i)
    return lista_primos

a,b= 17,23

def calcular_N(a,b):
    return a * b

N= calcular_N(a,b)


def calcular_funcao_totient_N(a,b):
    return (a-1) * (b-1)
totient_n= calcular_funcao_totient_N(a,b)


def achar_div_comun(a,tn):
    divisores_a = [i for i in range(1, a + 1) if a % i == 0]

    # Encontrar divisores de tn
    divisores_tn = [i for i in range(1, tn + 1) if tn % i == 0]
    divisores_comuns= set(divisores_a) & set(divisores_tn)
    if len(divisores_comuns) == 1:
        return a
    else:
        return achar_div_comun(a+1,tn)
valor_E=(achar_div_comun(3,totient_n))


#Algoritmo Euclidiano
def MDC(a,b):
   if b == 0:
       return a
   else:
       return MDC(b, a % b)

#Algoritmo Euclidiano Estendido
def MDCE(a,b):
    if b == 0:
        return [1,0,a]
    else:
        x,y,d = MDCE(b,a%b)
        return [y,x-(a/b)*y,d]

#Inverso Modular
def invmod(a,n):
    #o inverso modular só existe de mdc(a,n) -1
    if MDC(a,n) !=1:
        return 'invmod não existe'
    else:
        x,y,d = MDCE(a,n)
        return mat.ceil(x) % n

valor_D= invmod(3,totient_n)


print(f'chaves Públicas: {N},{valor_E}')
print(f'Chaves Privadas: {a},{b},{valor_D}')

def converter_ASCII(mensagem):
    lista=[]
    for i in mensagem:
        lista.append(ord(i))
    return lista
mensagem= 'BSI CRIPTOGRAFIA'

mensagem_em_ASCII = converter_ASCII(mensagem)
print(f'Mensagem {mensagem} Em ASCII: {mensagem_em_ASCII}')
def codificar_mensagem_RSA(ASCII):
    lista=[]
    for i in ASCII:
        result =(i ** valor_E) % N
        lista.append(result)
    return lista
print(f'Mensagem Convertida em Valores ASCII Codificada Em RSA: {codificar_mensagem_RSA(mensagem_em_ASCII)}')
mensagem_codificada = codificar_mensagem_RSA(mensagem_em_ASCII)

def decodificar_mensagem(mensage_codificada):
    lista = []

    for i in mensage_codificada:
        result = (i ** valor_D) % N
        lista.append(result)
    return  lista
print(f'Mensagem Decodificada: {decodificar_mensagem(mensagem_codificada)}')
