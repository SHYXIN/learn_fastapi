from model.explorer import Explorer
import data.explorer as data
from typing import Union


def get_all() -> list[Explorer]:
    return data.get_all()


def get_one(name: str) -> Union[Explorer, None]:
    return data.get_one(name)


def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)


def replace(id, explorer: Explorer) -> Explorer:
    return data.replace(id, explorer)


def modify(id, explorer: Explorer) -> Explorer:
    return data.modify(id, explorer)


def delete(id) -> Explorer:
    return data.delete(id)
