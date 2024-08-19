-- create database ecomerce;
use ecomerce;
-- drop database ecomerce;

create table cliente(
cod_cliente int auto_increment primary key,
nome varchar(255) not null,
data_nascimento date not null,
cpf char(11) not null
);

create table pedido(
cod_pedido int auto_increment primary key,
cod_cliente int not null,
data_pedido date not null,
nota_fiscal varchar(255) not null,
valor_total float not null,
foreign key (cod_cliente) references cliente(cod_cliente)
);

create table produto(
cod_produto int auto_increment primary key,
descricao varchar(255) not null,
quantidade int not null
);

create table item_perdido(
cod_pedido int not null,
cod_produto int not null,
numero_item int auto_increment primary key,
volor_unitario float not null,
quantidade int not null,
foreign key (cod_pedido) references pedido(cod_pedido),
foreign key (cod_produto) references produto(cod_produto)
);

create table logado(
cod_log int auto_increment primary key,
data_log date not null,
descricao varchar(255) not null
);

create table requisicao_compra(
cod_requisicao_compra int auto_increment primary key,
cod_produto int not null,
data_requisicao date not null,
quantidade int not null,
foreign key (cod_produto) references item_perdido(cod_produto)
);