import subprocess
import re

output = subprocess.check_output(["hostname"]).decode()
print(f"Hostname {output}")

output = subprocess.check_output(["ip", "addr"]).decode()
inet_addresses = re.findall(r"\sinet\s([\d.]+)/(\d+)", output)
inet_address = inet_addresses[1]
print(f"IP Address {inet_address[0]}/{inet_address[1]}")

output = subprocess.check_output(["cat", "/proc/cpuinfo"]).decode()
cores = 0
cpu_info = {}
for line in output.split("\n"):
    if line.startswith('processor'):
        cores += 1
    if line.strip():
        key, value = map(str.strip, line.split(":", 1))
        cpu_info[key] = value
vendor_id = cpu_info.get('vendor_id')
model_name = cpu_info.get('model name')
print(f"CPU {cores} Cores")
print(f"CPU Vendor {vendor_id}")
print(f"CPU Model {model_name}")

output = subprocess.check_output(["cat", "/proc/meminfo"]).decode()
mem_info = {}
for line in output.split("\n"):
    if line.strip():
        key, value = map(str.strip, line.split(":", 1))
        mem_info[key] = value
mem_total_kb = mem_info.get('MemTotal')
mem_total = int(mem_total_kb.split()[0])
print(f"Memory Total {mem_total}")

output = subprocess.check_output(["lsblk"]).decode()
disk_info = []
for line in output.split("\n"):
    if line.strip() and line.split()[5] == "disk":
        name, _, _, size, _, _ = line.split()
        disk_info.append((name, size))
print("Disk")
for name, size in disk_info:
    print(f"  {name} {size}G")
