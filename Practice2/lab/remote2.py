import paramiko
from getpass import getpass

print("Password: ")
passwd = getpass()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("172.17.0.5", username="root", password=passwd)

# client.exec_command('mkdir -p ~/.ssh/')

with open("/home/vscode/.ssh/id_rsa") as file:
	key = file.read()

# prepare ssh connection
session = client.invoke_shell(term="xterm")
session.close()

client.exec_command(f'echo "{key}" | tee -a ~/.ssh/authorized_keys')

# client.exec_command('chmod 644 ~/.ssh/authrized_keys')
# client.exec_command('chmod 700 ~/.ssh/')

client.close()