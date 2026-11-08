
-- Crear base de datos
CREATE DATABASE Practico8;
GO

-- Seleccionar base de datos
USE Practico8;
GO

-- Crear tabla de pacientes
CREATE TABLE Pacientes (
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    sexo VARCHAR(20) NOT NULL,
    donador_organos BIT NOT NULL,
    cobertura VARCHAR(20) NOT NULL
);
GO

-- Consultar pacientes registrados
SELECT * FROM Pacientes;
