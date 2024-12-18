DROP DATABASE IF EXISTS Formularios;
CREATE DATABASE IF NOT EXISTS Formularios;
USE Formularios;

CREATE TABLE Formulario(
idFormulario INTEGER PRIMARY KEY AUTO_INCREMENT,
Nombre VARCHAR (30) NOT NULL, 
Descripcion VARCHAR (40) NOT NULL, 
Fecha_Creacion DATE NOT NULL
);

CREATE TABLE InfoForm(
idInfoForm INTEGER PRIMARY KEY AUTO_INCREMENT,
Tipo VARCHAR (20) NOT NULL, 
Titulo VARCHAR (30) NOT NULL, 
Opciones VARCHAR (100) NOT NULL, 
idFormulario INTEGER not null, 
FOREIGN KEY (idFormulario) 
REFERENCES Formulario(idFormulario)
);

SELECT * FROM Formulario;

INSERT INTO  Formulario  VALUES ("Test de velocidad", "Es un test del mas rapido", "2024-12-12" );
