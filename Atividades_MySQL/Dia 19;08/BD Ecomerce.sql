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
valorunitario float not null,
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

insert into EX2_CLIENTE(codcliente,nome,datanascimento,cpf) value
	(null,"Cliente","2004-03-04","12345678910"),
    (null,"Cliente","2004-03-04","12345678910"),
    (null,"Cliente","2004-03-04","12345678910"),
    (null,"Cliente","2004-03-04","12345678910"),
    (null,"Cliente","2004-03-04","12345678910"),
    (null,"Cliente","2004-03-04","12345678910"),
    (null,"Cliente","2004-03-04","12345678910"),
    (null,"Cliente","2004-03-04","12345678910"),
    (null,"Cliente","2004-03-04","12345678910"),
    (null,"Cliente","2004-03-04","12345678910");
	
insert into EX2_PRODUTO(codproduto,descricao,quantidade) value
	(null,"Descrição",1),
    (null,"Descrição",2),
    (null,"Descrição",10),
    (null,"Descrição",42),
    (null,"Descrição",1),
    (null,"Descrição",2),
    (null,"Descrição",7),
    (null,"Descrição",90);
	
insert into EX2_PEDIDO(codpedido,codcliente,datapedido,notafiscal,valortotal) value
	(null,1,"2024-05-03","049402073200323399330","32.00"),
    (null,2,"2024-05-03","044020732002336999330","23.50"),
    (null,3,"2024-05-03","040207372200239399330","92.55"),
    (null,4,"2024-05-03","040207324002374399330","10.99"),
    (null,5,"2024-05-03","040207320023399885330","232.05");
	
insert into EX2_ITEMPEDIDO(codpedido,codproduto,numeroitem,valorunitario,quantidade) value
	(1,1,null,"60.00",2),
	(2,2,null,"50.08",1),
	(3,3,null,"64.50",4),
	(4,4,null,"46.00",3),
	(5,5,null,"42.50",5);
    
select * from EX2_CLIENTE;
select * from EX2_PRODUTO;
select * from EX2_PEDIDO;
select * from EX2_ITEMPEDIDO;