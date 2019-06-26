import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = sys.argv[1]
target = str(target)
def scan(a):
	try:
		c = s.connect((target,a))
		return True
	except:
		return False

for i in range(6666):
	if scan(i):
		print("PORT OPEN: ", i)

