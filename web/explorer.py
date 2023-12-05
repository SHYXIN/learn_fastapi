from fastapi import APIRouter, HTTPException
from model.explorer import Explorer
# import fake.explorer as service
import service.explorer as service
from typing import Union
from error import Duplication, Missing

router = APIRouter(prefix='/explorer')


@router.get("")
@router.get('/')
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get('/{name}')
def get_one(name) -> Union[Explorer, None]:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


# all the remaining endpoints do nothing yet:
@router.post("", status_code=201)
@router.post('/', status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplication as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.patch('/')
def modify(name:str, explorer: Explorer) -> Explorer:
    try:
        return service.modify(name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)



@router.delete('/{name}')
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
