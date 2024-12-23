import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('10.1.1.2', 8889))
sock.listen(1)

print("En attente de connexion...")
client, client_addr = sock.accept()
print("connexion établie avec {client_addr}")

while True:
    # On lit les 4 premiers octets qui arrivent du client
    # Car dans le client, on a fixé la taille du header à 4 octets
    header = client.recv(4)
    if not header:
        print("connexion fermée par le client.")
        break

    # On lit la valeur
    msg_len = int.from_bytes(header[0:4], byteorder='big')

    print(f"Lecture des {msg_len} prochains octets")

    # Une liste qui va contenir les données reçues
    chunks = []

    bytes_received = 0
    while bytes_received < msg_len:
        # Si on reçoit + que la taille annoncée, on lit 1024 par 1024 octets
        chunk = client.recv(min(msg_len - bytes_received,
                                1024))
        if not chunk:
            raise RuntimeError('Invalid chunk received bro')

        # on ajoute le morceau de 1024 ou moins à notre liste
        chunks.append(chunk)

        # on ajoute la quantité d'octets reçus au compteur
        bytes_received += len(chunk)

    # ptit one-liner pas combliqué à comprendre pour assembler la liste en un seul message
    message_received = b"".join(chunks).decode('utf-8')
    print(f"Données reçues du client : {message_received}")

    try:
        res = eval(message_received())
        client.send(str(res).encode())
    except Exception as e:
       client.send(f"Erreur: {str(e)}".encode())

client.close()
sock.close()

