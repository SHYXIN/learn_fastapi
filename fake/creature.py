from model.creature import Creature
from typing import Union

# fake data, untill we use a real database and SQL
_creatures = [
    Creature(name='Yeti',
             aka='Abominable Snowman',
             country='CN',
             area='Himalayas',
             description='Hirsute Himalayan'),
    Creature(name='Bigfoot',
             description="Yeti's Cousin Eddie",
             country='US',
             area='*',
             aka='Sasquatch')
]


def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures


def get_one(name: str) -> Union[Creature, None]:
    """Return one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


# The following are nonfunctional for now
# so the just act like they work, without modifying
# the actual fake _creatures list:
def create(creature: Creature) -> Creature:
    """Add an creature"""
    return creature


def modify(creature: Creature) -> Creature:
    """Partically modify an creature"""
    return creature


def replace(creature: Creature) -> Creature:
    """Completely replace an creature"""
    return creature


def delete(name: str) -> bool:
    """Delete an creature; return None if exists"""
    return None
