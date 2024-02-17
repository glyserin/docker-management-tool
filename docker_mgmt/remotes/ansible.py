from typing import List, Union
from .setup import Server

def create_inventory(server: Union[List[Server], Server]) -> str:
    pass


def run_playbook(inventory: str, roles:List[str]) -> bool:
    pass