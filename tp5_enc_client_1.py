import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))
sock.send("Hello" .encode())

data = sock.recv(1024)

msg = input('Calcul a envoyé: ')

sock.send(msg.encode())

encoded_msg = msg.encode('utf-8')

msg_len = len(encoded_msg)

header = msg_len.to_bytes(4, byteorder='big')

payload = header + encoded_msg


sock_data = sock.recv(1024)
print(sock_data.decode())

sock.send(payload)
sock.close()
