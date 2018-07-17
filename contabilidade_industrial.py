#!/usr/bin/python
'''
Contabilidade de seguros.

'''
import sys

# Calculo do premio com outras taxas
def premio_com_outras_taxas():

   print('\033[1;35m*'*45)
   print('\033[1;32m==> Calculo do premio total com outras taxas.')
   print('\033[1;35m*'*45)

   capital=float(input('\033[1;35mValor do capital:\033[1;36m '))
   tx_risco=float(input('\033[1;35mTaxa de risco:\033[1;36m '))
   tx_encargo=float(input('\033[1;35mPercentagem de encargos:\033[1;36m '))
   ca=float(input('\033[1;35mCusto de apolice:\033[1;36m '))
   tx_sa=float(input('\033[1;35mPercentagem de selo de apolice:\033[1;36m '))
   outra_tx=float(input('\033[1;35mPercentagem de otras taxas:\033[1;36m '))

   # Formulas
   permilagem=tx_risco/1000
   ps=capital*permilagem
   encargos=(tx_encargo/100)*ps
   pc=ps+encargos
   pb=pc+ca
   sa=(tx_sa/100)*pb
   inem=(outra_tx/100)*pb
   pt=pb+sa+inem

   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCALCULO DO PREMIO TOTAL.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mPrémio simples({:.2f}x{:.2f}).....{:.2f}'.format(capital,tx_risco,ps))
   print('\033[1;32m[+]\033[1;36mEncargos({:.2f}x{:.2f}).............{:.2f}'.format(ps,tx_encargo,encargos))
   print('\033[1;32m[=]\033[1;36mPrémio comercial....................{:.2f}'.format(pc))
   print('\033[1;32m[+]\033[1;36mCusto de ápolice....................{:.2f}'.format(ca))
   print('\033[1;32m[=]\033[1;36mPrémio bruto........................{:.2f}'.format(pb))
   print('\033[1;32m[+]\033[1;36mSelo de apolice({:.2f}x{:.2f})..........{:.2f}'.format(pb,tx_sa,sa))
   print('\033[1;32m[+]\033[1;36mOutras taxas(INEM)&({:.2f}x{:.2f})......{:.2f}'.format(pb,outra_tx,inem))
   print('\033[1;32m[=]\033[1;36mPrémio total..........................{:.2f}'.format(pt))
   print('\033[1;35m*'*45)
 

# Calculo do premio sem otras taxas
def premio_sem_outras_taxas():

   print('\033[1;35m*'*45)
   print('\033[1;32m==> Calculo do premio total com sem outras taxas.')
   print('\033[1;35m*'*45)

   capital=float(input('\033[1;35mValor do capital:\033[1;36m '))
   tx_risco=float(input('\033[1;35mTaxa de risco:\033[1;36m '))
   tx_encargo=float(input('\033[1;35mPercentagem de encargos:\033[1;36m '))
   ca=float(input('\033[1;35mCusto de apolice:\033[1;36m '))
   tx_sa=float(input('\033[1;35mPercentagem de selo de apolice:\033[1;36m '))
   
   # Formulas
   permilagem=tx_risco/1000
   ps=capital*permilagem
   encargos=(tx_encargo/100)*ps
   pc=ps+encargos
   pb=pc+ca
   sa=(tx_sa/100)*pb
   pt=pb+sa

   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCALCULO DO PREMIO TOTAL.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mPrémio simples({:.2f}x{:.2f}).....{:.2f}'.format(capital,tx_risco,ps))
   print('\033[1;32m[+]\033[1;36mEncargos({:.2f}x{:.2f}).............{:.2f}'.format(ps,tx_encargo,encargos))
   print('\033[1;32m[=]\033[1;36mPrémio comercial....................{:.2f}'.format(pc))
   print('\033[1;32m[+]\033[1;36mCusto de ápolice....................{:.2f}'.format(ca))
   print('\033[1;32m[=]\033[1;36mPrémio bruto........................{:.2f}'.format(pb))
   print('\033[1;32m[+]\033[1;36mSelo de apolice({:.2f}x{:.2f})..........{:.2f}'.format(pb,tx_sa,sa))
   print('\033[1;32m[=]\033[1;36mPrémio total..........................{:.2f}'.format(pt))
   print('\033[1;35m*'*45)
 

# Mediação de seguros
def mediacao_de_seguro():
   
   # Calculo do premio total, remuneracao de mediação, imposto sobre remunerações e valor a prestar conta a seguradora
   print('\033[1;35m*'*45)
   print('\033[1;32m[&]CALCULO DO PREMIO TOTAL\n[&]REMUNERAÇÃO DE MEDIAÇÃO\n[&]IMPOSTO SOBRE REMUNERAÇÕES\n[&]VALOR A PRESTAR CONTA A SEGURADORA')
   print('\033[1;35m*'*45)
   
   capital=float(input('\033[1;35mValor do capital:\033[1;36m '))
   tx_risco=float(input('\033[1;35mTaxa de risco:\033[1;36m '))
   tx_encargo=float(input('\033[1;35mPercentagem de encargos:\033[1;36m '))
   ca=float(input('\033[1;35mCusto de apolice:\033[1;36m '))
   tx_sa=float(input('\033[1;35mPercentagem de selo de apolice:\033[1;36m '))
   outra_tx=float(input('\033[1;35mPercentagem de otras taxas:\033[1;36m '))

   # Formulas
   permilagem=tx_risco/1000
   ps=capital*permilagem
   encargos=(tx_encargo/100)*ps
   pc=ps+encargos
   pb=pc+ca
   sa=(tx_sa/100)*pb
   inem=(outra_tx/100)*pb
   pt=pb+sa+inem

   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCALCULO DO PREMIO TOTAL.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mPrémio simples({:.2f}x{:.2f}).....{:.2f}'.format(capital,tx_risco,ps))
   print('\033[1;32m[+]\033[1;36mEncargos({:.2f}x{:.2f}).............{:.2f}'.format(ps,tx_encargo,encargos))
   print('\033[1;32m[=]\033[1;36mPrémio comercial....................{:.2f}'.format(pc))
   print('\033[1;32m[+]\033[1;36mCusto de ápolice....................{:.2f}'.format(ca))
   print('\033[1;32m[=]\033[1;36mPrémio bruto........................{:.2f}'.format(pb))
   print('\033[1;32m[+]\033[1;36mSelo de apolice({:.2f}x{:.2f})..........{:.2f}'.format(pb,tx_sa,sa))
   print('\033[1;32m[+]\033[1;36mOutras taxas(INEM)&({:.2f}x{:.2f})......{:.2f}'.format(pb,outra_tx,inem))
   print('\033[1;32m[=]\033[1;36mPrémio total..........................{:.2f}'.format(pt))
   print('\033[1;35m*'*45)
 
   # Calculo de remuneração de mediação
   print('\033[1;35m*'*45)
   print('\033[1;32mCALCULO DE REMUNERAÇÃO DE MEDIAÇÃO.')
   print('\033[1;35m*'*45)
   tx_cc=float(input('\033[1;35mTaxa de comissão de cobrança:\033[1;36m '))
   tx_c=float(input('\033[1;35mTaxa de cobrança:\033[1;36m '))

   # Formulas
   cm=ps*(tx_cc/100)
   cc=ps*(tx_c/100)
   rb=cm+cc
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mREMUNERAÇÃO DE MEDIAÇÃO.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mComissões de mediaçã({:.2f}x{:.2f}).....{:.2f}'.format(ps,tx_cc,cm))
   print('\033[1;32m[+]\033[1;36mComissões de cobrança({:.2f}x{:.2f})....{:.2f}'.format(ps,tx_c,cc))
   print('\033[1;32m[=]\033[1;36mRemuneração bruta ou iliquida..........{:.2f}'.format(rb))
 
  
   # Imposto sobre remunerações
   print('\033[1;35m*'*45)
   print('\033[1;32mIMPOSTO SOBRE REMUNERAÇÕES.')
   print('\033[1;35m*'*45)
   tx_irps=float(input('\033[1;35mTaxa de IRPS:\033[1;36m '))
   tx_is=float(input('\033[1;35mTaxa de Imposto de selo:\033[1;36m '))

   # Formulas
   irps=rb*(tx_irps/100)
   a=rb*tx_is
   b=100+tx_is
   _is=a/b
   ti=irps+_is
   rli=rb-ti
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mIMPOSTO SOBRE REMUNERAÇÕES.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mIrps({:.2f}x{:.2f})..........{:.2f}'.format(rb,tx_irps,irps))
   print('\033[1;32m[+]\033[1;36mIs({:.2f}x{:.2f}/100+{:.2f})....{:.2f}'.format(rb,tx_is,tx_is,_is))
   print('\033[1;32m[=]\033[1;36mTotal de imposto..................{:.2f}'.format(ti))
   print('\033[1;32m[#]\033[1;36mRLI({:.2f}-{:.2f})...............{:.2f}'.format(rb,ti,rli))

   
   # Valor a prestar conta a seguradora
   # Formula
   vpcs=pt-(rb-ti)
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mVALOR A PRESTAR CONTA A SEGURADORA.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mVPCS = Prémio total - (RB - Impostos)')
   print('\033[1;32m[#]\033[1;36mVPCS = {:.2f}-({:.2f}-{:.2f})'.format(pt,rb,ti))
   print('\033[1;32m[#]\033[1;36mVPCS = {:.2f}'.format(vpcs))
   print('\033[1;35m*'*45)



# Calculo do premio com outras taxas
def premio_com_taxa_de_suprevisao():

   print('\033[1;35m*'*45)
   print('\033[1;32m==> Calculo do premio total com taxa de suprevisão.')
   print('\033[1;35m*'*45)

   capital=float(input('\033[1;35mValor do capital:\033[1;36m '))
   tx_risco=float(input('\033[1;35mTaxa de risco:\033[1;36m '))
   tx_encargo=float(input('\033[1;35mPercentagem de encargos:\033[1;36m '))
   ca=float(input('\033[1;35mCusto de apolice:\033[1;36m '))
   tx_sa=float(input('\033[1;35mPercentagem de selo de apolice:\033[1;36m '))
   outra_tx=float(input('\033[1;35mPercentagem de taxa de suprevisão:\033[1;36m '))

   # Formulas
   permilagem=tx_risco/1000
   ps=capital*permilagem
   encargos=(tx_encargo/100)*ps
   pc=ps+encargos
   pb=pc+ca
   sa=(tx_sa/100)*pb
   inem=(outra_tx/100)*pb
   pt=pb+sa+inem

   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCALCULO DO PREMIO TOTAL.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mPrémio simples({:.2f}x{:.2f}).....{:.2f}'.format(capital,tx_risco,ps))
   print('\033[1;32m[+]\033[1;36mEncargos({:.2f}x{:.2f}).............{:.2f}'.format(ps,tx_encargo,encargos))
   print('\033[1;32m[=]\033[1;36mPrémio comercial....................{:.2f}'.format(pc))
   print('\033[1;32m[+]\033[1;36mCusto de ápolice....................{:.2f}'.format(ca))
   print('\033[1;32m[=]\033[1;36mPrémio bruto........................{:.2f}'.format(pb))
   print('\033[1;32m[+]\033[1;36mSelo de apolice({:.2f}x{:.2f})..........{:.2f}'.format(pb,tx_sa,sa))
   print('\033[1;32m[+]\033[1;36mTaxa de suprevisão({:.2f}x{:.2f})......{:.2f}'.format(pb,outra_tx,inem))
   print('\033[1;32m[=]\033[1;36mPrémio total..........................{:.2f}'.format(pt))
   print('\033[1;35m*'*45)


def indemnizacao_e_autoseguro():
   # Calculo de indemnização e autoseguro
   print('\033[1;35m*'*45)
   print('\033[1;32mCALCULO DE INDEMNIZAÇÃO E AUTOSEGURO.')
   print('\033[1;35m*'*45)
   cr=float(input('\033[1;35mCapital em risco:\033[1;36m '))
   cs=float(input('\033[1;35mCapital seguro:\033[1;36m '))
   danos=float(input('\033[1;35mDanos:\033[1;36m '))

   # Formulas
   indemnizacao=(cs*danos)/cr
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mINDEMNIZAÇÃO.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mIndemnização = (Capital seguro X Danos)/Capital em risco')
   print('\033[1;32m[#]\033[1;36mIndemnização = ({:.2f}x{:.2f})/{:.2f}'.format(cs,danos,cr))
   print('\033[1;32m[#]\033[1;36mIndemnização = {:.2f}'.format(indemnizacao))
 
   # Calculo de Autoseguro
   # Formulas
   autoseguro=danos-indemnizacao
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mAUTO-SEGURO.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mAuto-seguro = Danos - Indemnização')
   print('\033[1;32m[#]\033[1;36mAuto-seguro = {:.2f} - {:.2f}'.format(danos,indemnizacao))
   print('\033[1;32m[#]\033[1;36mAuto-seguro = {:.2f}'.format(autoseguro))
   print('\033[1;35m*'*45)


def novo_capital():
   # Calculo de novo capital
   print('\033[1;35m*'*45)
   print('\033[1;32mCALCULO DE NOVO CAPITAL.')
   print('\033[1;35m*'*45)
   ca=float(input('\033[1;35mCapital Antigo:\033[1;36m '))
   _ia=float(input('\033[1;35mÌndice Antigo:\033[1;36m '))
   _in=float(input('\033[1;35mÌndice Novo:\033[1;36m '))

   # Formulas
   cn=(ca*_in)/_ia
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCAPITAL SEGURO PARA ANUIDADE SEGUINTE.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mCapital Novo = (Capital Antigo X Ìndice Novo)/Ìndice Antigo')
   print('\033[1;32m[#]\033[1;36mCapital Novo = ({:.2f}x{:.2f})/{:.2f}'.format(ca,_in,_ia))
   print('\033[1;32m[#]\033[1;36mCapital Novo = {:.2f}'.format(cn))
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mR% O valor de capital seguro para anuidade seguinte é de {:.2f}'.format(cn))
   print('\033[1;35m*'*45)


def imposto_de_selo_md():
   # Calculo de imposto de selo usando o md
   print('\033[1;35m*'*45)
   print('\033[1;32mREMUNERAÇÃO DOS MEDIADORES DE SEGURO.')
   print('\033[1;35m*'*45)
   c=float(input('\033[1;35mRemuneração bruta/iliquida:\033[1;36m '))
   tx=float(input('\033[1;35mTaxa de imposto de selo:\033[1;36m '))

   # Formulas
   _is=(c*tx)/(100+tx)
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCalculo de imposto de selo usando metodo directo.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mIs = (C x Tx)/(100+tx)')
   print('\033[1;32m[#]\033[1;36mIs = ({:.2f}x{:.2f})/(100+{:.2f})'.format(c,tx,tx))
   print('\033[1;32m[#]\033[1;36mIs = {:.2f}'.format(_is))
   print('\033[1;35m*'*45)

def rl_is_mi():
   # Calculo de imposto de selo usando o md
   print('\033[1;35m*'*45)
   print('\033[1;32mREMUNERAÇÃO DOS MEDIADORES DE SEGURO.')
   print('\033[1;35m*'*45)
   c=float(input('\033[1;35mRemuneração bruta/iliquida:\033[1;36m '))
   tx=float(input('\033[1;35mTaxa de imposto de selo:\033[1;36m '))

   # Formulas
   c1=(c*100)/(100+tx)
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCalculo de remuneração liquida de imposto de selo usando metodo indirecto.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mC1 = (C x 100)/(100+tx)')
   print('\033[1;32m[#]\033[1;36mC1 = ({:.2f}x100)/(100+{:.2f})'.format(c,tx))
   print('\033[1;32m[#]\033[1;36mC1 = {:.2f}'.format(c1))
   print('\033[1;35m*'*45)


def irps():
   # Calculo de imposto de selo usando o md
   print('\033[1;35m*'*45)
   print('\033[1;32mREMUNERAÇÃO DOS MEDIADORES DE SEGURO.')
   print('\033[1;35m*'*45)
   c=float(input('\033[1;35mRemuneração bruta/iliquida:\033[1;36m '))
   tirps=float(input('\033[1;35mTaxa de IRPS:\033[1;36m '))

   # Formulas
   irps=c*(tirps/100)
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCalculo de IRPS.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mIrps = C x (tirps/100)')
   print('\033[1;32m[#]\033[1;36mIrps = {:.2f}x({:.2f}/100)'.format(c,tirps))
   print('\033[1;32m[#]\033[1;36mIrps = {:.2f}'.format(irps))
   print('\033[1;35m*'*45)


def rli():
   # Calculo de imposto de selo usando o md
   print('\033[1;35m*'*45)
   print('\033[1;32mREMUNERAÇÃO DOS MEDIADORES DE SEGURO.')
   print('\033[1;35m*'*45)
   c=float(input('\033[1;35mRemuneração bruta/iliquida:\033[1;36m '))
   _is=float(input('\033[1;35mImposto de selo:\033[1;36m '))
   irps=float(input('\033[1;35mIrps:\033[1;36m '))

   # Formulas
   rli=c-_is-irps
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCalculo de remuneração liquida de imposto de selo.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mRli = C - Is - Tirps')
   print('\033[1;32m[#]\033[1;36mRli = {:.2f}-{:.2f}-{:.2f}'.format(c,_is,irps))
   print('\033[1;32m[#]\033[1;36mRli = {:.2f}'.format(rli))
   print('\033[1;35m*'*45)

def _is():
   # Calculo de imposto de selo usando o md
   print('\033[1;35m*'*45)
   print('\033[1;32mREMUNERAÇÃO DOS MEDIADORES DE SEGURO.')
   print('\033[1;35m*'*45)
   c=float(input('\033[1;35mRemuneração bruta/iliquida:\033[1;36m '))
   c1=float(input('\033[1;35mRemuneração liquida:\033[1;36m '))

   # Formulas
   a=c*100
   b=c1*100
   tx=(a-b)/c1
   
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32mCalculo de taxa de imposto de selo.')
   print('\033[1;35m*'*45)
   print('\033[1;32m[#]\033[1;36mtx = [(Cx100)-(c1*100)]/c1')
   print('\033[1;32m[#]\033[1;36mtx = [({:.2f}x100) - ({:.2f}x100)]/{:.2f}'.format(c,c1,c1))
   print('\033[1;32m[#]\033[1;36mtx = {:.2f}'.format(tx))
   print('\033[1;35m*'*45)


def menu():

   print('''\033[1;32m
  oooooo
  o    o                         
  o      oooooo oo  o oooooooo                  
  o      o    o ooo o    oo     
  o    o o    o o  oo    oo   \033[1;36m<<oo>>\033[1;32m
  oooooo oooooo o  oo    oo   \033[1;36m<<oo>>\033[1;32m  
                                      
  oooooo
  oo   oo ooooo ooooooo o    o ooooooo  oooooo ooooo
  oooo    o     o       o    o o     o  o    o o   o
      oo  ooooo o   ooo o    o oooooo   o    o o
  oo   oo o     o     o o    o o     o  o    o ooooo
  ooooooo ooooo ooooooo oooooo o      o oooooo     o
                                               o   o
                                               ooooo
''')
    
   # Output's
   print('\033[1;35m*'*45)
   print('\033[1;32m=====> CONTABILIDADE DE SEGUROS. <=====')
   print('\033[1;35m*'*45)
   print('\033[1;32m[1]\033[1;36m Mediação de seguro;')
   print('\033[1;32m[2]\033[1;36m Calculo do prémio total com outras taxas[INEM];')
   print('\033[1;32m[3]\033[1;36m Calculo do premio total sem outras taxas[INEM];')
   print('\033[1;32m[4]\033[1;36m Calculo do premio total com taxa de suprevisão;')
   print('\033[1;32m[5]\033[1;36m Indemnização e Auto-seguro;')
   print('\033[1;32m[6]\033[1;36m Calculo de novo capital;')
   print('\033[1;32m[7]\033[1;36m Calculo de imposto de selo usando metodo directo(Is);')
   print('\033[1;32m[8]\033[1;36m Calculo de remuneração liquida de imposto de selo usando metodo indirecto(C1);')
   print('\033[1;32m[9]\033[1;36m Calculo de Irps(Irps);')
   print('\033[1;32m[10]\033[1;36m Calculo de Rli(Rli);')
   print('\033[1;32m[11]\033[1;36m Calculo da taxa de imposto de selo(tx);')
   print('\033[1;32m[12]\033[1;36m Sair do programa;')
   op=int(input('\033[1;32m[Opção]\033[1;36m Digite a opção: '))
   
   # Inicialização
   if op==1:
      mediacao_de_seguro()
   elif op==2:
        premio_com_outras_taxas()
   elif op==3:
        premio_sem_outras_taxas()
   elif op==4:
        premio_com_taxa_de_suprevisao()
   elif op==5:
        indemnizacao_e_autoseguro()
   elif op==6:
        novo_capital()
   elif op==7:
        imposto_de_selo_md()
   elif op==8:
        rl_is_mi()
   elif op==9:
        irps()
   elif op==10:
        rli()
   elif op==11:
        _is()
   elif op==12:
        sys.exit()
   else:
      print('\033[1;31m[Inválido!]\033[1;31m OPÇÃO INVÁLIDA!')
      sys.exit()
   


menu()