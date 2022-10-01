'''
This script generates a list of tables in the database created by
sqlite_bedrock_packs. It's triggered by tox. It's not generating files
automatically with Sphinx.
'''
from __future__ import annotations
from pathlib import Path
from sqlite_bedrock_packs import create_db

OUTPUT_PATH = Path("docs/tables.rst")

def main():
    db = create_db()
    cursor = db.execute(
        '''
        SELECT
            tbl_name, sql
        FROM
            sqlite_master
        WHERE
            type='table' AND
            tbl_name != 'sqlite_sequence'
        ORDER BY
            tbl_name;
        '''
    )
    query_results = cursor.fetchall()
    with OUTPUT_PATH.open('w', encoding="utf8") as f:
        f.write(
            'List of tables\n'
            '==============\n\n'
            "Currently, SQLite Bedrock Packs package does't support some of "
            "the types of objects that you can find in Minecraft resourece "
            "packs and behavior packs. The following tables are the ones "
            "that are currently supported.\n\n"
        )
        # for name, sql in query_results:
        #     f.write(f"- {name}\n")
        # f.write("\n")
        for name, sql in query_results:
            f.write(name + "\n")
            f.write("-"*len(name) + "\n\n")
            f.write(".. code-block:: sql\n\n")
            f.write("    " + sql.replace("\n", "\n    ") + "\n\n")

if __name__ == "__main__":
    main()


