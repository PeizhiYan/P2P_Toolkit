# AES 256 encryption/decryption using pycryptodome library

from Crypto.Cipher import AES
import hashlib
import binascii, os

class AES256:
	""" The AES-256 Encryption/Decryption Module """
	def __init__(self, password):
		self.salt = "this is salt"
		# generate 256-bit encryption key
		self.secretKey = hashlib.pbkdf2_hmac('sha256', 
											password.encode('UTF-8'), 
											self.salt.encode('UTF-8'),
											100000)  

	def encrypt(self, msg):
		msg = msg.encode('UTF-8') # convert to buffers of bytes
		aesCipher = AES.new(self.secretKey, AES.MODE_GCM)
		ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
		return (ciphertext, aesCipher.nonce, authTag)

	def decrypt(self, encryptedMsg):
		(ciphertext, nonce, authTag) = encryptedMsg
		aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce)
		plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
		return plaintext.decode('UTF-8')





# line 33