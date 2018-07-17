#!/usr/bin/python
'''
Calculadora de média do Instituto 
Indústrial e Comercial-Beira.

'''
def color():
    green='\033[1;32m'
    amarela='\033[1;33m'
    rocho='\033[1;35m'
    azul='\033[1;34m'
    aqua='\033[1;36m'
    branco='\033[1;37m'
    red='\033[1;31m'

def tres_acs():
    # Inputs
    print('\033[1;33m*'*45)
    print('\033[1;33m[#] ==>> \033[1;36mCALCULADORA DE MÉDIA DO I.I.C.B')
    print('\033[1;33m*'*45)
    acs1=float(input('\033[1;32mACS1: \033[1;36m'))
    acs2=float(input('\033[1;32mACS2: \033[1;36m'))
    acs3=float(input('\033[1;32mACS3: \033[1;36m'))
    acp1=float(input('\033[1;32mACP1: \033[1;36m'))
    acp2=float(input('\033[1;32mACP2: \033[1;36m'))
    print('\033[1;33m*'*45)
    # Formúlas
    med_acs=(acs1+acs2+acs3)/3
    med_acp=acp1+acp2
    med_final=(med_acs+med_acp)/3
    
    # Condições
    if med_final<=9.9:
       print('\033[1;32mReprovado com média: \033[1;31m{:.2f} valores.'.format(med_final))
    else:
       print('\033[1;32mAprovado com média: \033[1;34m{:.2f} valores.'.format(med_final))

def quatro_acs():
    # Inputs
    print('\033[1;33m*'*45)
    print('\033[1;33m[#] ==>> \033[1;36mCALCULADORA DE MÉDIA DO I.I.C.B')
    print('\033[1;33m*'*45)
    acs1=float(input('\033[1;32mACS1: \033[1;36m'))
    acs2=float(input('\033[1;32mACS2: \033[1;36m'))
    acs3=float(input('\033[1;32mACS3: \033[1;36m'))
    acs4=float(input('\033[1;32mACS4: \033[1;36m'))
    acp1=float(input('\033[1;32mACP1: \033[1;36m'))
    acp2=float(input('\033[1;32mACP2: \033[1;36m'))
    print('\033[1;33m*'*45)
    # Formúlas
    med_acs=(acs1+acs2+acs3+acs4)/4
    med_acp=acp1+acp2
    med_final=(med_acs+med_acp)/3
   
    # Condições
    if med_final<=9.9:
       print('\033[1;32mReprovado com média: \033[1;31m{:.2f} valores.'.format(med_final))
    else:
       print('\033[1;32mAprovado com média: \033[1;34m{:.2f} valores.'.format(med_final))

def inic():
    # Inicialização do algoritmo
   try:
      n=int(input("\033[1;32mDigite o número de acs's feitas: \033[1;36m"))
      if n==3:
         tres_acs()
      elif n==4:
          quatro_acs()
      else:
         print('\033[1;31mO número de acs digitado é invalido para essa instituicao.[!]')

   except Exception as err:
        print('\033[1;31mErro_try again.')
        inic()
inic()




