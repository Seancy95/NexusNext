"""Assessment-only guard: deny non-loopback socket connections."""
from __future__ import annotations

import ipaddress
import socket

_original_connect = socket.socket.connect


def _is_loopback(host: object) -> bool:
    text = str(host).strip().strip("[]")
    if text.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_address(text).is_loopback
    except ValueError:
        return False


def _guarded_connect(sock: socket.socket, address: object):
    if isinstance(address, tuple) and address and _is_loopback(address[0]):
        return _original_connect(sock, address)
    raise OSError("CLOUD-EVAL-B02 assessment blocked non-loopback network access")


socket.socket.connect = _guarded_connect
