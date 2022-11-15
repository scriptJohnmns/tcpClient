import socket

ip = input("Digite o IP a ser utilizado: ")
port = input("Digite a porta a ser utilizada: ")
msg = input("Digite a mensagem a ser enviada: ")
bytes_str = input("Digite o tamanho de bytes da mensagem: ")

ip = str(ip)
port = int(port)
bytes_str = int(bytes_str)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(15)
try:
    client.connect((ip, port))
    client.send(msg.encode())
    pcts_recebidos = client.recv(bytes_str).decode()
    print(pcts_recebidos)
except:
    print("Um erro ocorreu")




