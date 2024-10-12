from os import environ, path
from socket import AF_INET, SOCK_STREAM, socket


class SocketClient:

    def send_file(self, filepath: str) -> None:
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect(
                (environ.get("SERVER_HOST"), int(environ.get("SERVER_PORT")))
            )

            file_extension = self._get_file_extension(filepath=filepath)
            sock.send(file_extension.encode())

            with open(filepath, "rb") as f:
                bytes_read = f.read()

            sock.sendall(bytes_read)

        print("[✔] File sent successfully.")

    def _get_file_extension(self, filepath: str) -> str:
        filename = path.basename(filepath)
        return path.splitext(filename)[1][1:] + ";"


if __name__ == "__main__":
    socket_client = SocketClient()
    socket_client.send_file(filepath="public/file.json")
    socket_client.send_file(filepath="public/file.xml")
    socket_client.send_file(filepath="public/file.csv")
    socket_client.send_file(filepath="public/file.toml")
    socket_client.send_file(filepath="public/file.yml")
