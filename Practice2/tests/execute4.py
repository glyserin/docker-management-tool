import subprocess

output = subprocess.check_output(["cat", "/etc/os-release"])
print("-" * 80)
print(output.decode())