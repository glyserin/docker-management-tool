import os

output = os.popen("cat /etc/os-release").read()

print("-" * 80)
print(output)