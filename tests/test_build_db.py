from sqlite_bedrock_packs.db_main import create_db, load_rp, load_bp
from sqlite_bedrock_packs.better_json_tools import load_jsonc
from pathlib import Path

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
    db = create_db(db_path)
    for rp_path in rp_paths:
        load_rp(db, rp_path)
    for bp_path in bp_paths:
        load_bp(db, bp_path)
    db.commit()
