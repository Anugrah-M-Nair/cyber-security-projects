import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Client: {message}")
            response = f"Chatbot: You said '{message}'"
            client_socket.send(response.encode())
        except:
            break
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 12345))
    server.listen()
    print("[SERVER STARTED] Waiting for connections...")
    
    while True:
        client_socket, _ = server.accept()
        print("[NEW CONNECTION] Client connected.")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
