import paramiko
from getpass import getpass

print("Password: ")
passwd = getpass()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("172.17.0.5", username="root", password=passwd)

client.exec_command('mkdir -p ~/.ssh/')
client.exec_command('chmod 700 ~/.ssh/')

with open("/home/vscode/.ssh/id_rsa.pub") as file:
	key = file.read()

client.exec_command(f'echo "{key}" | tee -a ~/.ssh/authorized_keys')
client.exec_command('chmod 644 ~/.ssh/authorized_keys')

client.close()