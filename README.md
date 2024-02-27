# Print Dialog Automation Microservice

## Table of Contents
- [About The Project](#about-the-project)
- [Uses](#uses)
- [Instruction](#instruction)
- [Request Data](#request-data)
- [Receive Data](#receive-data)
- [UML](#uml)

## About The Project

This microservice automates the process of opening a document and bringing up the print dialog using the Ctrl+P command. Once the client program establishes a connection to the server via Socket, the microservice will listen for the file path to the document. Upon receiving the file path, the microservice will attempt to open the document and bring up the print dialog.

The microservice sends back a status message indicating the completion of the action or an error if encountered.

## Uses

- Python
- Socket
- pywinauto

## Instruction

Communication between the server (microservice) and the client program is made via Socket. The file path is entered by the user when prompted by the client program, as the microservice does not hold information about the client's file system.

### Start the Microservice

To start the microservice, run the `main.py` script in your terminal or command prompt.

### Request Data

#### How to request data from the microservice:

1. Import the socket module:
    ```python
    import socket
    ```
2. Create a socket object:
    ```python
    s = socket.socket()
    ```
3. Define the port on which you want to connect:
    ```python
    port = 12345
    ```
4. Connect to the server on the local computer:
    ```python
    s.connect(('127.0.0.1', port))
    ```
5. Send the file path by encoding the string:
    ```python
    file_path = "C:\\path\\to\\your\\document.docx"
    s.send(file_path.encode())
    ```

The microservice will then process this request to open the document and bring up the print dialog.

## Receive Data

#### How to receive data from the microservice:

1. Receive the status message by decoding to get the string:
    ```python
    response = s.recv(1024).decode()
    ```
    The decoded string will be either "complete" indicating success or an error message.

## UML

![UML Sequence Diagram](/uml.png)

[Back to Top](#print-dialog-automation-microservice)
