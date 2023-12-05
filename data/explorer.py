from typing import Union, Optional
from data import conn, curs, IntegrityError
from model.explorer import Explorer
from error import Missing, Duplication

curs.execute("""create table if not exists explorer(
                name text primary key,
                country text,
                description text)""")


def row_to_model(row: tuple) -> Explorer:
    return Explorer(name=row[0], country=row[1], description=row[2])


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict() if explorer else None


def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f'Explorer {name} not found')


def get_all() -> list[Explorer]:
    qry = "select * from explorer"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(explorer: Explorer) -> Explorer:
    qry = """insert into explorer(name, country, description) 
             values(:name, :country, :description)"""
    params = model_to_dict(explorer)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplication(msg=f"Explorer {explorer.name} already exists")
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Union[Explorer, None]:
    if not (name and explorer):
        return None
    qry = """update explorer
             set country=:country,
                 name=:name,
                 description=:description,
             where name=:name_orig"""
    params = model_to_dict(explorer)
    params['name_orig'] = explorer.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        explorer2 = get_one(explorer.name)
        return explorer2
    else:
        raise Missing(msg=f"Explorer {name} not found")


def delete(name: str) -> bool:
    if not name:
        return False
    qry = "delete from explorer where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Explorer {name} not found")