import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("tentative de connexion au serveur...")
sock.connect(('10.1.1.2', 8889))

sock.send('Hello' .encode())

data = sock.recv(1024)
print(f"Message reçu du serveur : {data.decode()}")

# on récup une string saisie par l'utilisateur
msg = input('Calcul à envoyer (ex: "3 + 3"): ')

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
print(f"Envoi du message : {payload}")
sock.send(payload)

result = sock.recv(1024)
print(f"Résultat reçu du serveur : {result.decode()}")
sock.close()



