drop database cadastro;
create database cadastro;
use cadastro;

create table estado(
id_estado int auto_increment primary key,
nome varchar(100)
);

create table cidade(
id_cidade int auto_increment primary key,
nome varchar(100)
);

create table pessoa(
id int auto_increment primary key,
nome varchar(100),
id_estado int,
id_cidade int,
foreign key fk_estado(id_estado) references estado(id_estado),
foreign key fk_cidade(id_cidade) references cidade(id_cidade)
);

insert into cidade values
(null,"Campo Grande"), 
(null,"Dourados"), 
(null,"Três Lagoas"), 
(null,"Corumbá"), 
(null,"Cuiabá"), 
(null,"Goiania");

insert into estado values
(null,"Mato Grosso"),
(null,"Mato Grosso do Sul"),
(null,"Goias"),
(null,"Paraná"),
(null,"São Paulo"),
(null,"Rio Grande do Sul");

insert into pessoa values
(null,"Ederson da Costa",1,2),
(null,"Maria Aparecida",2,2),
(null,"Pedro Correia",1,3),
(null,"Michael Jackson",2,3),
(null,"Fredie Mercury",3,5);

select pessoa.nome, cidade.nome, estado.nome from pessoa left join cidade on pessoa.id_cidade = cidade.id_cidade right join estado on pessoa.id_estado = estado.id_estado;
select pessoa.nome, cidade.nome, estado.nome from pessoa join cidade on pessoa.id_cidade = cidade.id_cidade join estado on pessoa.id_estado = estado.id_estado;
select pessoa.nome, cidade.nome, estado.nome from pessoa cross join cidade on pessoa.id_cidade = cidade.id_cidade cross join estado on pessoa.id_estado = estado.id_estado;
select nome from pessoa union all select nome from estado union all select nome from cidade;