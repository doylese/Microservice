import socket


def send_file_path(file_path, host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(file_path.encode('utf-8'))
        response = s.recv(1024)
        print(f"Server response: {response.decode('utf-8')}")


def print_intro():
    print("-" * 60)
    print("WELCOME TO THE PRINT DIALOG AUTOMATION MICROSERVICE")
    print("This microservice will open the document and bring up the print dialog.")
    print("-" * 60)
    print("\nInstructions:\n")
    print("  > The server listens for a file path to open.")
    print("  > On receiving the file path, the server opens the document.")
    print("  > The server then simulates Ctrl+P to open the print dialog.")
    print("  > A response is sent back to the client upon completion.\n")
    print("-" * 60)


if __name__ == "__main__":
    print_intro()
    while True:  # Add a loop to allow multiple requests
        file_path = input("Enter the file path to send (or type 'exit' to quit): ")
        if file_path.lower() == 'exit':  # Provide a way to exit the loop
            break
        send_file_path(file_path)
