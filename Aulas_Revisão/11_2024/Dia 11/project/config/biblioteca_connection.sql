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
    status ENUM('disponível', 'emprestado') default 'disponível', 
    codigo int, 
    usuario int,
    foreign key(usuario) references usuario(id_usuario)
);

create table emprestimo (
    id_emprestimo int auto_increment primary key,
    id_usuario int,
    id_livro int,
    devolvido boolean default false,
    foreign key(id_usuario) references usuario(id_usuario),
    foreign key(id_livro) references livro(id_livro)
);

select * from usuario;
select * from livro;
select * from emprestimo;
