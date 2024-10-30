drop database if exists teste_trigger;
create database if not exists teste_trigger;
use teste_trigger;
 
create table estado(
id_estado int auto_increment primary key,
nome varchar (50) not null
);
 
create table cidade(
id_cidade int auto_increment primary key,
nome varchar (50) not null,
id_estado int,
foreign key (id_estado) references estado (id_estado)
);
 
create table genero(
id_gen int auto_increment primary key,
tipo enum("Masculino","Feminino","Outro") not null
);
 
create table raca(
id_raca int auto_increment primary key,
tipo enum("Branco","Negro","Amarelo","Indígena") not null
);
 
create table religiao(
id_religiao int auto_increment primary key,
tipo enum("Protestante","Católico","Islâmico","Budismo","Umbanda","Judeu") not null
);
 
create table agencia(
numero_da_agencia int auto_increment primary key,
endereco varchar(100) not null,
id_cidade int,
id_estado int,
foreign key (id_cidade) references cidade(id_cidade),
foreign key (id_estado) references estado(id_estado)
);
 
create table cliente(
numero_da_conta varchar(15) primary key not null,
cpf varchar(11) not null,
nome varchar(100) not null,
rg varchar(12) not null,
data_de_nascimento date not null,
estado_civil enum("Casado","Solteiro","Separado","Divorciado","Viúvo"),
religiao int,
genero int,
saldo float,
numero_da_agencia int,
id_cidade int,
id_estado int,
foreign key (religiao) references religiao (id_religiao),
foreign key (genero) references genero(id_gen),
foreign key (id_cidade) references cidade(id_cidade),
foreign key (id_estado) references estado(id_estado),
foreign key (numero_da_agencia) references agencia (numero_da_agencia)
);
 
create table saque(
id_operecao int auto_increment primary key,
id_agencia int,
id_conta_cliente varchar(15),
valor_saque float,
foreign key (id_agencia) references agencia(numero_da_agencia),
foreign key (id_conta_cliente) references cliente(numero_da_conta)
);
 
create table deposito(
id_operecao int auto_increment primary key,
id_agencia int,
id_conta_cliente varchar(15),
valor_deposito float,
foreign key (id_agencia) references agencia(numero_da_agencia),
foreign key (id_conta_cliente) references cliente(numero_da_conta)
);

select * from cliente;

DELIMITER %
create trigger tgg_sub_cliente after insert on saque
for each row
begin
    declare saldo_atual float;
    select saldo into saldo_atual from cliente where numero_da_conta = new.id_conta_cliente;

    if saldo_atual >= new.valor_saque then
        update cliente 
        set saldo = saldo - new.valor_saque where numero_da_conta = new.id_conta_cliente;
    else
        signal sqlstate '45000' set message_text = 'Saldo insuficiente';
    end if;
end %

DELIMITER %
create trigger tgg_deposito after insert on deposito
for each row
begin
    update cliente 
    set saldo = saldo + new.valor_deposito where numero_da_conta = new.id_conta_cliente;
end %

-- Inserindo estados
INSERT INTO estado (nome) VALUES ('São Paulo'), ('Rio de Janeiro'), ('Minas Gerais');

-- Inserindo cidades
INSERT INTO cidade (nome, id_estado) VALUES 
('São Paulo', 1), 
('Rio de Janeiro', 2), 
('Belo Horizonte', 3);

-- Inserindo gêneros
INSERT INTO genero (tipo) VALUES ('Masculino'), ('Feminino'), ('Outro');

-- Inserindo raças
INSERT INTO raca (tipo) VALUES ('Branco'), ('Negro'), ('Amarelo'), ('Indígena');

-- Inserindo religiões
INSERT INTO religiao (tipo) VALUES ('Protestante'), ('Católico'), ('Islâmico'), ('Budismo'), ('Umbanda'), ('Judeu');

-- Inserindo agências
INSERT INTO agencia (endereco, id_cidade, id_estado) VALUES 
('Avenida Paulista, 1000', 1, 1), 
('Rua da Praia, 50', 2, 2), 
('Avenida Afonso Pena, 200', 3, 3);

-- Inserindo clientes
INSERT INTO cliente (numero_da_conta, cpf, nome, rg, data_de_nascimento, estado_civil, religiao, genero, saldo, numero_da_agencia, id_cidade, id_estado) VALUES 
('123456789', '12345678901', 'João Silva', 'MG1234567', '1990-01-01', 'Solteiro', 2, 1, 1000.50, 1, 1, 1),
('987654321', '98765432100', 'Maria Oliveira', 'MG7654321', '1985-05-05', 'Casado', 1, 2, 2000.75, 2, 2, 2);

-- Inserindo saques
INSERT INTO saque (id_agencia, id_conta_cliente, valor_saque) VALUES 
(1, '123456789', 100.00), 
(2, '987654321', 150.00);

-- Inserindo depósitos
INSERT INTO deposito (id_agencia, id_conta_cliente, valor_deposito) VALUES 
(1, '123456789', 250.00), 
(2, '987654321', 300.00);

select * from cliente;


