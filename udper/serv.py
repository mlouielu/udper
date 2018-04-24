import socket
from collections import Counter


BUFFER_SIZE = 65535


def create_udp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    return sock


def receive_and_count(sock):
    c = Counter()
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        c[hash(data)] += 1

        print(c)


if __name__ == '__main__':
    sock = create_udp('0.0.0.0', 6600)
    receive_and_count(sock)
