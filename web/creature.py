import os
from fastapi import APIRouter, HTTPException
from model.creature import Creature
if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as service
else:
    from service import creature as service
from error import Missing, Duplication
from typing import Union

router = APIRouter(prefix='/creature')


@router.get('/')
def get_all() -> list[Creature]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> Union[Creature, None]:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


# all the remaining endpoints do nothing yet:
@router.post('/')
def create(creature: Creature) -> Creature:
    try:
        return service.create(creature)
    except Duplication as exc:
        raise HTTPException(status_code=409, detail=exc.msg)


@router.patch('/')
def modify(creature: Creature) -> Creature:
    try:
        return service.modify(creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.delete('/{name}')
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
