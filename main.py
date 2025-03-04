from password_manager import PasswordManager
from ssl_checker import SSLCertificateChecker
# from encryptor import Encryptor  # Encryptor クラスができたら追加！

def main():
    # 🔹 パスワードマネージャーの動作確認
    print("=== Password Manager ===")
    manager = PasswordManager()
    original_password = "secure_password"
    hashed_pw = manager.hash_password(original_password)
    print(f"ハッシュ化されたパスワード: {hashed_pw}")

    result = manager.check_password("secure_password", hashed_pw)
    print("パスワードが一致:", result)

    # 🔹 SSL 証明書チェッカーの動作確認
    print("\n=== SSL Certificate Checker ===")
    checker = SSLCertificateChecker("www.google.com")
    cert = checker.get_certificate()
    print(f"取得した証明書: {cert}")

    # 🔹 もし Encryptor クラスを作ったらここに追加
    # print("\n=== Encryptor ===")
    # encryptor = Encryptor()
    # encrypted_data = encryptor.encrypt("Hello, World!")
    # print(f"暗号化データ: {encrypted_data}")

if __name__ == "__main__":
    main()
