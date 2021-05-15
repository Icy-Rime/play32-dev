import socket as cpy_socket

AF_INET = cpy_socket.AF_INET
AF_INET6 = cpy_socket.AF_INET6
IPPROTO_IP = cpy_socket.IPPROTO_IP
IPPROTO_TCP = cpy_socket.IPPROTO_TCP
IPPROTO_UDP = cpy_socket.IPPROTO_UDP
IP_ADD_MEMBERSHIP = cpy_socket.IP_ADD_MEMBERSHIP
SOCK_DGRAM = cpy_socket.SOCK_DGRAM
SOCK_RAW = cpy_socket.SOCK_RAW
SOCK_STREAM = cpy_socket.SOCK_STREAM
SOL_SOCKET = cpy_socket.SOL_SOCKET
SO_REUSEADDR = cpy_socket.SO_REUSEADDR

def socket(af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP):
    return cpy_socket.socket(af, type, proto)
def getaddrinfo(host, port, af=0, type=0, proto=0, flags=0):
    return cpy_socket.getaddrinfo(host, port, af, type, proto, flags)
