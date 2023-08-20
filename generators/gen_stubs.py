from __future__ import annotations
import sqlite_bedrock_packs as sqlbp
from pathlib import Path

def main():
    output_dir = Path("src/sqlite_bedrock_packs/views.pyi")

    # The original PY file has a bunch of imports that we want to copy over
    # to the PYI file.
    the_py_file = Path("src/sqlite_bedrock_packs/views.py")

    output: list[str] = the_py_file.read_text().splitlines()
    modules = set()

    for v in sqlbp._views.WRAPPER_CLASSES.values():
        output.append(f"class {v.__name__}(AbstractDBView):")
        class_body: list[str] = []
        for k, v in v.__annotations__.items():
            if v.__module__ == "builtins":
                type_ = f"{v.__qualname__}"
            else:
                type_ = f"{v.__module__}.{v.__qualname__}"
                modules.add(v.__module__)
            class_body.append(f"{k}: {type_}")
        output.extend("    " + line for line in class_body)


    output = [f"import {module}" for module in sorted(modules)] + output
    output_dir.write_text("\n".join(output))
    

if __name__ == "__main__":
    main()
