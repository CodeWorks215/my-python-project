import bcrypt

class PasswordManager:
    def __init__(self):
        pass

    def hash_password(self, password: str) -> bytes:
        """パスワードをハッシュ化する"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password: str, hashed_password: bytes) -> bool:
        """入力されたパスワードが一致するか検証"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# 動作確認
if __name__ == "__main__":
    manager = PasswordManager()
    original_password = "secure_password"

    hashed_pw = manager.hash_password(original_password)
    print(f"ハッシュ化されたパスワード: {hashed_pw}")

    result = manager.check_password("secure_password", hashed_pw)
    print("パスワードが一致:", result)
