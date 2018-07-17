from socket import *

s=socket(AF_INET,SOCK_STREAM)
host='127.0.0.1'
port=8080

msg='===> WELCOME TO SIXPENZE PANNEL ===>>'
s.bind((host, port))
s.listen(1000)
while True:
      c, e = s.accept()
      print("\033[1;32mConectado com: \033[1;36m",e)
      c.send(msg.encode('ascii'))
      c.close()


