from unittest import TestCase, main
from unittest.mock import MagicMock, patch

from socket_client import SocketClient


class SocketClientTest(TestCase):

    @patch("socket_client.socketpair")
    def test_should_return_file_extension_on_success(self, mock_socket):
        mock_socket.create_connection.return_value = None
        sut = SocketClient()
        response = sut._get_file_extension("fake.json")
        self.assertEqual(response, ".json")

    @patch("builtins.open")
    @patch.object(SocketClient, "_socket_connect")
    def test_should_call_socket_methods_with_correct_values(
        self, mock_socket, mock_open
    ):
        mock_client_socket = MagicMock()
        mock_socket.return_value = mock_client_socket
        mock_client_socket.send.return_value = None
        mock_client_socket.sendall.return_value = None
        mock_client_socket.close.return_value = None

        mock_open_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_open_file
        mock_open_file.read.return_value = b"fake_content"

        sut = SocketClient()
        sut.send_file("fake.json")

        mock_client_socket.send.assert_called_with(".json")
        mock_client_socket.sendall.assert_called_with(b"fake_content")

        mock_client_socket.close.assert_called_once()


if __name__ == "__main__":
    main()
