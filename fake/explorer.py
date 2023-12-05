from model.explorer import Explorer
from typing import Union

# fake data, replaced in Chater 10 by a real database and SQL

_explorers = [
    Explorer(name='Claude Hande',
             country='FR',
             description='Scarce during full moon'),
    Explorer(name='Noah Weiser',
             country='DE',
             description='Myopic machete man')
]


def get_all() -> list[Explorer]:
    """Return all explorers"""
    return _explorers


def get_one(name: str) -> Union[Explorer, None]:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


# The following are nonfunctional for now
# so the just act like they work, without modifying
# the actual fake _explorers list:
def create(explorer: Explorer) -> Explorer:
    """Add an explorer"""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Partically modify an explorer"""
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """Completely replace an explorer"""
    return explorer


def delete(name: str) -> bool:
    """Delete an explorer; return None if exists"""
    return None
