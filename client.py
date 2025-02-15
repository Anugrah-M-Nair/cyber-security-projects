import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12345))
    print("[CONNECTED] Type messages (or 'exit' to quit)")

    while True:
        message = input("You: ")
        if message.lower() == "exit":
            break
        client.send(message.encode())
        response = client.recv(1024).decode()
        print(response)

    client.close()

if __name__ == "__main__":
    start_client()
