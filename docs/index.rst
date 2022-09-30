SQLite Bedrock Packs
====================

SQLite Bedrock Packs is a package that loads data from
*Minecraft: Bedrock Edition* packs into SQLite database. 

Source code: https://github.com/Nusiq/sqlite_bedrock_packs

What it does?
-------------
The main purpose of this package is to make developing tools that validate
resource packs and behavior packs easier. SQLite Bedrock Packs package focuses
on mapping relations between various objects from RPs and BPs (like entities,
animations, textures, spawn rules etc.)

The data loaded into the database includes:

- Identifiers of the detected objects
- References in objects that point to other objects (like list of animations
  in an entity).
- Paths to the files that contain the objects
- JSON paths to the objects in the files

It does not include the actual data from the objects but it should be easy to
access knowing exactly where the object is located, thanks to
`better-json-tools <https://pypi.org/project/better-json-tools/>`_ module which
is included in this package 

  The code of `better-json-tools` is included in `sqlite-bedrock-packs` instead
  of being a dependency because it is a part of the
  `Mcblend <https://github.com/Nusiq/mcblend>`_ Blender add-on. Addons cannot
  have dependencies. This solution lets me develop the code of Mcblend,
  sqlite-bedrock-packs and better-json-tools in parallel while still being able
  to use them as independent packages.

SQLite Bedrock Packs let you use SQL queries to easily find problems in your
project like missing, unused or duplicated objects.

What it does not do?
--------------------
SQLite Bedrock Packs is relatively low level tool. It doesn't provide any
abstractions over the data and it doesn't perform any validation on its own.

Example
-------
The following example shows very basic usage of the package. It loads data from
a resource pack and prints the list of all of the entities in the pack.

.. code-block:: Python

   from sqlite_bedrock_packs import create_db, load_rp

   # Create a new database in memory
   db = create_db()

   # Load a resource pack
   load_rp(
      db, "path/to/resource_pack",
      include=["client_entities"]  # We don't need to load more
   )

   # Run SQL query and print the results. This is just a simple example but
   # the queries can be way more complex.
   for identifier in db.execute("SELECT identifier FROM ClientEntity;"):
      print(identifier[0])



Table of contents
-----------------

.. toctree::
   :maxdepth: 1

   functions
