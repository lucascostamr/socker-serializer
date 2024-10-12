from socketserver import StreamRequestHandler, TCPServer
from os import environ

class SocketServer(StreamRequestHandler):

    def handle(self):
        self.data = self.rfile.read().strip()
        print("{} sent a file".format(self.client_address[0]))

        mimetype, data = self.data.decode().split(";")

        with open("public/results/result." + mimetype, "w") as file:
            file.write(data)

if __name__ == "__main__":
    HOST, PORT = environ.get("SERVER_HOST"), int(environ.get("SERVER_PORT"))

    with TCPServer((HOST, PORT), SocketServer) as server:
        server.serve_forever()