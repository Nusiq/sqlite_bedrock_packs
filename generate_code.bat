@REM install current vresion of the module
.tox\py310\Scripts\python.exe -m pip install .

@REM Generate code with graph of relations between tables
.tox\py310\Scripts\python.exe generators/code_gen_graph.py

@REM Generate code with wrapper classes for db tables
.tox\py310\Scripts\python.exe generators/code_gen_wrappers.py
