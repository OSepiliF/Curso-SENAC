drop database if exists sprint;
create database sprint;
use sprint;

create table Professor(
idProfessor int auto_increment primary key,
nome varchar(50),
especialidade varchar(50),
dtNasc date);

insert into Professor(nome, especialidade, dtNasc) values
    ('Jeferson', 'Matematica', '1999-12-23'),
    ('Ana', 'Física', '1985-06-15'),
    ('Carlos', 'Química', '1978-11-02'),
    ('Beatriz', 'Biologia', '1990-09-17'),
    ('Eduardo', 'História', '1982-03-05'),
    ('Fernanda', 'Geografia', '1988-12-25');

-- A.
select * from Professor;

-- B.
alter table Professor add column titulares enum('monitor','assistente','titular');

-- C.
update Professor set titulares = 'monitor' where idProfessor = 1;
update Professor set titulares = 'assistente' where idProfessor = 2;
update Professor set titulares = 'titular' where idProfessor = 3;
update Professor set titulares = 'monitor' where idProfessor = 4;
update Professor set titulares = 'assistente' where idProfessor = 5;
update Professor set titulares = 'titular' where idProfessor = 6;

-- D.
insert into Professor(nome, especialidade, dtNasc, titulares) values
	('Roberto','Português','1997-02-21','Titular');
    
-- E.
delete from Professor where idProfessor = 5;

-- F.
select nome from Professor where titulares = 'titular';

-- G.
select especialidade, dtNasc from Professor where titulares = 'monitor';

-- H.
update Professor set dtNasc = '1999-01-01' where idProfessor = 3;

-- I.
truncate table Professor;