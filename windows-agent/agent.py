import socket
import threading

HOST = "0.0.0.0"
PORT = 8765


def handle_client(client_socket, address):
    print(f"Chromebook connected: {address}")

    try:
        client_socket.sendall(
            b"WINDOWS_FOR_CHROMEBOOK_CONNECTED"
        )

        while True:
            data = client_socket.recv(4096)

            if not data:
                break

            print(f"Received: {data.decode('utf-8', errors='replace')}")

    except ConnectionError:
        pass

    finally:
        print(f"Chromebook disconnected: {address}")
        client_socket.close()


def start_server():
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))
    server.listen()

    print("===================================")
    print(" Windows for Chromebook Agent")
    print("===================================")
    print(f"Listening on port {PORT}")
    print("Waiting for Chromebook...")

    while True:
        client_socket, address = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address),
            daemon=True
        )

        thread.start()


if __name__ == "__main__":
    start_server()
