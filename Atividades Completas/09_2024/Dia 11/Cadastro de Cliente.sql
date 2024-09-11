drop database if exists ATV_CADASTRO;
create database ATV_CADASTRO;
use ATV_CADASTRO;

create table CADASTRO_CLIENTES (
    idcliente int auto_increment primary key,
    nome varchar(150) not null,
    regime_tributacao enum('Pessoa Fisica', 'Pessoa Juridica', 'Estrangeiro') not null,
    email varchar(150) not null,
    email_danfe varchar(150) not null,
    email_cobranca varchar(150) not null,
    email_lojavirtual varchar(150) not null,
    tel_comercial varchar(50) not null,
    tel_residencial varchar(50),
    tel_celular varchar(50) not null,
    ramal varchar(100),
    fax varchar(100),
    cpf char(11) not null,
    rg char(14),
    situa_icms enum('Ativo', 'Inativo', 'Isento', 'Suspenso'),
    insc_estadual varchar(100),
    insc_suframa varchar(100),
    sexo enum('Masculino', 'Feminino', 'Outro'),
    data_nasc date not null,
    transportadora1 varchar(150),
    transportadora2 varchar(150),
    tabela_preco enum('Tabela Padrão', 'Loja Virtual', 'Promoções', 'Atacado'),
    mod_frete_padrao enum('CIF', 'FOB', 'Frete Grátis'),
    sit_cadastro enum('Aguardando Aprovação', 'Aprovado', 'Rejeitado'),
    linha_pefclinte varchar(100),
    aliquota float,
    icms_st boolean,
    tbm_fornecedor boolean,
    enviar_email_cadastro boolean,
    enviar_email_sitcadastral boolean
);

create table ORDEM_SERVICO (
	idcliente int,
    documento varchar(50),
    emissao date,
    cliente varchar(100),
    precisao date,
    descricao varchar(50) primary key,
    execucao varchar(50),
    servico varchar(50),
    variante varchar(30),
    qtde int,
    valor float,
    foreign key (idcliente) references CADASTRO_CLIENTES(idcliente)
);

create table PECAS (
    descricao varchar(50) primary key,
    variante varchar(50),
    preco_venda float,
    cod int,
    qtde_base int,
    qtde int,
    uni_medida varchar(20),
    custo_uni float,
    custo_total float,
    qtde_fixa_variavel int,
    ordem varchar(50),
    origem varchar(50),
    status_ enum('Disponível', 'Indisponível', 'Em Produção', 'Descontinuado')
);

create table NOTA_FISCAL (
    idcliente int,
    descricao varchar(50),
    docto varchar(50) primary key unique,
    sequencia int,
    emissao date not null,
    vencimento date,
    prev_faturamento date,
    aprov_cliente date,
    aprov_hora time,
    embarques int,
    prazo_entrega int,
    num_pedido_compra int,
    vendedor varchar(100),
    historico varchar(100),
    faturamentos int,
    cliente varchar(100),
    endereco_entrega varchar(100),
    tabela_preco varchar(50),
    transportadora1 varchar(150),
    transportadora2 varchar(150),
    tipo_frete enum('CIF', 'FOB', 'Frete Grátis', 'Sem Frete'),
    valor_frete float,
    porcem float,
    valor_desconto_rateado float,
    contato enum('Vendedor', 'Comprador', 'Cliente', 'Outro'),
    foreign key (idcliente) references CADASTRO_CLIENTES(idcliente),
    foreign key (descricao) references PECAS(descricao)
);

--
insert into CADASTRO_CLIENTES (nome, regime_tributacao, email, email_danfe, email_cobranca, email_lojavirtual, tel_comercial, tel_celular, cpf, data_nasc)
values 
('John Doe', 'Pessoa Fisica', 'john@example.com', 'danfe@example.com', 'cobranca@example.com', 'lojavirtual@example.com', '1234567890', '0987654321', '12345678901', '1980-01-01'),
('Jane Smith', 'Pessoa Juridica', 'jane@example.com', 'danfe@example.com', 'cobranca@example.com', 'lojavirtual@example.com', '2345678901', '10987654321', '23456789012', '1990-02-02');

update CADASTRO_CLIENTES set tel_comercial = '1111111111' where idcliente = 1;
select * from CADASTRO_CLIENTES;
delete from CADASTRO_CLIENTES where idcliente = 2;

--
insert into PECAS (descricao, variante, preco_venda, cod, qtde_base, qtde, uni_medida, custo_uni, custo_total, qtde_fixa_variavel, ordem, origem, status_)
values 
('Peca A', 'Variante 1', 100.00, 1, 10, 20, 'Unidade', 50.00, 1000.00, 5, 'Ordem 1', 'Origem 1', 'Disponível'),
('Peca B', 'Variante 2', 150.00, 2, 15, 30, 'Unidade', 75.00, 2250.00, 10, 'Ordem 2', 'Origem 2', 'Em Produção');

update PECAS set preco_venda = 120.00 where descricao = 'Peca A';
select * from PECAS;
delete from PECAS where descricao = 'Peca B';

--
insert into ORDEM_SERVICO (idcliente, documento, emissao, cliente, precisao, descricao, execucao, servico, variante, qtde, valor)
values 
(1, 'DOC001', '2024-09-10', 'John Doe', '2024-09-15', 'Peca C', 'Execução 1', 'Serviço X', 'Variante 3', 5, 1000.00);

update ORDEM_SERVICO set valor = 150.00 where documento = 'doc001' and descricao = 'Peca A';
delete from ORDEM_SERVICO where documento = 'doc001' AND descricao = 'Peca A';
select * from ORDEM_SERVICO;

-- 
insert into NOTA_FISCAL (docto, sequencia, emissao, vencimento, prev_faturamento, aprov_cliente, aprov_hora, embarques, prazo_entrega, num_pedido_compra,
 vendedor, historico, faturamentos, cliente, endereco_entrega, tabela_preco, transportadora1, transportadora2, tipo_frete, valor_frete, porcem, valor_desconto_rateado, contato, idcliente, descricao)
values 
('NFP001', 1, '2024-09-01', '2024-09-30', '2024-09-15', '2024-09-05', '12:00:00', 2, 5, 1001, 'Vendedor A', 'Venda de peças', 1, 
 'John Doe', 'Rua A, 123', 'Tabela Padrão', 'Transportadora X', 'Transportadora Y', 'CIF', 50.00, 5.00, 10.00, 'Vendedor', 1, 'Peca A');

update NOTA_FISCAL set valor_frete = 60.00 where docto = 'NFP001';
select * from NOTA_FISCAL;
delete from NOTA_FISCAL where docto = 'NFP001';