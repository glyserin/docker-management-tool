from fabric import Connection
from getpass import getpass

print("Password: ")
password = getpass()

connection = Connection("172.17.0.4", user="root", connect_kwargs= {
	"key_filename": "/home/vscode/.ssh/id_rsa"
})

with open("/home/vscode/.ssh/id_rsa") as file:
	key = file.read()

result = connection.run(f'echo "{key}" | tee -a ~/.ssh/authorized_keys')

print(result)

connection.close()