import os

# os.system("ls")
# os.system("cat /etc/os-release")

V1 = os.system("true")
V2 = os.system("false")
print(f"true -> exit code : {V1}")
print(f"false -> exit code : {V2}")