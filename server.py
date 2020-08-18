from socket import *    

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 3333
serverSocket.bind(("", serverPort))
serverSocket.listen(10)

print ('#########################################')
print ('Servidor rodando em http://localhost:3333')
print ('#########################################')	

while True:
	connectionSocket, addr = serverSocket.accept()
	print ('[*] Requisição efetuada por cliente:' + str(addr));	
	
	try:
		message =  connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:]).read()
		outputdata = bytes(f, 'utf8')
		
		connectionSocket.send(b"HTTP/1.1 200 OK\n\n")
		connectionSocket.send(outputdata)
		connectionSocket.close()

	except IOError:
		notFound = open('NotFound.html').read()
		notFoundOutput = bytes(notFound, 'utf8')

		connectionSocket.send(b"HTTP/1.1 404 Not Found\n\n")
		connectionSocket.send(notFoundOutput)
		connectionSocket.close()

serverSocket.close()