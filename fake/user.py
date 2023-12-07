from model.user import User
from error import Missing, Duplication
from typing import Union

# (no hashed password checking in this module)
fakes = [
    User(name="kwijobo", hash="abc"),
    User(name="ermagerd", hash="xyz")
]


def find(name: str) -> Union[User, None]:
    for e in fakes:
        if e.name == name:
            return e
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing user {name}")


def check_duplication(name: str):
    if find(name):
        raise Duplication(msg=f"Duplication user {name}")


def get_all() -> list[User]:
    """Return all users"""
    return fakes


def get_one(name: str) -> User:
    check_missing(name)  # 如果找不到直接就抛出异常了
    return find(name)


def create(user: User) -> User:
    """Add a user"""
    check_duplication(user.name)
    return user


def modify(name: str, user: User) -> User:
    """Partially modify a user"""
    check_missing(name)
    return user


def delete(name: str) -> None:
    """Delete a user"""
    check_missing(name)
    return None
