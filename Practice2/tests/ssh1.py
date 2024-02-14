import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect("172.17.0.4", key_filename="/home/vscode/.ssh/id_rsa")
stdin, stdout, stderr = client.exec_command("cat /etc/os-release")

print("".join(stdout.readlines()))

client.close()