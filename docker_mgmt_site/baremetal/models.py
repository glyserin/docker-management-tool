from typing import List, Optional
from django.db import models

from docker_mgmt.remotes.setup import Server as _Server
from docker_mgmt.remotes.setup import Disk

class Server(models.Model, _Server):
    hostname = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200, null=True, blank=True)
    number_of_cores = models.IntegerField(default=1)
    cpu_vendor = models.CharField(max_length=200, null=True, blank=True)
    cpu_model = models.CharField(max_length=200, null=True, blank=True)
    cpu_clocks = models.CharField(max_length=200, null=True, blank=True)
    memory_totals = models.IntegerField(null=True, blank=True)
    disk_info = models.JSONField(default=dict())
    roles = models.ManyToManyField("AnsibleRole")

    def __str__(self) -> str:
        if self.hostname:
            return self.hostname
        return self.ip_address
    
    @property
    def disks(self) -> Optional[List[Disk]]:
        disks = []
        for k, v in self.disk_info.items():
            disk = Disk()
            disk.dev = k
            disk.size = v
            disks.append(disk)
        return disks


class AnsibleRole(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=250, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    