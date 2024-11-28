drop database if exists biblioteca;
create database biblioteca;
use biblioteca;

create table usuario (
    id_usuario int auto_increment primary key,
    nome varchar(100),
    cpf char(11),
    telefone char(20),
    senha varchar(40)
);

create table livro (
    id_livro int auto_increment primary key,
    titulo varchar(80),
    autor varchar(50),
    genero varchar(50),
    status ENUM('disponível', 'emprestado') DEFAULT 'disponível', 
    codigo int, 
    usuario int,
    foreign key(usuario) references usuario(id_usuario)
);

create table emprestimo (
    id_emprestimo int auto_increment primary key,
    id_livro int, 
    id_usuario int,
    foreign key(id_livro) references livro(id_livro),
    foreign key(id_usuario) references usuario(id_usuario) 
);

select * from livro;
select * from livro join usuario on livro.usuario = usuario.id_usuario;
