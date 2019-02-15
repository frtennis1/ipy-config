from cryptography.fernet import Fernet

fe = Fernet(b'gda0KrfQjVKFtc9xaQMAc394ZkS8ePWz9A1wJf39REU=')

with open('payload.txt', 'rb') as f:
    payload = f.read()


decrypted = fe.decrypt(payload).decode()

with open('decrypted_payload.txt', 'w') as f:
    f.write(decrypted)

