use netflix;
-- drop database netflix;
-- create database netflix;

create table cliente(
id int auto_increment primary key,
email varchar(255) not null,
senha varchar(100) not null,
nome varchar(255) not null,
telefone char(13) not null,
cpf char(11) not null,
endereco_de_cobranca varchar(255) not null,
numero_do_cartao_credito char(16) not null
);

create table servico(
id int auto_increment primary key,
id_cliente int not null,
assinatura int not null,
mensalidade float not null,
foreign key (id_cliente) references cliente(id)
);

create table filme(
id int auto_increment primary key,
titulo varchar(255) not null,
ano_de_producao date not null,
duracao_em_minutos int not null,
avaliacao int
);

create table serie(
id int auto_increment primary key,
titulo varchar(255) not null,
ano_de_producao date not null,
temporada int not null,
numero_de_episodios int not null,
avaliacao int
);

create table episodio(
id int auto_increment primary key,
id_serie int not null,
id_proximo_episodio int not null,
titulo varchar(255) not null,
duracao_em_minutos int not null,
temporada int not null,
numero_do_episodio int not null,
proximo_episodio int not null,
foreign key (id_serie) references serie(id),
foreign key (id_proximo_episodio) references episodio(id)
);

create table proximo_episodio(
id int auto_increment primary key,
id_serie int not null,
titulo varchar(255) not null,
duracao_em_minutos int not null,
temporada int not null,
numero_do_episodio int not null,
foreign key (id_serie) references serie(id)
);

create table documentario(
id int auto_increment primary key,
titulo varchar(255) not null,
ano_de_producao date not null,
duracao_em_minutos int not null,
nome_da_produtora varchar(255) not null,
avaliacao int
);

create table atores(
id int auto_increment primary key,
nome varchar(255) not null,
data_de_nascimento date not null,
local_de_nascimento varchar(255) not null
);

create table catalogo(
id int auto_increment primary key,
id_serie int not null,
id_filme int not null,
id_documentario int not null,
id_atores int not null,
foreign key (id_serie) references serie(id),
foreign key (id_filme) references filme(id),
foreign key (id_documentario) references documentario(id),
foreign key (id_atores) references atores(id)
);

alter table servico add column id_catalogo int first;
alter table servico add foreign key (id_catalogo) references catalogo(id);