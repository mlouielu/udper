import socket


def create_udp(dscp=0x0):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if dscp:
        sock.setsockopt(socket.SOL_IP, socket.IP_TOS, dscp)
    return sock


def sendto(sock, host, port, data):
    sock.sendto(data, (host, port))


if __name__ == '__main__':
    sock = create_udp()
    DUMMY_1 = b'\x00' * 1024
    DUMMY_2 = b'\xff' * 1024

    sendto(sock, 'localhost', 6600, DUMMY_1)
    sendto(sock, 'localhost', 6600, DUMMY_2)
