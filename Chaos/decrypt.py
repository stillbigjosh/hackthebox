import os
from getpass import getpass
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random



def encrypt(key, filename):
	chunksize = 64*1024
	outputfile = 'encrypt.'+ filename
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)
	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputfile, 'wb') as outfile:
			outfile.write(filesize.encode('UTF-8'))
			outfile.write(IV)

			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += b' ' * (16 - (len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))
def decrypt(key, filename):
	chunksize = 64*1024
	outputfile = filename[8:]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputfile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break
				outfile.write(decryptor.decrypt(chunk))

			outfile.truncate(filesize)
def getkey(password):
	hashme = SHA256.new(password.encode('UTF-8'))
	return hashme.digest()


def Main():
	Question = input('Encrypt or Decrypt? E | D: ')
	if Question == 'E':
		filename = input('Please enter filename: ')
		password = getpass()
		encrypt(getkey(password), filename)
		print('Complete!')

	elif Question == 'D':
		filename = input('Please enter filename: ')
		password = getpass()
		decrypt(getkey(password), filename)
		print('Complete!')
	else:
		print('Please enter a valid option...')

if __name__ == '__main__':
	Main()
