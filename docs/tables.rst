List of tables
==============

Currently, SQLite Bedrock Packs package does't support some of the types of objects that you can find in Minecraft resourece packs and behavior packs. The following tables are the ones that are currently supported.

Attachable
----------

.. code-block:: sql

    CREATE TABLE Attachable (
        Attachable_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        AttachableFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
    
        FOREIGN KEY (AttachableFile_fk) REFERENCES AttachableFile (AttachableFile_pk)
            ON DELETE CASCADE
    )

AttachableAnimationControllerField
----------------------------------

.. code-block:: sql

    CREATE TABLE AttachableAnimationControllerField (
        AttachableAnimationControllerField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Attachable_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (Attachable_fk) REFERENCES Attachable (Attachable_pk)
            ON DELETE CASCADE
    )

AttachableAnimationField
------------------------

.. code-block:: sql

    CREATE TABLE AttachableAnimationField (
        AttachableAnimationField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Attachable_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (Attachable_fk) REFERENCES Attachable (Attachable_pk)
            ON DELETE CASCADE
    )

AttachableFile
--------------

.. code-block:: sql

    CREATE TABLE AttachableFile (
        AttachableFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

AttachableGeometryField
-----------------------

.. code-block:: sql

    CREATE TABLE AttachableGeometryField (
        AttachableGeometryField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Attachable_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (Attachable_fk) REFERENCES Attachable (Attachable_pk)
            ON DELETE CASCADE
    )

AttachableItemField
-------------------

.. code-block:: sql

    CREATE TABLE AttachableItemField (
        AttachableItemField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Attachable_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        condition TEXT,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (Attachable_fk) REFERENCES Attachable (Attachable_pk)
            ON DELETE CASCADE
    )

AttachableMaterialField
-----------------------

.. code-block:: sql

    CREATE TABLE AttachableMaterialField (
        AttachableMaterialField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Attachable_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (Attachable_fk) REFERENCES Attachable (Attachable_pk)
            ON DELETE CASCADE
    )

AttachableRenderControllerField
-------------------------------

.. code-block:: sql

    CREATE TABLE AttachableRenderControllerField (
        AttachableRenderControllerField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Attachable_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        condition TEXT,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (Attachable_fk) REFERENCES Attachable (Attachable_pk)
            ON DELETE CASCADE
    )

AttachableTextureField
----------------------

.. code-block:: sql

    CREATE TABLE AttachableTextureField (
        AttachableTextureField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Attachable_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (Attachable_fk) REFERENCES Attachable (Attachable_pk)
            ON DELETE CASCADE
    )

BehaviorPack
------------

.. code-block:: sql

    CREATE TABLE BehaviorPack (
        BehaviorPack_pk INTEGER PRIMARY KEY AUTOINCREMENT,
    
        path Path NOT NULL
    )

BpAnimation
-----------

.. code-block:: sql

    CREATE TABLE BpAnimation (
        BpAnimation_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        BpAnimationFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
        
        FOREIGN KEY (BpAnimationFile_fk) REFERENCES BpAnimationFile (BpAnimationFile_pk)
            ON DELETE CASCADE
    )

BpAnimationController
---------------------

.. code-block:: sql

    CREATE TABLE BpAnimationController (
        BpAnimationController_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        BpAnimationControllerFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
        
        FOREIGN KEY (BpAnimationControllerFile_fk) REFERENCES BpAnimationControllerFile (BpAnimationControllerFile_pk)
            ON DELETE CASCADE
    )

BpAnimationControllerFile
-------------------------

.. code-block:: sql

    CREATE TABLE BpAnimationControllerFile (
        BpAnimationControllerFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        BehaviorPack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (BehaviorPack_fk) REFERENCES BehaviorPack (BehaviorPack_pk)
            ON DELETE CASCADE
    )

BpAnimationFile
---------------

.. code-block:: sql

    CREATE TABLE BpAnimationFile (
        BpAnimationFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        BehaviorPack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (BehaviorPack_fk) REFERENCES BehaviorPack (BehaviorPack_pk)
            ON DELETE CASCADE
    )

BpItem
------

.. code-block:: sql

    CREATE TABLE BpItem (
        BpItem_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        BpItemFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        -- The version of the parser. The value is based on fromat_version property
        -- of the file or matching schema (when format_version is missing).
        -- It divides the items into two groups 1.10 and 1.16.100. Most of the
        -- format_versions in Minecraft don't change the format so you need only
        -- two parsers to handle all the items.
        parserVersion TEXT NOT NULL,
        -- The texture of the item. It only exists in 1.16.100+ items.
        texture TEXT,
        
        FOREIGN KEY (BpItemFile_fk) REFERENCES BpItemFile (BpItemFile_pk)
            ON DELETE CASCADE
        -- Constraint emulates enum
        FOREIGN KEY (parserVersion) REFERENCES BpItemParserVersionEnum (value)
    )

BpItemFile
----------

.. code-block:: sql

    CREATE TABLE BpItemFile (
        BpItemFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        BehaviorPack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (BehaviorPack_fk) REFERENCES BehaviorPack (BehaviorPack_pk)
            ON DELETE CASCADE
    )

BpItemParserVersionEnum
-----------------------

.. code-block:: sql

    CREATE TABLE BpItemParserVersionEnum (
        -- Emulates enum type. Stores possible value of BpItem.parserVersion
        --- column.
        value TEXT PRIMARY KEY
    )

ClientEntity
------------

.. code-block:: sql

    CREATE TABLE ClientEntity (
        ClientEntity_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ClientEntityFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        FOREIGN KEY (ClientEntityFile_fk) REFERENCES ClientEntityFile (ClientEntityFile_pk)
            ON DELETE CASCADE
    )

ClientEntityAnimationControllerField
------------------------------------

.. code-block:: sql

    CREATE TABLE ClientEntityAnimationControllerField (
        ClientEntityAnimationControllerField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ClientEntity_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (ClientEntity_fk) REFERENCES ClientEntity (ClientEntity_pk)
            ON DELETE CASCADE
    )

ClientEntityAnimationField
--------------------------

.. code-block:: sql

    CREATE TABLE ClientEntityAnimationField (
        ClientEntityAnimationField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ClientEntity_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (ClientEntity_fk) REFERENCES ClientEntity (ClientEntity_pk)
            ON DELETE CASCADE
    )

ClientEntityFile
----------------

.. code-block:: sql

    CREATE TABLE ClientEntityFile (
        ClientEntityFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

ClientEntityGeometryField
-------------------------

.. code-block:: sql

    CREATE TABLE ClientEntityGeometryField (
        ClientEntityGeometryField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ClientEntity_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
        
        FOREIGN KEY (ClientEntity_fk) REFERENCES ClientEntity (ClientEntity_pk)
            ON DELETE CASCADE
    )

ClientEntityMaterialField
-------------------------

.. code-block:: sql

    CREATE TABLE ClientEntityMaterialField (
        ClientEntityMaterialField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ClientEntity_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (ClientEntity_fk) REFERENCES ClientEntity (ClientEntity_pk)
            ON DELETE CASCADE
    )

ClientEntityRenderControllerField
---------------------------------

.. code-block:: sql

    CREATE TABLE ClientEntityRenderControllerField (
        ClientEntityRenderControllerField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ClientEntity_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        condition TEXT,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (ClientEntity_fk) REFERENCES ClientEntity (ClientEntity_pk)
            ON DELETE CASCADE
    )

ClientEntityTextureField
------------------------

.. code-block:: sql

    CREATE TABLE ClientEntityTextureField (
        ClientEntityTextureField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ClientEntity_fk INTEGER NOT NULL,
    
    
        shortName TEXT NOT NULL,
        -- identifier is the path without the extension
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (ClientEntity_fk) REFERENCES ClientEntity (ClientEntity_pk)
            ON DELETE CASCADE
    )

Entity
------

.. code-block:: sql

    CREATE TABLE Entity (
        Entity_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        EntityFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        FOREIGN KEY (EntityFile_fk) REFERENCES EntityFile (EntityFile_pk)
            ON DELETE CASCADE
    )

EntityFile
----------

.. code-block:: sql

    CREATE TABLE EntityFile (
        EntityFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        BehaviorPack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (BehaviorPack_fk) REFERENCES BehaviorPack (BehaviorPack_pk)
            ON DELETE CASCADE
    )

EntityLootField
---------------

.. code-block:: sql

    CREATE TABLE EntityLootField (
        EntityLootField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Entity_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
        componentType TEXT NOT NULL,
    
        FOREIGN KEY (Entity_fk) REFERENCES Entity (Entity_pk)
            ON DELETE CASCADE
        -- Constraint emulates enum
        FOREIGN KEY (componentType) REFERENCES EntityLootFieldComponentTypeEnum (value)
    )

EntityLootFieldComponentTypeEnum
--------------------------------

.. code-block:: sql

    CREATE TABLE EntityLootFieldComponentTypeEnum (
        -- This table is used to store possible values for the 
        -- EntityLootField.componentType column. Stores the names of the
        -- components that can have a loot table reference (like 
        -- "minecraft:loot" or "minecraft:equipment")
        value TEXT PRIMARY KEY
    )

EntitySpawnEggField
-------------------

.. code-block:: sql

    CREATE TABLE EntitySpawnEggField (
        -- Spawn eggs are added to the database based on entities that use the
        -- is_spawnable property. The name of the spawn egg is based on the entity
        -- identifier.
    
        EntitySpawnEggField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Entity_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
    
        FOREIGN KEY (Entity_fk) REFERENCES Entity (Entity_pk)
            ON DELETE CASCADE
    )

EntityTradeField
----------------

.. code-block:: sql

    CREATE TABLE EntityTradeField (
        EntityTradeField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        Entity_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
        componentType TEXT NOT NULL,
    
        FOREIGN KEY (Entity_fk) REFERENCES Entity (Entity_pk)
            ON DELETE CASCADE
        -- Constraint emulates enum
        FOREIGN KEY (componentType) REFERENCES EntityTradeFieldComponentTypeEnum (value)
    )

EntityTradeFieldComponentTypeEnum
---------------------------------

.. code-block:: sql

    CREATE TABLE EntityTradeFieldComponentTypeEnum (
        -- This table is used to store possible values for the
        -- EntityTradeField.componentType column. Stores the names of the
        -- components that can have a trade table reference (like
        -- "minecraft:economy_trade_table" or "minecraft:trade_table")
        value TEXT PRIMARY KEY
    )

Geometry
--------

.. code-block:: sql

    CREATE TABLE Geometry (
        Geometry_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        GeometryFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        parent TEXT,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (GeometryFile_fk) REFERENCES GeometryFile (GeometryFile_pk)
            ON DELETE CASCADE
    )

GeometryFile
------------

.. code-block:: sql

    CREATE TABLE GeometryFile (
        GeometryFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

LootTable
---------

.. code-block:: sql

    CREATE TABLE LootTable (
        LootTable_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        LootTableFile_fk INTEGER NOT NULL,
    
        -- Identifier of the loot table (path to the file relative to the behavior
        -- pack root). Unike some other path based identifiers, this one includes
        -- the file extension.
        identifier TEXT NOT NULL,
    
        FOREIGN KEY (LootTableFile_fk) REFERENCES LootTableFile (LootTableFile_pk)
            ON DELETE CASCADE
    )

LootTableFile
-------------

.. code-block:: sql

    CREATE TABLE LootTableFile (
        LootTableFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        BehaviorPack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (BehaviorPack_fk) REFERENCES BehaviorPack (BehaviorPack_pk)
            ON DELETE CASCADE
    )

LootTableItemField
------------------

.. code-block:: sql

    CREATE TABLE LootTableItemField (
        -- A reference to an item inside a loot table.
    
        LootTableItemField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        LootTable_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (LootTable_fk) REFERENCES LootTable (LootTable_pk)
            ON DELETE CASCADE
    )

LootTableItemSpawnEggReferenceField
-----------------------------------

.. code-block:: sql

    CREATE TABLE LootTableItemSpawnEggReferenceField (
        -- A reference to a spawn egg inside an item inside a loot table.
    
        LootTableItemSpawnEggReferenceField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        LootTableItemField_fk INTEGER NOT NULL,
    
        entityIdentifier TEXT NOT NULL,
        spawnEggIdentifier TEXT NOT NULL,
        connectionType TEXT NOT NULL,
    
        -- If connectionType is direct, it points at the identifier
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (LootTableItemField_fk) REFERENCES LootTableItemField (LootTableItemField_pk)
            ON DELETE CASCADE
        -- Constraint emulates enum
        FOREIGN KEY (connectionType) REFERENCES
            LootTableItemSpawnEggReferenceFieldConnectinTypeEnum (value)
    )

LootTableItemSpawnEggReferenceFieldConnectinTypeEnum
----------------------------------------------------

.. code-block:: sql

    CREATE TABLE LootTableItemSpawnEggReferenceFieldConnectinTypeEnum (
        -- This table is used to store possible values for the
        -- LootTableItemSpawnEggReferenceField.connectionType column.
        -- Stores the type of connection, it can be either "direct" or
        -- "set_actor_id_function".
        value TEXT PRIMARY KEY
    )

LootTableLootTableField
-----------------------

.. code-block:: sql

    CREATE TABLE LootTableLootTableField (
        -- A reference to an loot table inside another loot table.
    
        LootTableLootTableField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        LootTable_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (LootTable_fk) REFERENCES LootTable (LootTable_pk)
            ON DELETE CASCADE
    )

Particle
--------

.. code-block:: sql

    CREATE TABLE Particle (
        Particle_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ParticleFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        material TEXT,
        texture TEXT,
        FOREIGN KEY (ParticleFile_fk) REFERENCES ParticleFile (ParticleFile_pk)
            ON DELETE CASCADE
    )

ParticleFile
------------

.. code-block:: sql

    CREATE TABLE ParticleFile (
        ParticleFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

RenderController
----------------

.. code-block:: sql

    CREATE TABLE RenderController (
        RenderController_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RenderControllerFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (RenderControllerFile_fk) REFERENCES RenderControllerFile (RenderControllerFile_pk)
            ON DELETE CASCADE
    )

RenderControllerFile
--------------------

.. code-block:: sql

    CREATE TABLE RenderControllerFile (
        RenderControllerFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

RenderControllerGeometryField
-----------------------------

.. code-block:: sql

    CREATE TABLE RenderControllerGeometryField (
        RenderControllerGeometryField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RenderController_fk INTEGER NOT NULL,
    
        ownerArray TEXT,
        inOwnerArrayJsonPath TEXT, -- Path to the item in the owner array
        shortName TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (RenderController_fk) REFERENCES RenderController (RenderController_pk)
            ON DELETE CASCADE
    )

RenderControllerMaterialsField
------------------------------

.. code-block:: sql

    CREATE TABLE RenderControllerMaterialsField (
        RenderControllerMaterialsField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RenderController_fk INTEGER NOT NULL,
    
        ownerArray TEXT,
        inOwnerArrayJsonPath TEXT, -- Path to the item in the owner array
        shortName TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        -- The star pattern that matches the bone name
        boneNamePattern TEXT,
        FOREIGN KEY (RenderController_fk) REFERENCES RenderController (RenderController_pk)
            ON DELETE CASCADE
    )

RenderControllerTexturesField
-----------------------------

.. code-block:: sql

    CREATE TABLE RenderControllerTexturesField (
        RenderControllerTexturesField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RenderController_fk INTEGER NOT NULL,
    
        ownerArray TEXT,
        inOwnerArrayJsonPath TEXT, -- Path to the item in the owner array
        shortName TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (RenderController_fk) REFERENCES RenderController (RenderController_pk)
            ON DELETE CASCADE
    )

ResourcePack
------------

.. code-block:: sql

    CREATE TABLE ResourcePack (
        ResourcePack_pk INTEGER PRIMARY KEY AUTOINCREMENT,
    
        path Path NOT NULL
    )

RpAnimation
-----------

.. code-block:: sql

    CREATE TABLE RpAnimation (
        RpAnimation_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RpAnimationFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
        
        FOREIGN KEY (RpAnimationFile_fk) REFERENCES RpAnimationFile (RpAnimationFile_pk)
            ON DELETE CASCADE
    )

RpAnimationController
---------------------

.. code-block:: sql

    CREATE TABLE RpAnimationController (
        RpAnimationController_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RpAnimationControllerFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
        
        FOREIGN KEY (RpAnimationControllerFile_fk) REFERENCES RpAnimationControllerFile (RpAnimationControllerFile_pk)
            ON DELETE CASCADE
    )

RpAnimationControllerFile
-------------------------

.. code-block:: sql

    CREATE TABLE RpAnimationControllerFile (
        RpAnimationControllerFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

RpAnimationControllerParticleEffect
-----------------------------------

.. code-block:: sql

    CREATE TABLE RpAnimationControllerParticleEffect (
        RpAnimationControllerParticleEffect_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RpAnimationController_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (RpAnimationController_fk) REFERENCES RpAnimationController (RpAnimationController_pk)
            ON DELETE CASCADE
    )

RpAnimationControllerSoundEffect
--------------------------------

.. code-block:: sql

    CREATE TABLE RpAnimationControllerSoundEffect (
        RpAnimationControllerSoundEffect_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RpAnimationController_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (RpAnimationController_fk) REFERENCES RpAnimationController (RpAnimationController_pk)
            ON DELETE CASCADE
    )

RpAnimationFile
---------------

.. code-block:: sql

    CREATE TABLE RpAnimationFile (
        RpAnimationFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

RpAnimationParticleEffect
-------------------------

.. code-block:: sql

    CREATE TABLE RpAnimationParticleEffect (
        RpAnimationParticleEffect_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RpAnimation_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (RpAnimation_fk) REFERENCES RpAnimation (RpAnimation_pk)
            ON DELETE CASCADE
    )

RpAnimationSoundEffect
----------------------

.. code-block:: sql

    CREATE TABLE RpAnimationSoundEffect (
        RpAnimationSoundEffect_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RpAnimation_fk INTEGER NOT NULL,
    
        shortName TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (RpAnimation_fk) REFERENCES RpAnimation (RpAnimation_pk)
            ON DELETE CASCADE
    )

RpItem
------

.. code-block:: sql

    CREATE TABLE RpItem (
        RpItem_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        RpItemFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        icon TEXT,
        
        FOREIGN KEY (RpItemFile_fk) REFERENCES RpItemFile (RpItemFile_pk)
            ON DELETE CASCADE
    )

RpItemFile
----------

.. code-block:: sql

    CREATE TABLE RpItemFile (
        RpItemFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

SoundDefinition
---------------

.. code-block:: sql

    CREATE TABLE SoundDefinition (
        SoundDefinition_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        SoundDefinitionsFile_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (SoundDefinitionsFile_fk) REFERENCES SoundDefinitionsFile (SoundDefinitionsFile_pk)
            ON DELETE CASCADE
    )

SoundDefinitionSoundField
-------------------------

.. code-block:: sql

    CREATE TABLE SoundDefinitionSoundField (
        SoundDefinitionSoundField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        SoundDefinition_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (SoundDefinition_fk) REFERENCES SoundDefinition (SoundDefinition_pk)
            ON DELETE CASCADE
    )

SoundDefinitionsFile
--------------------

.. code-block:: sql

    CREATE TABLE SoundDefinitionsFile (
        SoundDefinitionsFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

SoundFile
---------

.. code-block:: sql

    CREATE TABLE SoundFile (
        SoundFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        -- The identifier is the path without extension. This is added to the DB to
        -- make searches easier.
        identifier TEXT NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

TextureFile
-----------

.. code-block:: sql

    CREATE TABLE TextureFile (
        TextureFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ResourcePack_fk INTEGER,
    
        path Path NOT NULL,
        -- The identifier is the path without extension. This is added to the DB to
        -- make searches easier.
        identifier TEXT NOT NULL,
        FOREIGN KEY (ResourcePack_fk) REFERENCES ResourcePack (ResourcePack_pk)
            ON DELETE CASCADE
    )

TradeTable
----------

.. code-block:: sql

    CREATE TABLE TradeTable (
        TradeTable_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        TradeTableFile_fk INTEGER NOT NULL,
    
        -- Identifier of the trade table (path to the file relative to the behavior
        -- pack root). Unike some other path based identifiers, this one includes
        -- the file extension.
        identifier TEXT NOT NULL,
    
        FOREIGN KEY (TradeTableFile_fk) REFERENCES TradeTableFile (TradeTableFile_pk)
            ON DELETE CASCADE
    )

TradeTableFile
--------------

.. code-block:: sql

    CREATE TABLE TradeTableFile (
        TradeTableFile_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        BehaviorPack_fk INTEGER,
    
        path Path NOT NULL,
        FOREIGN KEY (BehaviorPack_fk) REFERENCES BehaviorPack (BehaviorPack_pk)
            ON DELETE CASCADE
    )

TradeTableItemField
-------------------

.. code-block:: sql

    CREATE TABLE TradeTableItemField (
        -- A reference to an item inside a trade table.
    
        TradeTableItemField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        TradeTable_fk INTEGER NOT NULL,
    
        identifier TEXT NOT NULL,
        dataValue INTEGER,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (TradeTable_fk) REFERENCES TradeTable (TradeTable_pk)
            ON DELETE CASCADE
    )

TradeTableItemSpawnEggReferenceField
------------------------------------

.. code-block:: sql

    CREATE TABLE TradeTableItemSpawnEggReferenceField (
        -- A reference to a spawn egg inside an item inside a trade table.
    
        TradeTableItemSpawnEggReferenceField_pk INTEGER PRIMARY KEY AUTOINCREMENT,
        TradeTableItemField_fk INTEGER NOT NULL,
    
        entityIdentifier TEXT NOT NULL,
        spawnEggIdentifier TEXT NOT NULL,
        jsonPath TEXT NOT NULL,
    
        FOREIGN KEY (TradeTableItemField_fk) REFERENCES TradeTableItemField (TradeTableItemField_pk)
            ON DELETE CASCADE
    )

