import pickle
import time
import socket


def create_udp(dscp=0x0):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if dscp:
        sock.setsockopt(socket.SOL_IP, socket.IP_TOS, dscp)
    return sock


def create_udp_recv(ip, port, timeout=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    sock.settimeout(timeout)
    return sock


def sendto(sock, host, port, data):
    sock.sendto(data, (host, port))


if __name__ == '__main__':
    recv = create_udp_recv('0.0.0.0', 9000)
    sock_1 = create_udp()
    sock_2 = create_udp(0xE0)
    DUMMY_1 = b'\x00' * 160
    DUMMY_2 = b'\x10' * 160

    for t in range(10):
        for pk in range(60):
            for _ in range(50):
                sendto(sock_2, 'localhost', 6600, DUMMY_2)
            for _ in range(50):
                sendto(sock_1, 'localhost', 6600, DUMMY_1)
        time.sleep(4)
        print('RECV')
        data, addr = recv.recvfrom(65535)
        print(pickle.loads(data))
