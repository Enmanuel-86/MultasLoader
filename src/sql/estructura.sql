CREATE DATABASE IF NOT EXISTS multasloader;
-- DROP DATABASE multasloader;

USE multasloader;

#DROP DATABASE multasloader;

# Creamos la tabla en donde se almacenan los datos de las  personas
CREATE TABLE multasloader.personas(
	id_persona INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	cedula VARCHAR(15) NOT NULL UNIQUE,
	nombre VARCHAR(50) NOT NULL,
	apellido VARCHAR(50) NOT NULL,
	residencia VARCHAR(50) NOT NULL
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- DROP TABLE multasloader.catalogo_vehiculos;
CREATE TABLE multasloader.catalogo_tipos_vehiculos(
	id_tipo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	tipo VARCHAR(20) NOT NULL UNIQUE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE multasloader.catalogo_modelos_vehiculos(
	id_modelo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	modelo VARCHAR(30) NOT NULL UNIQUE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

CREATE TABLE multasloader.catalogo_marcas_vehiculos(
	id_marca INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	marca VARCHAR(30) NOT NULL UNIQUE
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- DROP TABLE multasloader.vehiculos;
# Creamos la tabla en donde se almacenan los datos los vehiculos
CREATE TABLE multasloader.vehiculos(
	id_vehiculo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	id_tipo INT UNSIGNED NOT NULL,
	id_modelo INT UNSIGNED,
	id_marca INT UNSIGNED,
	placa VARCHAR(20) UNIQUE,
	color VARCHAR(50) DEFAULT "N/A",
	FOREIGN KEY (id_tipo) REFERENCES multasloader.catalogo_tipos_vehiculos(id_tipo)
		ON UPDATE CASCADE
		ON DELETE RESTRICT,
	FOREIGN KEY (id_modelo) REFERENCES multasloader.catalogo_modelos_vehiculos(id_modelo)
		ON UPDATE CASCADE
		ON DELETE RESTRICT,
	FOREIGN KEY (id_marca) REFERENCES multasloader.catalogo_marcas_vehiculos(id_marca)
		ON UPDATE CASCADE
		ON DELETE RESTRICT
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- DROP TABLE multasloader.multados_por_vehiculo;
CREATE TABLE multasloader.multados_por_vehiculo(
	id_multa_por_vehiculo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	id_persona INT UNSIGNED NOT NULL, 
	id_vehiculo INT UNSIGNED NOT NULL,
	lugar_acontecimiento VARCHAR(70) NOT NULL,
	fecha_multa DATE NOT NULL,
	monto_cancelar DECIMAL(10,2) NOT NULL,
	FOREIGN KEY (id_persona) REFERENCES multasloader.personas(id_persona)
		ON UPDATE CASCADE
		ON DELETE RESTRICT,
	FOREIGN KEY (id_vehiculo) REFERENCES multasloader.vehiculos(id_vehiculo)
		ON UPDATE CASCADE
		ON DELETE RESTRICT
	
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;

-- DROP TABLE multasloader.multados_en_espera;
CREATE TABLE multasloader.multados_en_espera(
	id_multa_en_espera INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	id_persona INT UNSIGNED, 
	id_vehiculo INT UNSIGNED,
	lugar_acontecimiento VARCHAR(70) NOT NULL,
	fecha_multa DATE NOT NULL,
	monto_cancelar DECIMAL(10,2) NOT NULL,
	FOREIGN KEY (id_persona) REFERENCES multasloader.personas(id_persona)
		ON UPDATE CASCADE
		ON DELETE RESTRICT,
	FOREIGN KEY (id_vehiculo) REFERENCES multasloader.vehiculos(id_vehiculo)
		ON UPDATE CASCADE
		ON DELETE RESTRICT
	
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;