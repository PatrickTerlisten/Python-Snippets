"""
This snippets shows how to work with untrusted SSL certificates
when using pyVim. Should work with other modules as well.
"""

from pyVim.connect import SmartConnect
import ssl


s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

c = SmartConnect(host="192.168.20.1", user="root",
                 pwd='Passw0rd', sslContext=s)

print(c.CurrentTime())
