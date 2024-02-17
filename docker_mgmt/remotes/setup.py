from typing import List, Optional

class Disk:
    dev: str                # sda, sdb, ...
    size: int               # unit: bytes

class Server:
    hostname: str
    ip_address: str
    number_of_cores: int
    cpu_vendor: str
    cpu_model: str
    cpu_clocks: str         # GHz or MHz
    memory_totals: int      # unit: bytes
    disks: Optional[List[Disk]]

def test_connect(ip: str, username=None, password=None) -> Optional[Server]:
    pass


    server = Server()
    server.hostname = "dev"
    server.ip_address = "192.168.36.11"
    # ...

def copy_id(server: Server, username=None, password=None) -> bool:
    pass