from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self):
        """鍵を生成する"""
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data: str) -> bytes:
        """データを暗号化する"""
        return self.cipher.encrypt(data.encode('utf-8'))

    def decrypt(self, encrypted_data: bytes) -> str:
        """暗号化されたデータを復号化する"""
        return self.cipher.decrypt(encrypted_data).decode('utf-8')

# 動作確認
if __name__ == "__main__":
    encryptor = Encryptor()

    message = "これは機密情報です"
    encrypted_message = encryptor.encrypt(message)
    print(f"暗号化されたデータ: {encrypted_message}")

    decrypted_message = encryptor.decrypt(encrypted_message)
    print(f"復号化されたデータ: {decrypted_message}")
