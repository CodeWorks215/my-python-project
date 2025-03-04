import ssl
import socket

class SSLCertificateChecker:
    def __init__(self, hostname: str):
        self.hostname = hostname

    def get_certificate(self):
        """SSL証明書を取得"""
        context = ssl.create_default_context()
        with socket.create_connection((self.hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                return ssock.getpeercert()

    def display_certificate(self):
        """証明書を表示"""
        cert = self.get_certificate()
        print("証明書情報:")
        for key, value in cert.items():
            print(f"{key}: {value}")
