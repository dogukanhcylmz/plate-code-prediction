# Description
- A mini application to utilize socket programming

- The main point of this project is the creation of a plate code prediction system, where a client interacts with a server to predict the plate code of a randomly selected city. 

- TCP sockets is used to communicate between the client and server that occurs within the same host, local host communication. The client responsible for initiating a connection with the server, receiving prompts for predictions, and subsequently sending user inputs for evaluation. Conversely, the server awaits client connections, it reads the excel file from the server side, selects a city at random, and requests predictions from clients. It then confirms the predictions and provides feedback, accordingly, and closing connections upon correct input. If the predicted plate code is from another city, the client is informed by the city's name. If the prediction is not a valid plate code, or if it is not a numeric value, it sends the corresponding message and terminates the connection with the client. Then it waits for another client. Also, if the client enters “END”, both the client side and server-side operation terminate. 
