drop database if exists titanic;
create database if not exists titanic;
use titanic;

create table titanic_base(
PassengerId int primary key,
Survived int,
Pclass int,
Nome varchar(100),
Sex varchar(20),
Age varchar(20),
SibSp int,
Parch int,
Ticket varchar(50),
Fare float,
Cabin varchar(50),
Embarked varchar(10)
);

select * from titanic_base;

# --- Quantos Sobreviveram/Morreram
select count(*) from titanic_base where Survived = 0;
select count(*) from titanic_base where Survived = 1;

# --- Quantas Crianças Abaixo dos 12 Anos Sobreviveram/Morreram
select count(*) from titanic_base where Survived = 0 and age <= 12;
select count(*) from titanic_base where Survived = 1 and age <= 12;

# --- Quantas Mulheres Sobreviveram/Morreram
select count(*) from titanic_base where Survived = 0 and sex = 'female';
select count(*) from titanic_base where Survived = 1 and sex = 'female';

# --- Quantos Homens Sobreviveram/Morreram
select count(*) from titanic_base where Survived = 0 and sex = 'male';
select count(*) from titanic_base where Survived = 1 and sex = 'male';