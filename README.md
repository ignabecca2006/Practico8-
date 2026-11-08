# Práctico 8 - Registro de Pacientes

Aplicación de escritorio desarrollada en Python con CustomTkinter y SQL Server.

## Funcionalidades

- Registrar pacientes mediante un formulario.
- Ingresar ID, nombre y fecha de nacimiento.
- Seleccionar sexo y cobertura médica.
- Indicar si el paciente es donador de órganos.
- Guardar los registros en una base de datos SQL Server.
- Limpiar el formulario mediante el botón Cancelar.

## Tecnologías utilizadas

- Python
- CustomTkinter
- pyodbc
- Microsoft SQL Server

## Instalación

1. Instalar Python y las dependencias incluidas en `requirements.txt`.
2. Ejecutar `database.sql` en SQL Server para crear la base de datos y la tabla.
3. Configurar el nombre del servidor en `conexion.py`.
4. Ejecutar la aplicación con `python main.py`.

## Base de datos

La base de datos `Practico8` contiene la tabla `Pacientes`, donde se almacenan los registros ingresados desde la aplicación.