import time
from datetime import datetime
from flask import Flask, request
import json
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from cryptography import exceptions as cryptoExceptions
from cryptography.fernet import InvalidToken as fernetException

app = Flask(__name__)
messagesStorage = []
credentials = []

password = input("Enter password: ")

def createKey(userInput):
    password = userInput.encode()
    salt = b'salt'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64decode(kdf.derive(password))

    key = createKey(password)

def decrypt(encrypted):
    """Decrypts with AES"""
    f = Fernet(key)
    try:
        decrypted = f.decrypt(encrypted.encode()).decode()
    except cryptoExceptions.InvalidSignature:
        print("Could't descript. Invalid key.")
        return None
    except fernetException:
        print("Could't descript. Invalid key.")
        return None
    return decrypted

def encrypt(descrypted):
    """Encripts with AES"""
    f = Fernet(key)
    return f.encrypt(descrypted.encode()).decode()

@app.route("/")
def main():
    return "Index page"

@app.route("/status", methods=["POST"])
def send():
    """
    Accept JSON {encrypted: ("username": str, "password": str, "text": str)}
    encrypted value is AES-encrypted json with username, text and password 
    return  {"ok": bool, "code": int, "error": str}
    code - код помилка
    error - пояснення помилки
    """
    decrypted = decrypt(request.get_json()["encrypted"])
    if decrypted is None:
        print("User tried to send message with invalid master key.")
        return {"ok":False, "code": 1, "error": "Master key invalid"}
    data = json.loads(decrypted)
    if not isinstance(data["username"], str) or len(data["username"]) == 0:
        return {"ok":False, "code": 2, "error": "Wrong value supplied for field 'username'"}
    if not isinstance(data["text"], str) or len(data["tetxt"]) == 0:
        return {"ok":False, "code": 3, "error": "Wrong value supplied for field 'text'"}
    if not isinstance(data["password"], str) or len(data["password"]) == 0:
        return {"ok":False, "code": 4, "error": "Wrong value supplied for field 'password'"}
    if data["username"] not in credentials.keys():
        credentials[data["username"]] = data["password"]
    elif credentials[data["username"]] != data["password"]:
        return {"ok": False, "code": 5, "error": f"Wrong password for user (data['user'])"}
    messagesStorage.append({"username": data["username"], "text": data["text"], "time": time.time()})
    return {"ok": True}


@app.route('/messages')
def getMessages():
    
    after = float(request.args['after'])
    #фільтруюьться повідомлення і створюється новий ліст з повідомлень
    # які у лісті меседж, беруться тільки ті повідомлення які задовільняють умову,
    # не дублювати повідомлення
    filtered = [message for message in messagesStorage if message['time'] > after]
    encrypted = encrypt(json.dumps({"messages": filtered}))
    return {'encrypted': encrypted}

app.run()