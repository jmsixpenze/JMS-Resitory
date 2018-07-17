#!/usr/bin/python

import time
import sys
horas=time.asctime()

def codificacao():
    try:
       msg=str(input(' |[#####]\033[1;36m Digite a Mensagem: '))
       s=''
       for c in msg: s+=chr(ord(c)+30000)
       print('\033[1;36m-'*45)
       print('\033[1;36m |[#####]Mensagem Codificada: \033[1;32m',s)
       print('\033[1;36m-'*45)
    except Exception as err:
        print(' [!] Aconteceu um erro:',err)
        print(' [+] Tente de novo.\n') 
        codificacao()

def descodificacao():
    try:
       msg=str(input(' |[#####]\033[1;36m Digite a Mensagem: '))
       s=''
       for c in msg: s+=chr(ord(c)-30000)
       print('\033[1;36m-'*45)
       print('\033[1;36m |[#####]Mensagem Descodificada: \033[1;32m',s)
       print('\033[1;36m-'*45)
    except Exception as err:
        print(' [!] Aconteceu um erro:',err)
        print(' [+] Tente de novo.\n') 
        descodificacao()

def main():
       print('''\033[1;36m
 -----------------------------------------
 |                                       |
      |\033[1;32mCODIFICAÇÃO & DESCODIFICAÇÃO\033[1;36m|
 |                                       |
 ----------------------------------------- 
 |[1] Codificar Mensagem                 |
 |[2] Descodificar Mensagem              |
 -----------------------------------------''') 
       try:
          op=int(input(' |[Opção] Digite a Opção: '))
          if op==1:
             codificacao()
          elif op==2:
             descodificacao()
          elif op==3:
                   sys.exit()
       except:
          print('\033[1;31m [!] Aconteceu um erro:')
          print('\033[1;36m [+] Tente de novo.')
          print('\033[1;36m-'*45)
          main()
          
main()  
                                    