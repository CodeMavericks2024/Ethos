from nacl.public import PrivateKey, Box

def encrypt_message(sender_private_key, receiver_public_key, message):
    box = Box(sender_private_key, receiver_public_key)
    return box.encrypt(message)

def decrypt_message(receiver_private_key, sender_public_key, encrypted_message):
    box = Box(receiver_private_key, sender_public_key)
    return box.decrypt(encrypted_message)

