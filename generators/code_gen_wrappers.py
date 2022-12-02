'''
This script generates the Python wrappers around the database tables.
'''
from __future__ import annotations
from sqlite3 import Connection
from pathlib import Path
from typing import Iterator, NamedTuple
from sqlite_bedrock_packs import Database

OUTPUT = Path("src/sqlite_bedrock_packs/wrappers.py")

# The header of the generated file
HEADER = '''"""
THIS FILE IS GENERATED. DO NOT EDIT IT MANUALLY.
"""
from __future__ import annotations
from functools import cache
from sqlite3 import Connection
from pathlib import Path
from typing import Union

'''



def tables(db: Connection) -> Iterator[str]:
    '''
    Yields the names of the tables from the database
    '''
    q_result = db.execute(
        '''
        SELECT
            name
        FROM
            sqlite_master
        WHERE
            type ='table' AND
            name NOT LIKE 'sqlite_%';
        '''
    )
    for table_name, in q_result:
        yield table_name


class FieldProperties(NamedTuple):
    name: str
    type_: str
    is_not_null: bool
    is_pk: bool


def table_fields(db: Connection, table_name: str) -> Iterator[FieldProperties]:
    '''
    Yields the names of the fields in a table
    '''
    q_result = db.execute(
        '''
        SELECT name, `type`, `notnull`, pk
        FROM pragma_table_info(?)
        ORDER BY name
        ''',
        (table_name,)
    )
    for field in q_result:
        yield FieldProperties(
            name=field[0],
            type_=field[1],
            is_not_null=bool(field[2]),
            is_pk=bool(field[3]),
        )




def build_class(table_name: str, fields: Iterator[FieldProperties]) -> str:
    """
    Builds the class definition for a table

    Example output:
    class Entity:
        def __init__(self, db: Connection, id: int):
            self.db: Connection = db
            self.Entity_pk: int = id

        @cache
        def query_result(self):
            return self.db.execute(
                '''
                SELECT EntityFile_fk, identifier
                FROM Entity
                WHERE Entity_pk = ?
                ''',
                (self.id,)
            ).fetchone()

        @property
        def EntityFile_fk(self):
            return self.query_result()[0]

        @property
        def identifier(self):
            return self.query_result()[1]
    """
    class_def: list[str] = [
        f"class {table_name}:\n"
        f"    def __init__(self, db: Connection, id: int):\n"
        f"        self.db: Connection = db"
    ]
    # Find the primary key
    pk_field = None
    other_fields: list[FieldProperties] = []
    for field in fields:
        if field.is_pk:
            if pk_field is not None:
                raise ValueError(
                    f"Table {table_name} has multiple primary keys")
            pk_field = field
        else:
            other_fields.append(field)
    if pk_field is None:
        raise ValueError(f"Table {table_name} has no primary key")
    # Add the primary key field line
    class_def.append(f"        self.{pk_field.name}: int = id\n")
    # Add the query_result function
    class_def.append(
        f"    @cache\n"
        f"    def query_result(self):\n"
        f"        return self.db.execute(\n"
        f"            '''\n"
        f"            SELECT {', '.join(field.name for field in other_fields)}\n"
        f"            FROM {table_name}\n"
        f"            WHERE {pk_field.name} = ?\n"
        f"            ''',\n"
        f"            (self.{pk_field.name},)\n"
        f"        ).fetchone()\n"
    )
    # Add the properties
    for i, field in enumerate(other_fields):
        type_ = sql_to_python_type(field.type_, field.is_not_null)
        class_def.append(
            f"    @property\n"
            f"    def {field.name}(self) -> {type_}:\n"
            f"        return self.query_result()[{i}]\n"
        )
    return '\n'.join(class_def)

def sql_to_python_type(type_: str, optional: bool) -> str:
    '''
    Translates a SQLite type to a Python type name
    '''
    if type_ == 'TEXT':
        return 'str' if optional else 'Union[str, None]'
    if type_ == 'INTEGER':
        return 'int' if optional else 'Union[int, None]'
    if type_ == 'Path':
        return 'Path' if optional else 'Union[Path, None]'
    raise ValueError(f"Unknown type {type_}")

def get_wrapper_classes_var(db) -> str:
    '''
    Returns a string representing the contents of the WRAPPER_CLASSES variable
    '''
    result: list[str] = ['WRAPPER_CLASSES = {']
    for table_name in tables(db):
        result.append(f"    '{table_name}': {table_name},")
    result.append('}')
    return '\n'.join(result)

def main():
    db = Database.create().connection
    with open(OUTPUT, 'w') as f:
        f.write(HEADER)
        for table_name in tables(db):
            f.write(build_class(table_name, table_fields(db, table_name)))
            f.write("\n\n")
        f.write("# Map strings to class names for easy access\n")
        f.write(get_wrapper_classes_var(db))

if __name__ == "__main__":
    main()

