create table if not exists test.salary(
	tran_id int primary key,
	person_id int 
	salary decimal(12,2)
);

create table not exists test.person(
	person_id int primary key,
	name varchar(512),
	school varchar(512),
	major varchar(512)
);