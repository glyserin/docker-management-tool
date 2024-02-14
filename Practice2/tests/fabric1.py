from fabric import Connection

connection = Connection("172.17.0.4", connect_kwargs= {
	"key_filename": "/home/vscode/.ssh/id_rsa"
})

result = connection.run("uname -s")

print("-" * 80)
print(result)