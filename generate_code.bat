@REM install current vresion of the module
.tox\python3.9\Scripts\python.exe -m pip install .

@REM Generate code with graph of relations between tables
.tox\python3.9\Scripts\python.exe generators/code_gen_graph.py

@REM Generate code with wrapper classes for db tables
.tox\python3.9\Scripts\python.exe generators/code_gen_wrappers.py
