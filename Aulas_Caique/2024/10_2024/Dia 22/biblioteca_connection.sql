DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cpf CHAR(11),
    telefone CHAR(20),
    senha VARCHAR(40)
);

CREATE TABLE livro (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(80),
    autor VARCHAR(50),
    genero VARCHAR(50),
    status ENUM('disponível', 'emprestado') DEFAULT 'disponível', 
    codigo INT, 
    usuario INT,
    FOREIGN KEY(usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE emprestimo (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_livro INT,
    devolvido BOOLEAN DEFAULT FALSE,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
    FOREIGN KEY(id_livro) REFERENCES livro(id_livro)
);

SELECT * FROM usuario;
SELECT * FROM livro;
SELECT * FROM emprestimo;
