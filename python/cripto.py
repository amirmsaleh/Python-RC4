#!/usr/bin/python3

import random
import rc4

# A chave deve ter entre 5 e 16 caracteres (entre 40 e 128 bits)
# chave = "Secret"

# Lista de chaves
lista_chaves = ['78938270','18390190','11727065','91967061','29143787','64293700','20775309','19286195','53853351','95572715','28841605','28555858','69564296','31970930','64027403','64647753','80633129','74374291','50416789','75803436']
# Seleciona chave aleatoriamente entre as presentes lista
chave = lista_chaves[random.randint(0,len(lista_chaves)-1)]

# Inicia a lista KSA utilizando a chave
rc4.ksa(chave)

texto_original = "Texto 1 a ser criptografado."

# Obtém o texto criptografado
tc = rc4.cripto(texto_original)
print ("Texto original:",texto_original,"\nChave:",chave,"\nCriptografado decimal:", *tc)
tc_hexa = []
for a in tc:
    tc_hexa.append("{:02x}".format(a))
print ("Criptografado hexadecimal:", *tc_hexa)

#Obtém o texto descriptografado
print ("Descriptografado:",rc4.decripto (tc))
               
