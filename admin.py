from socket import *

s=socket(AF_INET,SOCK_STREAM)

host=''
port=8080

s.connect((host, port))
dados = s.recv(1024)
print('\033[1;32m',dados.decode('ascii'))
