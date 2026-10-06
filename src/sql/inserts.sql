INSERT INTO multasloader.personas(cedula, nombre, apellido, residencia)
VALUES ("30751989", "Juan", "Perez", "Barcelona"),
       ("8281565", "Mario", "Bros", "New York"),
       ("6321458", "Pedro", "Stone", "Pto la cruz"),
       ("25123444", "Maria", "Rosario", "Guanta");

INSERT INTO multasloader.catalogo_tipos_vehiculos(tipo)
VALUES ("Moto"),
       ("Carro"),
       ("Camioneta"),
       ("Carrucha"),
       ("Bicicleta"),
       ("Motocicleta"),
       ("Cuatrimoto"),
       ("Camion");

INSERT INTO multasloader.catalogo_marcas_vehiculos (marca) 
VALUES ('Empire Keeway'),
       ('Bera'),
       ('Honda'),
       ('Yamaha'),
       ('Suzuki'),
       ('Toyota'),
       ('Chevrolet'),
       ('Ford'),
       ('Hyundai'),
       ('Fiat'),
       ('Isuzu'),
       ('Mack'),
       ('Iveco'),
       ('Nissan'),
       ('Mitsubishi');

INSERT INTO multasloader.catalogo_modelos_vehiculos (modelo) 
VALUES ('Horse 150'),
       ('SBR 150'),
       ('Cargo 150'),
       ('YBR 125'),
       ('GN 125'),
       ('Corolla'),
       ('Aveo'),
       ('Fiesta'),
       ('Accent'),
       ('Uno'),
       ('NPR'),
       ('FVR'),
       ('Cargo 1722'),
       ('Granite'),
       ('Stralis'),
       ('Hilux'),
       ('Silverado'),
       ('F-150'),
       ('Frontier'),
       ('L200');

-- Opción 1: Insert directo asumiendo IDs autoincrementales continuos (1..N)

INSERT INTO multasloader.vehiculos (id_tipo, id_modelo, id_marca, placa, color) VALUES
-- Motos 
(1, 1, 1, 'AA1B23C', 'Negro'),     -- Horse 150 / Empire Keeway
(1, 2, 2, 'AB2C34D', 'Azul'),      -- SBR 150 / Bera
(1, 5, 5, 'AC3D45E', 'Rojo'),      -- GN 125 / Suzuki
-- Carros 
(2, 6, 6, 'ABC123D', 'Blanco'),    -- Corolla / Toyota
(2, 7, 7, 'XYZ789E', 'Gris'),      -- Aveo / Chevrolet
(2, 8, 8, 'JKL456F', 'Rojo'),      -- Fiesta / Ford
(2, 10, 10, 'MNO321G', 'Verde'),   -- Uno / Fiat
-- Camionetas 
(3, 16, 6, 'A12BC3D', 'Plateado'), -- Hilux / Toyota
(3, 17, 7, 'B34CD5E', 'Blanco'),   -- Silverado / Chevrolet
(3, 18, 8, 'C56DE7F', 'Negro'),    -- F-150 / Ford
(8, 11, 11, 'A98BC7D', 'Blanco'),  -- NPR / Isuzu
(8, 14, 12, 'C45DE6F', 'Amarillo');-- Granite / Mack
INSERT INTO multasloader.vehiculos(id_tipo, id_modelo, id_marca, placa, color)
VALUES (4,Null,NULL, NULL, NULL);
       

INSERT INTO multasloader.multados_en_espera(id_persona, id_vehiculo, lugar_acontecimiento, fecha_multa, monto_cancelar)
VALUES (1,1, 'Av fuerzas armadas', STR_TO_DATE('06/10/2026', '%d/%m/%ys'), 14563.22);

DELETE FROM multasloader.multados_en_espera WHERE id_multados = 1;