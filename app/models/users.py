from .database import Base
from sqlalchemy import Column, String, Integer
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from secrets import compare_digest
import base64
import os


class Users(Base):
    """класс модели пользователя"""
    __tablename__ = "users"  # название таблицы

    # колонки в БД
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True, unique=True, nullable=True)
    email = Column(String(100), index=True, nullable=True)
    password_hash = Column(String(255), nullable=True)
    password_salt = Column(String(255), nullable=False)

    def set_password(self, password: str):
        """хеширует пароль и сохраняет его"""
        salt = os.urandom(32)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        password_hash = kdf.derive(password.encode('utf-8'))
        self.password_hash = base64.b64encode(password_hash).decode('utf-8')
        self.password_salt = base64.b64encode(salt).decode('utf-8')

    def check_password(self, password: str) -> bool:
        """сравнивает пароль с хешом"""
        try:
            salt = base64.b64decode(self.password_salt.encode('utf-8'))
            old_hash = base64.b64decode(self.password_hash.encode('utf-8'))

            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            new_hash = kdf.derive(password.encode('utf-8'))

            return compare_digest(old_hash, new_hash)
        except Exception:
            return False