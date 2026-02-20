SELECT TOP (50000)
    db.[TipoDocIdentCons],
    db.[IdentifConsultada] AS IDENTIFICACION,
    db.[Novedad],
    db.[IdJurisdiccion],
    db.[Jurisdiccion],
    db.[Matricula],
    db.[Chip],
    db.[CedulaCatastral],
    db.[Direccion],
    db.[ConsecConsBusqParamLogSupernot],
    db.[FechaConsBusqParamLogSupernot],
    db.[ConsecConsEstJuridicoLogSupernot],
    db.[FechaConsEstJuridicoLogSupernot],
    db.[DepartamentoPredio],
    db.[MunicipioPredio],
    db.[EstadoMatricula],
    db.[NumeroPropietarios],
    db.[PersRecibePredioCodTipoIdentificacion],
    db.[PersRecibePredioNumeroIdentificacion],
    db.[PersRecibePredioPrimerApellido],
    db.[PersRecibePredioSegundoApellido],
    db.[PersRecibePredioPrimerNombre],
    db.[PersRecibePredioSegundoNombre],
    db.[PersRecibePredioNumIdTributaria],
    db.[PersRecibePredioRazonSocial],
    db.[PersRecibePredioEsPropietario],

    -- Información de Anotaciones
    ac.[NumeroAnotacion],
    ac.[FechaAnotacion],
    ac.[RadicacionAnotacion],
    ac.[NomDocumentoAnotacionFolio],
    ac.[CantidadMonetaria],
    ac.[CodNaturalezaJuridicaFolio],
    ac.[NomNaturalezaJuridicaFolio],
    ac.[Comentario],
    ac.[Grupo],
    ac.[CodDocumentoAnotacionFolio],
    ac.[FechaDocumentoAnotacion],
    ac.[EntidadAnotacion],
    ac.[ComentarioEspecificaAnotacionFolio],
    ac.[NombreMunicipioAnotacion],
    ac.[Validez],
    ac.[CodTipoMoneda],

    -- Información Persona Cede
    pc.[RazonSocial] AS RazonSocial_Persona_Cede,
    pc.[NumIdTributaria] AS NumIdTributaria_Persona_Cede,
    pc.[TipoPersona] AS TipoPersona_Persona_Cede,
    pc.[EsPropietario] AS EsPropietario_Persona_Cede,
    pc.[NumeroCedulaCiudadania] AS NumeroCedula_Persona_Cede,
    pc.[CodTipoIdentificacion] AS CodTipoIdentificacion_Persona_Cede,
    pc.[PrimerApellido] AS PrimerApellido_Persona_Cede,
    pc.[SegundoApellido] AS SegundoApellido_Persona_Cede,
    pc.[PrimerNombre] AS PrimerNombre_Persona_Cede,
    pc.[SegundoNombre] AS SegundoNombre_Persona_Cede,
    pc.[PorcentajeParticipacion] AS PorcentajeParticipacion_Persona_Cede,

    -- Información Persona Recibe
    pr.[PrimerApellido] AS PrimerApellido_Persona_Recibe,
    pr.[SegundoApellido] AS SegundoApellido_Persona_Recibe,
    pr.[PrimerNombre] AS PrimerNombre_Persona_Recibe,
    pr.[SegundoNombre] AS SegundoNombre_Persona_Recibe,
    pr.[CodTipoIdentificacion] AS CodTipoIdentificacion_Persona_Recibe,
    pr.[NumeroCedulaCiudadania] AS NumeroCedula_Persona_Recibe,
    pr.[EsPropietario] AS EsPropietario_Persona_Recibe,
    pr.[TipoPersona] AS TipoPersona_Persona_Recibe,
    pr.[NumIdTributaria] AS NumIdTributaria_Persona_Recibe,
    pr.[RazonSocial] AS RazonSocial_Persona_Recibe,
    pr.[PorcentajeParticipacion] AS PorcentajeParticipacion_Persona_Recibe,

    -- Información de Propietarios Actuales
    mp.[TipoPersona] AS TipoPersona_Propietario,
    mp.[NumeroCedulaCiudadania] AS Cedula_Propietario,
    mp.[NumIdTributaria] AS Nit_Propietario,
    mp.[EsPropietario] AS EsPropietario_Propietario,
    mp.[RazonSocial] AS RazonSocial_Propietario,
    mp.[PrimerApellido] AS PrimerApellido_Propietario,
    mp.[SegundoApellido] AS SegundoApellido_Propietario,
    mp.[PrimerNombre] AS PrimerNombre_Propietario,
    mp.[SegundoNombre] AS SegundoNombre_Propietario

FROM [dbo].[Matriculas_DatosBasicos] db
LEFT JOIN [dbo].[Matricula_AnotacionCertificado] ac 
       ON db.[Id] = ac.[IdMatriculaDatosBasicosId]
LEFT JOIN [dbo].[AnotacionCertificado_Persona_Cede] pc 
       ON ac.[Id] = pc.[AnotacionCertificadoId]
LEFT JOIN [dbo].[AnotacionCertificado_Persona_Recibe] pr 
       ON ac.[Id] = pr.[AnotacionCertificadoId]
LEFT JOIN [dbo].[Matricula_Propietarios_Actuales] mp 
       ON db.[Id] = mp.[MatriculaDatosBasicosId]

WHERE db.[idLogConsulta] = '6708';

