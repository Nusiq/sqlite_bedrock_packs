from pathlib import Path
import re
from sqlite_bedrock_packs import (
    Database, Left, EntityFile, RpAnimationControllerFile, build_easy_query)
from sqlite_bedrock_packs.better_json_tools import load_jsonc



PACK_PATHS_STRUCTURE = '''
{
    "rp_paths": [...], // List of paths to resource packs
    "bp_paths": [...]  // List of paths to behavior packs
}
'''

def test_rp_database_creation():
    '''
    This test isn't really a test that could detect any bugs on its own. It
    demonstrates how to create a database file from a resource pack.
    '''
    
    secret_data_path = Path("tests/data/secret/pack_paths.json")
    db_path = Path("tests/data/secret/out.db")
    if not secret_data_path.exists():
        raise Exception(
            f"Please configure your local '{secret_data_path.as_posix()}' "
            "file. The file should contain lists of resource packs and "
            "behavior packs in following format:\n"
            f"{PACK_PATHS_STRUCTURE}")
    packs_data = load_jsonc(secret_data_path)
    rp_paths = (packs_data / "rp_paths").data
    bp_paths = (packs_data / "bp_paths").data
    print(
        f'The SQLite database file will be created in:\n'
        f'\t{db_path.as_posix()}')

    db_path.unlink(missing_ok=True)
    db = Database.create(db_path)
    for rp_path in rp_paths:
        db.load_rp(rp_path)
    for bp_path in bp_paths:
        db.load_bp(bp_path)
    db.commit()


def test_easy_query():
    # db_path = Path("tests/data/secret/out.db")
    # db = open_db(db_path)
    expected_ouput = '''
    SELECT DISTINCT
            EntityFile_pk AS EntityFile,
            RpAnimationControllerFile_pk AS RpAnimationControllerFile
    FROM EntityFile
    JOIN Entity
            ON EntityFile.EntityFile_pk = Entity.EntityFile_fk
    JOIN ClientEntity
            ON Entity.identifier = ClientEntity.identifier
    JOIN ClientEntityAnimationControllerField
            ON ClientEntity.ClientEntity_pk = ClientEntityAnimationControllerField.ClientEntity_fk
    JOIN RpAnimationController
            ON ClientEntityAnimationControllerField.identifier = RpAnimationController.identifier
    LEFT JOIN RpAnimationControllerFile
            ON RpAnimationController.RpAnimationControllerFile_fk = RpAnimationControllerFile.RpAnimationControllerFile_pk
    WHERE
            EntityFile.EntityFile_pk == 1
            AND RpAnimationControllerFile.RpAnimationControllerFile_pk == 1
    '''
    actual_result = build_easy_query(
        EntityFile, Left(RpAnimationControllerFile),
        accept_non_pk=True,
        where=[
            "EntityFile.EntityFile_pk == 1",
            "RpAnimationControllerFile.RpAnimationControllerFile_pk == 1"
        ]
    )

    pattern = re.compile(r'\s+')
    # Assert that expected == actual (ignoring whitespace)
    assert (
        pattern.sub(" ", expected_ouput).strip() ==
        pattern.sub(" ", actual_result).strip()
    )
