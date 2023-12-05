from model.creature import Creature
import data.creature as data
from typing import Union


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name: str) -> Union[Creature, None]:
    return data.get_one(name)


def create(creature: Creature) -> Creature:
    return data.create(creature)


def replace(id, creature: Creature) -> Creature:
    return data.replace(id, creature)


def modify(id, creature: Creature) -> Creature:
    return data.modify(id, creature)


def delete(id, creature: Creature) -> Creature:
    return data.delete(id)
