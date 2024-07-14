def alfa(li,lf):
    l=[]
    for c in range(ord(li),ord(lf) +1):
        l+= chr(c).upper()
        l+= chr(c).lower()
    return l
print(alfa('a','z'))

def clean_text(text):
    texto = text
    novo_texto=''
    alfabeto= alfa('a','z')
    for i in texto:
        if i in alfabeto:
            novo_texto += i.lower()
    return novo_texto
texto= 'Marcelo Gama - Rua 1233, %$#dfe'
print(clean_text(texto))