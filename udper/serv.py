import pickle
import socket
from collections import Counter


BUFFER_SIZE = 65535
BACKTO = ('192.168.231.234', 9000)


def create_udp(ip, port, timeout=2):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    sock.settimeout(timeout)
    return sock


def receive_and_count(sock):
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c = Counter()
    while True:
        try:
            data, addr = sock.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            if c:
                print('RESULT')
                print(c)

                # Send back
                udp.sendto(pickle.dumps(c), BACKTO)
            c = Counter()
        else:
            c[data[0]] += 1


if __name__ == '__main__':
    sock = create_udp('0.0.0.0', 6600)
    receive_and_count(sock)
