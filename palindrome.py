#!/usr/bin/python
'''
Algoritmo que descobre se uma palavra é 
palindrome ou não.

'''
print('\033[1;34m*'*45)
print('''\033[1;32mDIZ SE QUE UMA PALAVRA É PALINDROME:
\033[0;32mSe invertermos a posição das letras, da esquerda para 
a direita o resultado mantem.
\033[1;32mPor exemplo: \033[1;36masa --> asa
''')
print('\033[1;34m*'*45)

palavra = input('\033[1;32mDigite uma palavra: \033[1;36m')

if palavra==palavra[::-1]:
   print('\033[1;34m*'*45)
   print('\033[1;32mPalavra digitada: \033[1;36m' ,palavra)
   print('\033[1;32mA palavra: \033[1;36m{} \033[1;32mé palindrome.'.format(palavra))
   print('\033[1;34m*'*45)
else:
   print('\033[1;34m*'*45)
   print('\033[1;32mPalavra digitada: \033[1;36m' ,palavra)
   print('\033[1;32mA palavra: \033[1;36m{} \033[1;31m não é palindrome.'.format(palavra))
   print('\033[1;34m*'*45)

