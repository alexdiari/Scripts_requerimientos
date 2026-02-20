/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [id]
      ,[nombreServicio]
      ,[cantRegistros]
      ,[fechaInicio]
      ,[nombreArchivo]
      ,[usuario]
      ,[cantRegistrosContRta]
      ,[cantRegistrosSinRta]
      ,[novedad]
      ,[tokenInicial]
      ,[estado]
      ,[fechaFin]
      ,[asunto]
FROM [dbo].[LogConsultasMigracion]
SELECT DB_NAME() AS BaseActual;

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'LogConsultasMigracion';


SELECT *
FROM [dbo].[LogConsultasMigracion]
WHERE [id] = 491;

SELECT *
FROM [dbo].[LogConsultasMigracion]
WHERE [tokenInicial] = '<valor_token>'
ORDER BY [id];

SELECT [id],
       [tokenInicial],
       [nombreArchivo],
       [asunto],
       [usuario],
       [fechaInicio],
       [fechaFin]
FROM [dbo].[LogConsultasMigracion]
WHERE [id] = 491;

SELECT *
FROM [dbo].[LogConsultasMigracion]
WHERE asunto = '2025IE0123129'
  AND usuario = 'josea.gonzalez@contraloria.gov.co'
  AND nombreArchivo = 'PPT.txt'
  AND fechaInicio BETWEEN '2025-10-17 15:52:18' AND '2025-10-17 15:52:21'
ORDER BY id;

SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
  AND TABLE_NAME LIKE '%Log%' OR TABLE_NAME LIKE '%Detalle%';

  SELECT TOP (100)
       *
FROM [dbo].[DetalleConsApiOseiMigracion]
WHERE idLogConsulta = 491;

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'DetalleConsApiOseiMigracion';

SELECT l.id AS IdLog,
       l.nombreArchivo,
       l.usuario,
       l.asunto,
       l.fechaInicio,
       l.fechaFin,
       d.*
FROM [dbo].[LogConsultasMigracion] l
INNER JOIN [dbo].[DetalleConsApiOseiMigracion] d
        ON l.id = d.idLogConsulta
WHERE l.id = 491;

SELECT COUNT(*) AS TotalFilas
FROM [dbo].[DetalleConsApiOseiMigracion];

SELECT DISTINCT idLogConsulta
FROM [dbo].[DetalleConsApiOseiMigracion]
ORDER BY idLogConsulta DESC;

SELECT id, nombreServicio, cantRegistros, estado, novedad
FROM [dbo].[LogConsultasMigracion]
WHERE id = 491;

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%Detalle%';

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME LIKE '%Documento%' OR TABLE_NAME LIKE '%Migracion%';

SELECT *
FROM [dbo].[MigracionRtaConsDocumBD]
WHERE idLogConsulta = 491;






