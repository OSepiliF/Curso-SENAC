drop database if exists sprint;
create database sprint;
use sprint;

create table Revista(
idRevista int auto_increment primary key,
nome varchar(40),
categoria varchar(30)
);

insert into Revista(nome) values
	('Veja'),
    ('Tendencias'),
    ('Atualizações');
    
-- 1.
select * from Revista;

-- 2. 
update Revista set categoria = 'Fofocas' where idRevista = 1;
update Revista set categoria = 'Semanal' where idRevista = 2;
update Revista set categoria = 'Dia a Dia' where idRevista = 3;
select * from Revista;

-- 3.
insert into Revista(nome, categoria) values
	('Futebol do Ano','Esportes'),
    ('Reclamações','Reportagem'),
    ('Atualizações Semanal','Semanal');

-- 4.
select * from Revista;

-- 5.
describe Revista;

-- 6.
alter table Revista modify categoria varchar(40);

-- 7.
describe Revista;

-- 8.
alter table Revista add column periodicidade varchar(15);

-- 9.
select * from Revista;

-- 10.
alter table Revista drop column periodicidade;