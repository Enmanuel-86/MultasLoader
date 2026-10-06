SELECT * FROM multasloader.personas;
SELECT * FROM multasloader.catalogo_tipos_vehiculos;
SELECT * FROM multasloader.catalogo_marcas_vehiculos;
SELECT * FROM multasloader.catalogo_modelos_vehiculos;
SELECT * FROM multasloader.vehiculos;
SELECT * FROM multasloader.multados_en_espera;

SELECT p.nombre, p.apellido, lugar_acontecimiento 
FROM multasloader.multados_en_espera AS m
INNER JOIN multasloader.personas AS p ON p.id_persona = m.id_persona; 



# INNER JOIN para ver la consulta completa del multado en espera
SELECT p.nombre, p.apellido,
	   -- ctv.tipo, ctml.modelo, ctmc.marca,
	   v.id_vehiculo AS 'Numero de vehiculo', ctv.tipo, ctml.modelo, ctmc.marca, v.placa, v.color,
	   m.fecha_multa, m.monto_cancelar 
FROM multasloader.multados_en_espera AS m
INNER JOIN multasloader.personas AS p 
	ON p.id_persona = m.id_persona	
INNER JOIN multasloader.vehiculos AS v 
	ON v.id_vehiculo = m.id_vehiculo 
INNER JOIN multasloader.catalogo_tipos_vehiculos AS ctv 
	ON ctv.id_tipo = v.id_tipo
INNER JOIN multasloader.catalogo_modelos_vehiculos AS ctml
	ON ctml.id_modelo = v.id_modelo
INNER JOIN multasloader.catalogo_marcas_vehiculos AS ctmc
	ON ctmc.id_marca = v.id_marca
ORDER BY m.id_multa_en_espera   ASC
;
