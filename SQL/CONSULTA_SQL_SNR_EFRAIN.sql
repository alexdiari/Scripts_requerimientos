SELECT db.idLogConsulta, db.id, db.IdentifConsultada, db.IdJurisdiccion ,db.Matricula, db.novedad, db.Direccion, db.Chip, db.CedulaCatastral,
ac.NumeroAnotacion,  ac.FechaAnotacion, ac.ComentarioEspecificaAnotacionFolio, ac.CantidadMonetaria, ac.NomDocumentoAnotacionFolio, ac.EntidadAnotacion,
pc.TipoPersona, pc.NumeroCedulaCiudadania Identif_Cede, pc.NumIdTributaria IdentTribut_Cede, pr.TipoPersona, pr.NumeroCedulaCiudadania Ident_Recibe, pr.NumIdTributaria IdentTribut_Recibe,db.RtaSupernot
FROM [dbo].[Matriculas_DatosBasicos] db
left join Matricula_AnotacionCertificado ac on db.id = ac.IdMatriculaDatosBasicosid
left join AnotacionCertificado_Persona_Cede pc on ac.id = pc.AnotacionCertificadoid
left join AnotacionCertificado_Persona_Recibe pr on ac.id = pr.AnotacionCertificadoid
where db.idLogConsulta = 6708