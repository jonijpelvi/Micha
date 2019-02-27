import socket
from http_class import HTTP
from http_request_class import Request
http = HTTP()
request_handler = Request(".\\root", "index.html")

IP = "192.168.1.154"
port = 80


def handle_request(client_sock):
    if http.get_check_request(client_sock):
        if http.request[0] == "GET":
            request_handler.take_request(http.request)
            request_handler.check_get_send(client_sock)
        elif http.request[0] == "POST":
            pass


def main():
    sock = socket.socket()
    sock.bind((IP, port))
    sock.listen(25)
    while True:
        print("Awaiting Connection...")
        client_sock, addr = sock.accept()
        print("Connection established!")
        handle_request(client_sock)
        print("Closing connection.")
        client_sock.close()


if __name__ == "__main__":
    main()
