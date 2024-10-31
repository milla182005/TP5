import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))
sock.send('Hello' .encode())

data = sock.recv(1024)

# on récup une string saisie par l'utilisateur
msg = input('Calcul à envoyer: ')

sock.send(msg.encode())

# on encode le message explicitement en UTF-8 pour récup un tableau de bytes
encoded_msg = msg.encode('utf-8')

# on calcule sa taille, en nombre d'octets
msg_len = len(encoded_msg)

# on encode ce nombre d'octets sur une taille fixe de 4 octets
header = msg_len.to_bytes(4, byteorder='big')

# on peut concaténer ce header avec le message, avant d'envoyer sur le réseau
payload = header + encoded_msg

sock_data = sock.recv(1024)
print(sock_data.decode())

# on peut envoyer ça sur le réseau
sock.send(payload)
sock.close()
