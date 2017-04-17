"""
This snippets shows how to work with untrusted SSL certificates
when using pyVim. Should work with other modules as well.
"""

import ssl

from pyVim.connect import SmartConnect

SSLCONTEXT = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
SSLCONTEXT.verify_mode = ssl.CERT_NONE

PYVIM = SmartConnect(host="192.168.20.1", user="root",pwd='Passw0rd', sslContext=SSLCONTEXT)

print(PYVIM.CurrentTime())
