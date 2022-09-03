-- SQLite
-- Query that finds the data useful for rendering entities.
SELECT
    ClientEntity_pk AS 'Rpe ID',
    RenderController_pk AS 'Rc ID',
    Geometry_pk AS 'Geo ID',
    TextureFile_pk AS 'Texture ID',
    ClientEntity.identifier AS 'Rpe Identifier',
    -- ClientEntityFile.path AS 'Rpe Path',
    RenderController.identifier AS 'Rc Identifier',
    -- RenderControllerFile.path AS 'Rc Path',
    Geometry.identifier AS 'Geometry Identifier',
    -- GeometryFile.path AS 'Geometry Path',
    TextureFile.identifier AS 'Texture Identifier',
    -- TextureFile.path AS 'Texture Path',
    ClientEntityMaterialField.identifier AS 'Material',
    RenderControllerMaterialsField.boneNamePattern AS 'Material Pattern'
-- Rpe tables
FROM ClientEntity
JOIN
    ClientEntityGeometryField
    ON ClientEntityGeometryField.ClientEntity_fk = ClientEntity_pk
JOIN
    ClientEntityMaterialField
    ON ClientEntityMaterialField.ClientEntity_fk = ClientEntity_pk
JOIN
    ClientEntityTextureField
    ON ClientEntityTextureField.ClientEntity_fk = ClientEntity_pk
JOIN
    ClientEntityFile
    ON ClientEntity.ClientEntityFile_fk = ClientEntityFile_pk
JOIN
    ClientEntityRenderControllerField
    ON ClientEntityRenderControllerField.ClientEntity_fk = ClientEntity_pk
-- Geometry and Geometry File
JOIN
    Geometry
    ON ClientEntityGeometryField.identifier = Geometry.identifier
JOIN
    GeometryFile
    ON Geometry.GeometryFile_fk = GeometryFile_pk
-- Texture File
JOIN
    TextureFile
    ON ClientEntityTextureField.identifier = TextureFile.identifier
-- RC tables (render controller is optional)
LEFT OUTER JOIN
    RenderController
    ON RenderController.identifier = ClientEntityRenderControllerField.identifier
LEFT OUTER JOIN
    RenderControllerGeometryField
    ON RenderControllerGeometryField.RenderController_fk = RenderController_pk
LEFT OUTER JOIN
    RenderControllerMaterialsField
    ON RenderControllerMaterialsField.RenderController_fk = RenderController_pk
LEFT OUTER JOIN
    RenderControllerTexturesField
    ON RenderControllerTexturesField.RenderController_fk = RenderController_pk
LEFT OUTER JOIN
    RenderControllerFile
    ON RenderController.RenderControllerFile_fk = RenderControllerFile_pk
WHERE
    (
        RenderController_pk IS NULL
        OR (
            ClientEntityGeometryField.shortName = RenderControllerGeometryField.shortName AND
            ClientEntityMaterialField.shortName = RenderControllerMaterialsField.shortName AND
            ClientEntityTextureField.shortName = RenderControllerTexturesField.shortName
        )
    )
    -- AND 
    -- ClientEntity.identifier = 'shapescape:pigeon'
ORDER BY
    'Rpe Identifier';