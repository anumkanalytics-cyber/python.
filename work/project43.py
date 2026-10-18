import bcrypt
from typing import Tuple
from datetime import datetime


# Handler functions
def hash_pwd(password: str, rounds: int = 12) -> bytes:
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(rounds=rounds)
    )


def check_pwd(password: str, password_hash: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), password_hash)


class Userauth:
    def __init__(self):
        self.users = {}
        self.login_attempts = {}
        self.max_attempts = 3
        self.lockout_minutes = 15

    def add_user(self, username: str, password: str) -> bool:
        if username in self.users:
            return False

        self.users[username] = {
            "pwd_hash": hash_pwd(password),
            "created_at": datetime.now(),
            "pwd_rounds": 12
        }
        return True

    def login(self, username: str, password: str) -> Tuple[bool, str]:
        if self._is_locked(username):
            return False, "Too many attempts, account locked!"

        if username not in self.users:
            return False, "Invalid user info."

        user = self.users[username]

        if not check_pwd(password, user["pwd_hash"]):
            self._track_attempt(username)
            return False, "Invalid user info."

        # Clear failed attempts after a successful login
        if username in self.login_attempts:
            del self.login_attempts[username]

        self._upgrade_hash(username, password)

        return True, "Success!"

    def _is_locked(self, username: str) -> bool:
        if username not in self.login_attempts:
            return False

        attempts, last_attempt = self.login_attempts[username]

        if attempts >= self.max_attempts:
            mins_passed = (
                datetime.now() - last_attempt
            ).total_seconds() / 60

            if mins_passed < self.lockout_minutes:
                return True

            # Lockout period has expired
            del self.login_attempts[username]

        return False

    def _track_attempt(self, username: str):
        now = datetime.now()

        if username in self.login_attempts:
            attempts, _ = self.login_attempts[username]
            self.login_attempts[username] = (attempts + 1, now)
        else:
            self.login_attempts[username] = (1, now)

    def _upgrade_hash(self, username: str, password: str):
        user = self.users[username]
        min_rounds = 14

        if user["pwd_rounds"] < min_rounds:
            user["pwd_hash"] = hash_pwd(password, min_rounds)
            user["pwd_rounds"] = min_rounds


if __name__ == "__main__":
    auth = Userauth()

    user = "AnumKhan"
    pwd = "Anumk1234"  # Test password only

    if auth.add_user(user, pwd):
        print("Account created!")

    success, msg = auth.login(user, pwd)
    print("Good login:", msg)

    for i in range(4):
        success, msg = auth.login(user, "WrongPassword123")
        print(f"Bad login {i + 1}: {msg}")

    for i in range(4):
        success, msg = auth.login(user, "AKK!")
        print(f"bad login: {i+ 1}:{msg} ")
