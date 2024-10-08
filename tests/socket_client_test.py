from unittest import (
    main,
    TestCase
)
from unittest.mock import patch

from src.socket_client import SocketClient


class Test(TestCase):

    @patch("src.socket_client.socket")
    def test_should_return_file_extension_on_success(self, mock_socket):
        mock_socket.return_value.connect = lambda _: "fake_connection"
        sut = SocketClient()
        response = sut._get_file_extension("fake.json")
        self.assertEqual(response, ".json")


if __name__ == "__main__":
    main()
