from os import environ, path
from socket import socketpair


class SocketClient:
    def __init__(self):
        self._client_socket = self._socket_connect()
        print(self._client_socket)

    def send_file(self, filepath: str) -> None:
        file_extension = self._get_file_extension(filepath=filepath)
        self._client_socket.send(file_extension)

        with open(filepath, "rb") as f:
            bytes_read = f.read()

        self._client_socket.sendall(bytes_read)

        print("[✔] File sent successfully.")
        self._client_socket.close()

    def _get_file_extension(self, filepath: str) -> str:
        filename = path.basename(filepath)
        return path.splitext(filename)[1]

    def _socket_connect(self) -> None:
        client_socket = socketpair()
        return client_socket.create_connection(
            (environ.get("SERVER_HOST"), int(environ.get("SERVER_PORT")))
        )
