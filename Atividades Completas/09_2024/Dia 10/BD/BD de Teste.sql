drop database if exists registros_db;
create database registros_db;
use registros_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    texto VARCHAR(255)         
);

INSERT INTO usuarios (usuario, senha) VALUES
('Filipe', '123'),
('gerente', 'gerente123'),
('funcionario1', 'func123'),
('funcionario2', 'func456'),
('cliente', 'cliente123');

select * from usuarios;