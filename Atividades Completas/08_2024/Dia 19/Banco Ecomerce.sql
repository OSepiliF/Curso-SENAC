drop database ecomerce;
create database ecomerce;
use ecomerce;

create table EX2_CLIENTE(
codcliente int auto_increment primary key,
nome varchar(255) not null,
datanascimento date not null,
cpf char(11) not null
);

create table EX2_PEDIDO(
codpedido int auto_increment primary key,
codcliente int not null,
datapedido date not null,
notafiscal varchar(255) not null,
valortotal float not null,
foreign key (codcliente) references EX2_CLIENTE(codcliente)
);

create table EX2_PRODUTO(
codproduto int auto_increment primary key,
descricao varchar(255) not null,
quantidade int not null
);

create table EX2_ITEMPEDIDO(
codpedido int not null,
codproduto int not null,
numeroitem int auto_increment primary key,
volorunitario float not null,
quantidade int not null,
foreign key (codpedido) references EX2_PEDIDO(codpedido),
foreign key (codproduto) references EX2_PRODUTO(codproduto)
);

create table EX2_LOG(
codlog int auto_increment primary key,
data date not null,
descricao varchar(255) not null
);

create table EX2_REQUISICAO_COMPRA(
codrequisicaocompra int auto_increment primary key,
codproduto int not null,
data date not null,
quantidade int not null,
foreign key (codproduto) references EX2_ITEMPEDIDO(codproduto)
);