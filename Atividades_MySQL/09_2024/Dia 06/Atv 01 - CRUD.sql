drop database if exists sprint;
create database sprint;
use sprint;

create table Atleta(
idAtleta int auto_increment primary key,
nome varchar (40),
modalidade varchar(40),
qtdMedalha int
);

insert into Atleta(idAtleta, nome, modalidade, qtdMedalha) values
	(null,'Rafael', 'Atletismo', 4),
    (null,'João', 'Natação', 1),
    (null,'Carlos', 'Salto com Vara', 5),
    (null,'Luiza', 'Judô', 3),
    (null,'Pedro', 'Corrida de Obstaculos', 2);
    
-- 1.
select * from Atleta;

-- 2.
update Atleta set qtdMedalha = 20 where idAtleta = 1;
select qtdMedalha from Atleta;

-- 3.
update Atleta set qtdMedalha = 10 where idAtleta >= 2 and idAtleta <= 3;
select qtdMedalha from Atleta;

-- 4.
update Atleta set nome = 'Sabrina' where idAtleta = 4;
select nome from Atleta;

-- 5.
alter table Atleta add column (dataNasc date);
select dataNasc from Atleta;

-- 6.
update Atleta set dataNasc = '1991-10-18';
select dataNasc from Atleta;

-- 7.
delete from Atleta where idAtleta = 5;
select * from Atleta;

-- 8.
select * from Atleta where modalidade != 'Natação';

-- 9.
select * from Atleta where qtdMedalha >= 3;

-- 10.
alter table Atleta modify modalidade varchar(60);

-- 11.
describe Atleta;

-- 12.
delete from Atleta;
select * from Atleta;