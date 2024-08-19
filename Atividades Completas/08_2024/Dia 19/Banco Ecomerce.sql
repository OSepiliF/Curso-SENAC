-- create database ecomerce;
use ecomerce;
-- drop database ecomerce;

create table EX2_CLIENTE(
cod_cliente int auto_increment primary key,
nome varchar(255) not null,
data_nascimento date not null,
cpf char(11) not null
);

create table EX2_PEDIDO(
cod_pedido int auto_increment primary key,
cod_cliente int not null,
data_pedido date not null,
nota_fiscal varchar(255) not null,
valor_total float not null,
foreign key (cod_cliente) references EX2_CLIENTE(cod_cliente)
);

create table EX2_PRODUTO(
cod_produto int auto_increment primary key,
descricao varchar(255) not null,
quantidade int not null
);

create table EX2_ITEMPEDIDO(
cod_pedido int not null,
cod_produto int not null,
numero_item int auto_increment primary key,
volor_unitario float not null,
quantidade int not null,
foreign key (cod_pedido) references EX2_PEDIDO(cod_pedido),
foreign key (cod_produto) references EX2_PRODUTO(cod_produto)
);

create table EX2_LOG(
cod_log int auto_increment primary key,
data_log date not null,
descricao varchar(255) not null
);

create table EX2_REQUISICAO_COMPRA(
cod_requisicao_compra int auto_increment primary key,
cod_produto int not null,
data_requisicao date not null,
quantidade int not null,
foreign key (cod_produto) references EX2_ITEMPEDIDO(cod_produto)
);