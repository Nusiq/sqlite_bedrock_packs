'''
Moves the `documentation` to gh-pages branch.
'''
import shutil
import os
import subprocess

# Continue only if checkout is successful (return 0)
if subprocess.call('git checkout gh-pages', shell=True) == 0:
    # Remove all files except whitelist
    whitelist = [
        '.git', '.gitignore', '.tox', '.mypy_cache', '.vscode', 'documentation',
        '.nojekyll', 'mv_documentation.py'
    ]
    for p in os.listdir():
        if p not in whitelist:
            if os.path.isfile(p):
                os.remove(p)
            else:
                shutil.rmtree(p)

    # # Copy documentation files
    doc_source = './documentation/'
    for path in os.listdir(doc_source):
        from_ = os.path.join(doc_source, path)
        shutil.move(from_, './')

    # # Create .nojekyll file to let github know that jekyll is not used
    with open('.nojekyll', 'w') as f:
        pass

    print("#### INFO ####")
    print(
        "Copeid files from documentation/. You are now in gh-pages branch. "
        "If you want you can STAGE and COMMIT the changes."
    )
