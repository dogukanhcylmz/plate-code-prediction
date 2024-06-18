import socket
import random
import pandas as pd

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind(('localhost', 9999))
socket.listen(1)

plate_data = dict(pd.read_excel('plate_list.xlsx')[['CityName', 'PlateNumber']].values)
clientNumber = 1
cities = list(plate_data.keys())

while True:

    print(f"Waiting for {clientNumber}th client connection")
    print("Server is waiting for connection...")

    connection, client_address = socket.accept()
    print("Client connected from: ", client_address)
    
    city_name = random.choice(cities)
    connection.sendall(bytes("What is the plate code of{}".format(city_name), 'utf-8'))
    clientNumber += 1

    while True:

        prediction = connection.recv(1024).decode('utf-8')
        print("Received from client: ", prediction)

        if prediction == "END":
            connection.close()
            socket.close()
            exit()

        elif not prediction.isdigit():
            connection.sendall(bytes("You entered a non-numeric value. Game Over.", 'utf-8'))
            break

        elif int(prediction) == plate_data[city_name]:
            connection.sendall(bytes("Correct!", 'utf-8'))
            break

        elif int(prediction) < 1 or int(prediction) > 81:
            connection.sendall(bytes("Number exceeds the range. Game Over.", 'utf-8'))
            break

        else:
            plate_code = int(prediction)
            if plate_code in plate_data.values():
                city = next(key for key, value in plate_data.items() if value == plate_code)
                connection.sendall(bytes("You have entered the plate code of {}.".format(city), 'utf-8'))

    connection.close()
