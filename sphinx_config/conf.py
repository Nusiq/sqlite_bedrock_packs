# Another theme for the page
html_theme = 'sphinx_rtd_theme'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

# The name of the entry point, without the ".rst" extension.
# By convention this will be "index"
master_doc = "index"
add_module_names = False

# This values are all used in the generated documentation.
# Usually, the release and version are the same,
# but sometimes we want to have the release have an "rc" tag.
project = "sqlite-bedrock-packs"
author = "Artur D."