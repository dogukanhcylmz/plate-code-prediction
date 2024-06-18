import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9999)
client_socket.connect(server_address)
print(client_socket.recv(1024).decode())

try:
    while True:

        prediction = input("Your guess: ")
        client_socket.sendall(bytes(prediction, 'utf-8'))

        recv = client_socket.recv(1024).decode()
        print(recv)

        if prediction.upper() == "END":
            client_socket.close()
            break

        if not recv.startswith("You have entered"):
            client_socket.close()
            break


finally:
    client_socket.close()
