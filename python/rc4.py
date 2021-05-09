#!/usr/bin/python3

# Criptografia com RC4
# Para detalhes do algoritmo, verificar:
# https://en.wikipedia.org/wiki/RC4

# A chave deve ter entre 5 e 16 caracteres (entre 40 e 128 bits)

# Tamanho da lista de substituição
# O padrão é de 256 bytes
tamanho = 256

# Inicia o array de estados já com o tamanho final e conteúdo "None"
# Necessário para que todos os índices estejam disponíveis
lista_ksa = [None] * tamanho

# RC4 Key Scheduling Algorithm (KSA)
def ksa(chave_ksa_texto):
    chave_ksa = texto_lista(chave_ksa_texto)
    # Inicia a lista com valores ordenados de 1 ao tamanho
    for n in range(tamanho):
        lista_ksa[n] = n
    j = 0
    for i in range(tamanho):
        j = (j + lista_ksa[i] + int(chave_ksa[i % len(chave_ksa)])) % tamanho
        # Troca os valores da posições i e j
        lista_ksa[i], lista_ksa[j] = lista_ksa[j], lista_ksa[i]

# RC4 Pseudo-Random Generation Algorithm (PRGA) 
def prga(quant):
    pseudo = []
    lista_prga = lista_ksa[:]
    p = q = 0
    for a in range(quant): 
        p = (p + 1) % tamanho
        q = (q + lista_prga[p]) % tamanho
        lista_prga[p], lista_prga[q] = lista_prga[q], lista_prga[p]
        pseudo.append(lista_prga[(lista_prga[p] + lista_prga[q]) % tamanho])
    return pseudo
 
# Criptografa texto
def cripto(texto):
    lista_prga = prga(len(texto))
    saida = []
    a = 0
    for t in texto:
        # Mostra dados
        # Os dados criptografados com o operador XOR
        # print ("texto ascii prga[10] prga[16] xor[10] xor[16]")
        # print (t, ord (t), lista_prga[a], "{:02x}".format(lista_prga[a]), ord (t) ^ lista_prga[a], "{:02x}".format(ord (t) ^ lista_prga[a]))
        saida.append(ord (t) ^ lista_prga[a])
        a+=1
    return saida

# Descriptografa texto
def decripto(lista_bytes):
    lista_prga = prga(len(lista_bytes))
    saida = ""
    a = 0
    for l in lista_bytes:
        # Mostra dados usando o operador XOR
        # print (l, chr(l ^ lista_prga[a]))
        saida += chr(l ^ lista_prga[a])
        a+=1
    return saida
    
# Converte uma string em lista de bytes
# Usado para operações usando o código ASCII dos caracteres da chave
def texto_lista(texto):
    lista = []
    for t in texto:
        lista.append(ord(t))
    return lista


