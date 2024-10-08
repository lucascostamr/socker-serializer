from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)
from os import path
from os import environ


class SocketClient:
    def __init__(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        self._client_socket = client_socket.connect((
            environ.get("SERVER_HOST"),
            int(environ.get("SERVER_PORT"))
        ))

    def send_file(self, filepath: str) -> None:
        file_extension = self._get_file_extension(filepath=filepath)
        self._client_socket.send(file_extension)

        with open(filepath, "rb") as f:
            bytes_read = f.read()

        self._client_socket.sendall(bytes_read)

        print(f"[*] File sent successfully.")
        self._client_socket.close()

    def _get_file_extension(self, filepath: str) -> str:
        filename = path.basename(filepath)
        return path.splitext(filename)[1]
