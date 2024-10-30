drop database if exists Cadastro;
create database Cadastro;
use Cadastro;

create table estado (
id_estado int auto_increment primary key,
estado varchar(100) not null
);

create table cidade (
id_cidade int auto_increment primary key,
cidade varchar(100) not null,
id_estado int,
foreign key (id_estado) references estado(id_estado)
);

create table sexo (
id_sexo int auto_increment primary key,
sexo varchar(20) not null
);

create table nacionalidade (
id_nacionalidade int auto_increment primary key,
nacionalidade varchar(50) not null
);

create table raca (
id_raca int auto_increment primary key,
raca varchar(50) not null
);

create table escolaridade (
id_escolaridade int auto_increment primary key,
escolaridade varchar(50) not null
);

create table civil(
id_estado_civil int auto_increment primary key,
estado_civil varchar(50)
);

create table clientes (
cpf char(11) primary key not null,
nome varchar(100) not null,
rg varchar(9) not null,
id_cidade int,
id_sexo int,
id_nacionalidade int,
fone varchar(20) not null,
id_raca int,
id_escolaridade int,
id_estado_civil int,
foreign key (id_cidade) references cidade(id_cidade),
foreign key (id_sexo) references sexo(id_sexo),
foreign key (id_nacionalidade) references nacionalidade(id_nacionalidade),
foreign key (id_raca) references raca(id_raca),
foreign key (id_escolaridade) references escolaridade(id_escolaridade),
foreign key (id_estado_civil) references civil(id_estado_civil)
);

insert into estado (estado) values 
('Acre'),
('Alagoas'),
('Amazonas'),
('Bahia'),
('Ceará'),
('Distrito Federal'),
('Espírito Santo'),
('Goiás'),
('Maranhão'),
('Mato Grosso'),
('Mato Grosso do Sul'),
('Minas Gerais'),
('Pará'),
('Paraíba'),
('Paraná'),
('Pernambuco'),
('Piauí'),
('Rio de Janeiro'),
('Rio Grande do Norte'),
('Rio Grande do Sul'),
('Rondônia'),
('Roraima'),
('Santa Catarina'),
('São Paulo'),
('Sergipe'),
('Tocantins');

insert into cidade (cidade, id_estado) values
-- Acre
('Rio Branco', 1),
('Cruzeiro do Sul', 1),
('Sena Madureira', 1),
('Tarauacá', 1),
('Feijó', 1),
-- Alagoas
('Maceió', 2),
('Arapiraca', 2),
('Palmeira dos Índios', 2),
('Penedo', 2),
('Delmiro Gouveia', 2),
-- Amazonas
('Manaus', 3),
('Parintins', 3),
('Itacoatiara', 3),
('Telfé', 3),
('Coari', 3),
-- Bahia
('Salvador', 4),
('Feira de Santana', 4),
('Vitória da Conquista', 4),
('Camaçari', 4),
('Ilhéus', 4),
-- Ceará
('Fortaleza', 5),
('Juazeiro do Norte', 5),
('Sobral', 5),
('Crato', 5),
('Maracanaú', 5),
-- Distrito Federal
('Brasília', 6),
('Taguatinga', 6),
('Ceilândia', 6),
('Samambaia', 6),
('Gama', 6),
-- Espírito Santo
('Vitória', 7),
('Vila Velha', 7),
('Serra', 7),
('Cariacica', 7),
('Colatina', 7),
-- Goiás
('Goiânia', 8),
('Aparecida de Goiânia', 8),
('Anápolis', 8),
('Rio Verde', 8),
('Catalão', 8),
-- Maranhão
('São Luís', 9),
('Imperatriz', 9),
('Caxias', 9),
('Timon', 9),
('Bacabal', 9),
-- Mato Grosso
('Cuiabá', 10),
('Várzea Grande', 10),
('Rondonópolis', 10),
('Sinop', 10),
('Tangará da Serra', 10),
-- Mato Grosso do Sul
('Campo Grande', 11),
('Dourados', 11),
('Três Lagoas', 11),
('Corumbá', 11),
('Ponta Porã', 11),
-- Minas Gerais
('Belo Horizonte', 12),
('Uberlândia', 12),
('Contagem', 12),
('Juiz de Fora', 12),
('Montes Claros', 12),
-- Pará
('Belém', 13),
('Ananindeua', 13),
('Santarém', 13),
('Marabá', 13),
('Castanhal', 13),
-- Paraíba
('João Pessoa', 14),
('Campina Grande', 14),
('Santa Rita', 14),
('Patos', 14),
('Bayeux', 14),
-- Paraná
('Curitiba', 15),
('Londrina', 15),
('Maringá', 15),
('Ponta Grossa', 15),
('Cascavel', 15),
-- Pernambuco
('Recife', 16),
('Olinda', 16),
('Jaboatão dos Guararapes', 16),
('Caruaru', 16),
('Petrolina', 16),
-- Piauí
('Teresina', 17),
('Parnaíba', 17),
('Picos', 17),
('Floriano', 17),
('Oeiras', 17),
-- Rio de Janeiro
('Rio de Janeiro', 18),
('Niterói', 18),
('Nova Iguaçu', 18),
('Campos dos Goytacazes', 18),
('Duque de Caxias', 18),
-- Rio Grande do Norte
('Natal', 19),
('Mossoró', 19),
('Caicó', 19),
('Parnamirim', 19),
('Santa Cruz', 19),
-- Rio Grande do Sul
('Porto Alegre', 20),
('Caxias do Sul', 20),
('Pelotas', 20),
('Santa Maria', 20),
('Gravataí', 20),
-- Rondônia
('Porto Velho', 21),
('Ji-Paraná', 21),
('Vilhena', 21),
('Rolim de Moura', 21),
('Ouro Preto do Oeste', 21),
-- Roraima
('Boa Vista', 22),
('Rorainópolis', 22),
('Caracaraí', 22),
('Mucajaí', 22),
('Normandia', 22),
-- Santa Catarina
('Florianópolis', 23),
('Joinville', 23),
('Blumenau', 23),
('Chapecó', 23),
('Criciúma', 23),
-- São Paulo
('São Paulo', 24),
('Campinas', 24),
('Sorocaba', 24),
('Santos', 24),
('São José dos Campos', 24),
-- Sergipe
('Aracaju', 25),
('Lagarto', 25),
('Itabaiana', 25),
('Nossa Senhora do Socorro', 25),
('São Cristóvão', 25),
-- Tocantins
('Palmas', 26),
('Araguaína', 26),
('Guaraí', 26),
('Paraíso do Tocantins', 26),
('Porto Nacional', 26);

insert into sexo (sexo) values 
('Masculino'),
('Feminino'),
('Outro');

insert into nacionalidade (nacionalidade) values 
('Brasileira'),
('Estrangeira');

-- Inserção das raças
insert into raca (raca) values 
('Branca'),
('Parda'),
('Preta'),
('Amarela'),
('Indígena');

insert into escolaridade (escolaridade) values 
('Ensino Fundamental Incompleto'),
('Ensino Fundamental Completo'),
('Ensino Médio Incompleto'),
('Ensino Médio Completo'),
('Ensino Superior Incompleto'),
('Ensino Superior Completo'),
('Pós-Graduação'),
('Mestrado/Doutorado');

insert into clientes (cpf, nome, rg, id_cidade, id_sexo, id_nacionalidade, fone, id_raca, id_escolaridade) values
('12345678901', 'Ana Silva', '123456789', 1, 2, 1, '11987654321', 1, 6),
('12345678902', 'Carlos Souza', '234567890', 2, 1, 1, '11976543210', 2, 5),
('12345678903', 'Fernanda Costa', '345678901', 3, 2, 2, '11965432109', 3, 4),
('12345678904', 'João Pereira', '456789012', 4, 1, 1, '11954321098', 4, 7),
('12345678905', 'Maria Oliveira', '567890123', 5, 2, 1, '11943210987', 5, 8),
('12345678906', 'Pedro Santos', '678901234', 6, 1, 2, '11932109876', 1, 5),
('12345678907', 'Lucas Almeida', '789012345', 7, 1, 2, '11921098765', 2, 4),
('12345678908', 'Juliana Fernandes', '890123456', 8, 2, 1, '11910987654', 3, 6),
('12345678909', 'Ricardo Lima', '901234567', 9, 1, 2, '11909876543', 4, 7),
('12345678910', 'Tatiane Rodrigues', '012345678', 10, 2, 1, '11998765432', 5, 8),
('12345678911', 'Marcos Pereira', '123450987', 11, 1, 2, '11987654321', 1, 6),
('12345678912', 'Raquel Martins', '234561098', 12, 2, 1, '11976543210', 2, 5),
('12345678913', 'Diego Almeida', '345672109', 13, 1, 1, '11965432109', 3, 4),
('12345678914', 'Larissa Castro', '456783210', 14, 2, 2, '11954321098', 4, 7),
('12345678915', 'Vinícius Cardoso', '567894321', 15, 1, 2, '11943210987', 5, 8),
('12345678916', 'Beatriz Rocha', '678905432', 16, 2, 1, '11932109876', 1, 6),
('12345678917', 'Gabriel Araújo', '789016543', 17, 1, 2, '11921098765', 2, 5),
('12345678918', 'Sofia Lima', '890127654', 18, 2, 1, '11910987654', 3, 4),
('12345678919', 'Rafael Martins', '901238765', 19, 1, 2, '11909876543', 4, 7),
('12345678920', 'Isabela Santos', '012349876', 20, 2, 1, '11998765432', 5, 8),
('12345678921', 'Alice Martins', '234567890', 21, 2, 1, '11987654322', 1, 5),
('12345678922', 'Bruno Oliveira', '345678901', 22, 1, 1, '11976543221', 2, 4),
('12345678923', 'Carla Souza', '456789012', 23, 2, 2, '11965432120', 3, 6),
('12345678924', 'Daniela Costa', '567890123', 24, 1, 1, '11954321087', 4, 7),
('12345678925', 'Eduardo Lima', '678901234', 25, 2, 2, '11943210976', 5, 8),
('12345678926', 'Fabiana Almeida', '789012345', 26, 1, 1, '11932109865', 1, 6),
('12345678927', 'Gustavo Fernandes', '890123456', 27, 2, 1, '11921098754', 2, 5),
('12345678928', 'Heloísa Rodrigues', '901234567', 28, 1, 2, '11910987643', 3, 4),
('12345678929', 'Igor Castro', '012345678', 29, 2, 1, '11909876532', 4, 6),
('12345678930', 'Juliana Lima', '123456789', 30, 1, 2, '11998765421', 5, 7),
('12345678931', 'Kleber Santos', '234567890', 31, 2, 1, '11987654320', 1, 8),
('12345678932', 'Larissa Silva', '345678901', 32, 1, 2, '11976543210', 2, 5),
('12345678933', 'Marcelo Costa', '456789012', 33, 2, 1, '11965432109', 3, 4),
('12345678934', 'Nathalia Rocha', '567890123', 34, 1, 2, '11954321098', 4, 7),
('12345678935', 'Otávio Almeida', '678901234', 35, 2, 1, '11943210987', 5, 8),
('12345678936', 'Patrícia Fernandes', '789012345', 36, 1, 2, '11932109876', 1, 6),
('12345678937', 'Quiteria Souza', '890123456', 37, 2, 2, '11921098765', 2, 5),
('12345678938', 'Rogério Lima', '901234567', 38, 1, 1, '11910987654', 3, 4),
('12345678939', 'Sabrina Silva', '012345678', 39, 2, 2, '11909876543', 4, 7),
('12345678940', 'Thiago Santos', '123456789', 40, 1, 1, '11998765432', 5, 8),
('12345678941', 'Ursula Rodrigues', '234567890', 41, 2, 1, '11987654321', 1, 6),
('12345678942', 'Amanda Silva', '987654321', 42, 1, 1, '11987654322', 2, 5),
('12345678943', 'Felipe Costa', '876543210', 43, 2, 2, '11976543221', 3, 6),
('12345678944', 'Gabriela Santos', '765432109', 44, 1, 1, '11965432120', 4, 7),
('12345678945', 'Henrique Lima', '654321098', 45, 2, 2, '11954321087', 5, 8),
('12345678946', 'Irene Almeida', '543210987', 46, 1, 1, '11943210976', 1, 6),
('12345678947', 'Júlio Fernandes', '432109876', 47, 2, 1, '11932109865', 2, 5),
('12345678948', 'Karen Oliveira', '321098765', 48, 1, 2, '11921098754', 3, 4),
('12345678949', 'Leonardo Rodrigues', '210987654', 49, 2, 2, '11910987643', 4, 6),
('12345678950', 'Marcela Castro', '109876543', 50, 1, 1, '11909876532', 5, 7),
('12345678951', 'Nicolas Silva', '098765432', 51, 2, 1, '11998765421', 1, 8),
('12345678952', 'Olga Lima', '987654321', 52, 1, 2, '11987654320', 2, 5),
('12345678953', 'Paula Martins', '876543210', 53, 2, 2, '11976543210', 3, 6),
('12345678954', 'Quintino Souza', '765432109', 54, 1, 1, '11965432109', 4, 7),
('12345678955', 'Roberta Cardoso', '654321098', 55, 2, 2, '11954321098', 5, 8),
('12345678956', 'Sérgio Almeida', '543210987', 56, 1, 1, '11943210987', 1, 6),
('12345678957', 'Tatiane Rocha', '432109876', 57, 2, 1, '11932109876', 2, 5),
('12345678958', 'Ulysses Lima', '321098765', 58, 1, 2, '11921098765', 3, 4),
('12345678959', 'Viviane Souza', '210987654', 59, 2, 2, '11910987654', 4, 6),
('12345678960', 'Walter Fernandes', '109876543', 60, 1, 1, '11909876543', 5, 7);

-- 1.
update cidade set cidade="Abaixo de M" where cidade >= "A%" and cidade <= "M%";
update cidade set cidade="Acima de M" where cidade > "M%";
select cidade.cidade from clientes join cidade on clientes.id_cidade = cidade.id_cidade;

-- 2.
update cidade, estado set cidade="Centro Oeste" where estado = "Mato Grosso do Sul";
select cidade.cidade, estado.estado from cidade join estado on cidade.id_estado = estado.id_estado;

-- 3.
update nacionalidade set nacionalidade="Fora do Brasil" where nacionalidade = "Estrangeira";
select nacionalidade.nacionalidade from clientes join nacionalidade on clientes.id_nacionalidade = nacionalidade.id_nacionalidade;

-- 4.
update raca set raca="Seres Humanos";
select raca.raca from clientes join raca on clientes.id_raca = raca.id_raca; 

-- 5.
update escolaridade set escolaridade="Ensino Avançado" where escolaridade = "Ensino Médio Completo";
select escolaridade.escolaridade from clientes join escolaridade on clientes.id_escolaridade = escolaridade.id_escolaridade;
