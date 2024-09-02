drop database if exists Banco_Mercado;
create database Banco_Mercado;
use Banco_Mercado;

create table fornecedores(
cod_forne varchar(20) primary key not null,
nome varchar(100) not null,
cidade_sede varchar(50) not null,
grupo_cod_fornecedor varchar(25)
);

create table material(
cod_material int primary key not null,
cod_fornecedor varchar(20),
nome varchar(100) not null,
descricao varchar(100),
foreign key (cod_fornecedor) references fornecedores(cod_forne)
);

insert into fornecedores(cod_forne, nome, cidade_sede, grupo_cod_fornecedor) values
	('ABC', 'ABC Materiais Eletricos', 'Vitoria', Null),
	('XYZ', 'XYZ Materias de Escritorio', 'Rio de Janeiro', 'HIX'),
    ('Hidra', 'Hidra Materiais Hidraulicos', 'Sao Paulo', 'HIX'),
	('HIX', 'HidraX Materias Eletricos e Hidraulicos', 'Sao Paulo', Null);
    
insert into material (cod_material, cod_fornecedor, nome, descricao) values
    ('123', 'ABC', 'Tomada eletrica 10A Nova', 'Tomada eletrica 10A padrao novo'),
    ('234', 'ABC', 'Disjuntor 25A', 'Disjuntor eletrico 25A'),
    ('345', 'XYZ', 'Resma Papel A4', 'Resma papel branco A4'),
    ('456', 'XYZ', 'Toner Imp HR5522', 'Toner impressora HR5522'),
    ('678', 'Hidra', 'Cano PVC 1/2', 'Cano PVC 1/2 pol'),
    ('679', 'Hidra', 'Cano PVC 3/4', 'Cano PVC 3/4 pol'),
    ('680', 'Hidra', 'Medidor hidr 1/2', 'Medidor hidraulico 1/2 pol'),
    ('681', 'Hidra', 'Joelho 1/2', 'Conector Joelho 1/2 pol'),
    ('682', 'Hidra', 'Junta 1/2', 'Cano PVC 1/2 pol'),
    ('1234', 'ABC', 'Tomada eletrica 20A Nova', 'Tomada eletrica 20A padrao novo'),
    ('2345', 'XYZ', 'Caneta Azul', 'Caneta esferografica azul'),
    ('4567', 'XYZ', 'Grapeador', 'Grampeador mesa pequeno'),
    ('4568', 'XYZ', 'Caneta Marca Texto Amarela', 'Caneta Marca Texto Amarela'),
    ('4569', 'XYZ', 'Lapis HB', 'Lapis Preto HB');

select * from fornecedores;
select * from material;
select * from fornecedores join material on material.cod_fornecedor = fornecedores.cod_forne;
	
-- Quantos materiais possuem o Fornecedor ABC;
select count(cod_material) from material where cod_fornecedor like "ABC%";

-- Quantos materiais possuem o Fornecedor XYZ;
select count(cod_material) from material where cod_fornecedor like "XYZ%";

-- Quantos materiais possuem o Fornecedor HYDRA;
select count(cod_material) from material where cod_fornecedor like "HIDRA";