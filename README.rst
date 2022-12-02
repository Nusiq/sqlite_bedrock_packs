.. image:: https://readthedocs.org/projects/sqlite-bedrock-packs/badge/?version=latest
    :target: https://sqlite-bedrock-packs.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

SQLite bedrock packs
====================
Python package that loads data from Minecraft: Bedrock Edition packs into
SQLite database.

Documentation
-------------

If you're looking for documentation please visit:

https://sqlite-bedrock-packs.readthedocs.io/en/stable/

Installation
------------

.. code-block:: bash

   pip install sqlite-bedrock-packs

Changelog
=========

2.1.1
-----

Changed the minimal supported version of Python from 3.10 to 3.9

2.1.0
-----

Added new tables for storing the information about relations of entity spawn eggs
and their presence in loot tables and the trade tables:

- LootTableItemSpawnEggReferenceField
- TradeTableItemSpawnEggReferenceField
- EntitySpawnEggField

2.0.0
-----

Restructured the project to be more object oriented, added EasyQuery object.


1.2.0
-----

- Added new tables:
    - BpAnimation
    - BpAnimationController
    - BpAnimationControllerFile
    - BpAnimationFile
    - BpItem
    - BpItemFile
    - BpItemParserVersionEnum
    - EntityLootField
    - EntityLootFieldComponentTypeEnum
    - EntityTradeField
    - EntityTradeFieldComponentTypeEnum
    - LootTable
    - LootTableFile
    - LootTableItemField
    - LootTableLootTableField
    - RpItem
    - RpItemFile
    - TradeTable
    - TradeTableFile
    - TradeTableItemField

- Added new fields to the entity
    - LootTable
    - TradeTable

1.1.1
-----

Fixed crashes caused by missing client_entity identifier.

1.1.0
-----

- Added new tables:
    - BehaviorPack
    - Entity
    - EntityFile
    - SoundDefinition
    - SoundDefinitionSoundField
    - SoundDefinitionsFile
    - SoundFile

- Added type annotations and py.typed file.
- renamed better_json module to better_json_tools

1.0.2
-----

- Supported objects:
    - Attachable
    - AttachableAnimationControllerField
    - AttachableAnimationField
    - AttachableFile
    - AttachableGeometryField
    - AttachableItemField
    - AttachableMaterialField
    - AttachableRenderControllerField
    - AttachableTextureField
    - ClientEntity
    - ClientEntityAnimationControllerField
    - ClientEntityAnimationField
    - ClientEntityFile
    - ClientEntityGeometryField
    - ClientEntityMaterialField
    - ClientEntityRenderControllerField
    - ClientEntityTextureField
    - Geometry
    - GeometryFile
    - Particle
    - ParticleFile
    - RenderController
    - RenderControllerFile
    - RenderControllerGeometryField
    - RenderControllerMaterialsField
    - RenderControllerTexturesField
    - ResourcePack
    - RpAnimation
    - RpAnimationController
    - RpAnimationControllerFile
    - RpAnimationControllerParticleEffect
    - RpAnimationControllerSoundEffect
    - RpAnimationFile
    - RpAnimationParticleEffect
    - RpAnimationSoundEffect
    - TextureFile

Older releases
--------------
No changelog for releases before PyPI

