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

  from typing import cast
  from sqlite_bedrock_packs import (
    Database, build_easy_query, ClientEntity, Geometry, Left
  )

  # Create a new database
  db = Database.create()

  # Load a resourcepack, to make it faster only include objects that we need
  db.load_rp("packs/RP", include=["client_entities", "geometries"])

  # Create query for listing all entities that have a with a geometry
  query = build_easy_query(db, ClientEntity, Left(Geometry))
  # Generated query automatically finds the connections between the tables,
  # based on a graph of the databse. In this case it is very simple, because
  # listed tables are connected almost directly but things like for example
  # finding all RP animatoins connected to an BP entity are also possible.
  # The Left() function marks the Geometry for a LEFT JOIN in the query.

  print(query.sql_code)
  # SELECT DISTINCT
  #         ClientEntity_pk AS ClientEntity,
  #         Geometry_pk AS Geometry
  # FROM ClientEntity
  # JOIN ClientEntityGeometryField
  #         ON ClientEntity.ClientEntity_pk = ClientEntityGeometryField.ClientEntity_fk
  # LEFT JOIN Geometry
  #         ON ClientEntityGeometryField.identifier = Geometry.identifier



  # Run SQL query and print the results. The wrappers returned by the query
  # take care of converting the primary keys to actual objects. Note that
  # the query returns only the primary keys of the objects listed in the
  # build() method even if there are other tables which were used to join
  # the data and find meaningful connections.
  for ce, geo in yield_from_easy_query(db, ClientEntity, Geometry):
     print(ce.identifier, geo.identifier)



Table of contents
-----------------

.. toctree::
   :maxdepth: 1

   loading_data
   queries
   tables

