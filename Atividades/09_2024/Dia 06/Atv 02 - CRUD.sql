drop database if exists sprint;
create database sprint;
use sprint;

create Table Musica(
idMusica int auto_increment primary key,
titulo varchar(40),
artista varchar(40),
genero varchar(40)
);

insert into Musica (titulo, artista, genero) values
	('Song 1', 'Artist A', 'Pop'),
	('Song 2', 'Artist B', 'Hip-Hop'),
	('Song 3', 'Artist C', 'Funk'),
	('Song 4', 'Artist D', 'Rock'),
	('Song 5', 'Artist E', 'Jazz'),
	('Song 6', 'Artist F', 'Pop'),
	('Song 7', 'Artist G', 'Classical');
    
-- A.
select * from Musica;

-- B.
alter table Musica add column (curtidas int);

-- C.
update Musica set curtidas = 10;

-- D.
alter table Musica modify artista varchar(80);

-- E.
update Musica set curtidas = 5000 where idMusica = 1;

-- F.
update Musica set curtidas = 8000 where idMusica >= 2 and idMusica <=3;

-- G.
update Musica set titulo = 'Suavão' where idMusica = 5;

-- H.
delete from Musica where idMusica = 4;

-- I.
select * from Musica where genero != 'Funk';

-- J.
select * from Musica where curtidas >= 20;

-- K.
describe Musica;

-- L.
truncate Musica;
select * from Musica;