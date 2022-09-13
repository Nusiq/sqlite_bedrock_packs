from sqlite_bedrock_packs.db_main import create_db
from sqlite_bedrock_packs.db_main import load_rp
import sqlite3
from sqlite3 import Connection
from pathlib import Path
import json

def test_rp_database_creation():
    '''
    This test isn't really a test that could detect any bugs on its own. It
    demonstrates how to create a database file from a resource pack.
    '''
    secret_data_path = Path("tests/data/secret/rp_path.txt")
    db_path = Path("tests/data/secret/out.db")
    if not secret_data_path.exists():
        raise Exception(
            "Please configure your local 'tests/data/secret/rp_path.txt' file."
            "The file should contain a path to Minecraft Resource Pack used "
            "for testing.")
    rp_paths = []
    with secret_data_path.open("r") as f:
        for rp_path in f.readlines():
            rp_paths.append(Path(rp_path.strip("\n")))

    print(
        f'The SQLite database file will be created at:\n'
        f'\t{db_path.as_posix()}')

    db_path.unlink(missing_ok=True)
    db = create_db(db_path)
    for rp_path in rp_paths:
        load_rp(db, rp_path)
    db.commit()
