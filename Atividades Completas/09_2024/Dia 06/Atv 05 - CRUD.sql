drop database if exists sprint;
create database sprint;
use sprint;

create table Curso(
idCurso int auto_increment primary key,
nome varchar(50),
sigla char(3),
coordenador varchar(50)
);

insert into Curso(nome, sigla, coordenador) values
    ('Física Geral', 'FG', 'Dr. Valdemir'),
    ('Química Orgânica', 'QO', 'Prof. Marta'),
    ('Biologia Molecular', 'BM', 'Dr. Rafael');
    
-- A.
select * from Curso;

-- B.
select coordenador from Curso;

-- C.
select * from Curso where sigla = 'FG';

-- D.
select * from Curso order by nome;

-- E.
select * from Curso order by coordenador desc;

-- F.
select * from Curso where nome like 'F%';

-- G.
select * from Curso where nome like '%R';

-- H. 
select * from Curso where nome like '_I%';

-- I. 
select * from Curso where nome like '%A_';

-- J.
truncate table Curso;
