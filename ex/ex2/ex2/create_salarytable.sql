create schema if not exists ex2;

create table if not exists ex2.salary(
	tran_id int primary key,
	person_id int, 
	salary decimal(12,2)
);

create table if not exists ex2.person(
	person_id int primary key,
	name varchar(512),
	school varchar(512),
	major varchar(512)
);