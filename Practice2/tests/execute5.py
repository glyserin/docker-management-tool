import subprocess

output = subprocess.check_output(["ssh", "second", "cat", "/etc/os-release"])
print("-" * 80)
print(output.decode())