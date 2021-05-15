import ssl

def wrap_socket(sock, server_side=False, keyfile=None, certfile=None, cert_reqs=ssl.CERT_NONE, ca_certs=None, do_handshake=True, **kws):
    return ssl.wrap_socket(sock, keyfile, certfile, server_side, cert_reqs, ca_certs=ca_certs, do_handshake_on_connect=do_handshake).makefile("rwb")
