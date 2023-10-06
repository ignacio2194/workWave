from cryptography.fernet import Fernet
from workwave.apps.users.api.views import *


value = "asda3123"
print(value)
key = Fernet.generate_key()
print(key)
object_encrypted = Fernet(key)
print(type(object_encrypted))
encrypted_password = object_encrypted.encrypt(value.encode())
print(encrypted_password)
