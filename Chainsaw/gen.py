#!/usr/bin/python
from Crypto.PublicKey import RSA
from os import chmod
import getpass

def generate(username,password):
	key = RSA.generate(2048)
	pubkey = key.publickey()

	pub = pubkey.exportKey('OpenSSH')
	priv = key.exportKey('PEM',password,pkcs=1)

	filename = "{}.key".format(username)

	with open(filename, 'w') as file:
		chmod(filename, 0600)
		file.write(priv)
		file.close()

	with open("{}.pub".format(filename), 'w') as file:
		file.write(pub)
		file.close()

	# TODO: Distribute keys via ProtonMail

if __name__ == "__main__":
	while True:
		username = raw_input("User: ")
		password = getpass.getpass()
		generate(username,password)

