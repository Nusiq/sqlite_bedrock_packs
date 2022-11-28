'''
This script generates the graph with relations between tables in the database.
'''
from __future__ import annotations
from sqlite3 import Connection
from pathlib import Path
from typing import NamedTuple
from sqlite_bedrock_packs import Database

OUTPUT = Path("src/sqlite_bedrock_packs/graph.py")

# The header of the generated file
HEADER = '''"""
THIS FILE IS GENERATED. DO NOT EDIT IT MANUALLY.
"""
from __future__ import annotations
from typing import NamedTuple

class _TableConnection(NamedTuple):
    columns: tuple[str, str]
    is_pk: bool

'''
class _TableConnection(NamedTuple):
    columns: tuple[str, str]
    is_pk: bool

NON_PK_RELATIONS: dict[str, dict[str, _TableConnection]] = {
    "ClientEntity": {
        "Entity": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "ClientEntityRenderControllerField": {
        "RenderController": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "ClientEntityGeometryField": {
        "Geometry": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "ClientEntityTextureField": {
        "TextureFile": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "ClientEntityAnimationField": {
        "RpAnimation": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "ClientEntityAnimationControllerField": {
        "RpAnimationController": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "AttachableItemField": {
        "RpItem": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        ),
        "BpItem": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "AttachableTextureField": {
        "TextureFile": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "AttachableGeometryField": {
        "Geometry": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "AttachableRenderControllerField": {
        "RenderController": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "AttachableAnimationField": {
        "RpAnimation": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "AttachableAnimationControllerField": {
        "RpAnimationController": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "EntityLootField": {
        "LootTable": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "EntityTradeField": {
        "TradeTable": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "LootTableItemField": {
        "RpItem": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        ),
        "BpItem": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "LootTableItemSpawnEggReferenceField": {
        "EntitySpawnEggField": _TableConnection(
            columns=("spawnEggIdentifier", "identifier"),
            is_pk=False,
        )
    },
    "LootTableLootTableField": {
        "LootTable": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "TradeTableItemField": {
        "RpItem": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        ),
        "BpItem": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    },
    "Particle": {
        "TextureFile": _TableConnection(
            columns=("texture", "identifier"),
            is_pk=False
        )
    },
    "SoundDefinitionSoundField": {
        "SoundFile": _TableConnection(
            columns=("identifier", "identifier"),
            is_pk=False
        )
    }
}

def get_all_relations(db: Connection):
    # Add the reverse relations
    reversed_relations = {}
    for left, relations in NON_PK_RELATIONS.items():
        for right, properties in relations.items():
            if right not in reversed_relations:
                reversed_relations[right] = {}
            left_column, right_column = properties.columns
            reversed_relations[right][left] = _TableConnection(
                columns=(right_column, left_column),
                is_pk=False
            )
    result = NON_PK_RELATIONS | reversed_relations
    # Add the primary key relations
    q_result = db.execute(
        '''
        SELECT 
            p.`table` AS parent,
            p.`to` AS parent_column,
            sqlite_master.name AS child,
            p.`from` AS child_column
        FROM
            sqlite_master
        JOIN pragma_foreign_key_list(sqlite_master.name) AS p
            ON sqlite_master.name != p."table"
        WHERE
            sqlite_master.type = 'table'
            AND sqlite_master.name NOT LIKE 'sqlite_%'
        ORDER BY
            sqlite_master.name;
        '''
    )
    for parent, parent_column, child, child_column in q_result:
        if parent not in result:
            result[parent] = {}
        result[parent][child] = _TableConnection(
            columns=(parent_column, child_column),
            is_pk=True
        )
        if child not in result:
            result[child] = {}
        result[child][parent] = _TableConnection(
            columns=(child_column, parent_column),
            is_pk=True
        )
    return result

def pretty_str_relations(relations: dict[str, dict[str, _TableConnection]]) -> str:
    result: list[str] = ["{"]
    for k, v in relations.items():
        result.append(f'    "{k}": {{')
        for k2, v2 in v.items():
            result.append(f'        "{k2}": _TableConnection(')
            result.append(f'            columns=({v2.columns}),')
            result.append(f'            is_pk={v2.is_pk}')
            result.append("        ),")
        result.append("    },")
    result.append("}")
    return "\n".join(result)

def main():
    db = Database.create().connection
    db_relation_map = get_all_relations(db)

    with OUTPUT.open('w', encoding="utf8") as f:
        f.write(HEADER)
        f.write(f"RELATION_MAP = {pretty_str_relations(db_relation_map)}")

if __name__ == "__main__":
    main()

