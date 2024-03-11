import socket
import os
import time
from pywinauto.keyboard import send_keys


def open_file_print_dialog(file_path):
    if os.path.exists(file_path):
        try:
            # Open the document
            os.startfile(file_path)
            print("Document opened: " + file_path)

            # Wait for document
            time.sleep(4)

            send_keys('^p')
            time.sleep(1)
            return "complete"
        except Exception as e:
            print(f"Error: {e}")
            return "error opening file"
    else:
        return "file not found"


def start_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file_path = data.decode('utf-8')
                    result = open_file_print_dialog(file_path)
                    conn.sendall(result.encode('utf-8'))


if __name__ == "__main__":
    start_server()
