drop database if exists sprint;
create database sprint;
use sprint;

create table Filme(
idFilme int auto_increment primary key,
titulo varchar(50),
genero varchar(40),
diretor varchar (40)
);

INSERT INTO Filme (titulo, genero, diretor) VALUES
	('Mad Max: Estrada da Fúria', 'Ação', 'George Miller'),
	('Mad Max 2: A Caçada Continua', 'Suspense', 'George Miller'),
	('O Exterminador do Futuro', 'Ação', 'James Cameron'),
	('Os Vingadores', 'Ação', 'Joss Whedon'),
	('O Grande Lebowski', 'Comédia', 'Joel Coen'),
	('À Queima-Roupa', 'Comédia', 'Ethan Coen'),
	('A Rede Social', 'Drama', 'David Fincher');
    
-- 1.
select * from Filme;

-- 2.
alter table Filme add column protagonista varchar(50);

-- 3.
update Filme set protagonista = 'Seu Pai';

-- 4.
alter table Filme modify diretor varchar(150);

-- 5. 
update Filme set diretor = 'Joel Alguma coisa' where idFilme = 5;

-- 6.
update Filme set diretor = 'Rafael Fala Baixo' where idFilme in (2,7);

-- 7.
update Filme set titulo = 'País Sem Maravilhas' where idFilme = 6;

-- 8.
delete from Filme where idFilme = 3; 

-- 9.
select * from Filme where genero != 'Drama';

-- 10.
select * from Filme where genero = 'Suspense';

-- 11.
describe Filme;

-- 12.
truncate Filme;
select * from Filme;