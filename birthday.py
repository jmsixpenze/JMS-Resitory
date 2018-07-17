def data_de_nascimento():
  try:
   dia, mes, ano = input('\033[1;36mData (dd/mm/aaa): ').split('/')
   meses=['Janeiro','Fevereiro','Março','Abril','Maio','Junho'
      ,'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
   print('Voce nasceu em: ')
   print('{} de {} de {}'.format(dia,meses[int(mes)-1],ano))

  except Exception as err:
       print('\033[1;31mAconteceu um erro:\033[0;31m',err)
       print('\033[1;32mTente de novo: Por exemplo: 20/02/1999\n')
       data_de_nascimento()
data_de_nascimento()        


