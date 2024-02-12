import subprocess

proc = subprocess.Popen(["cat", "/etc/os-release"], stdout=subprocess.PIPE)

(out, err) = proc.communicate()

print("-" * 80)
print(out.decode())  # unicode decoding