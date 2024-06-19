drop database if exists hospital;
create database hospital;
use hospital;


create table departments (
    id tinyint unsigned primary key auto_increment,
    name varchar(100) not null unique,
    
    -- явное указание имени объекта ограничения
    -- constraint departments_not_empty_name check (name <> "")
    
    -- автоматическое создание имени объекта ограничения
    check (name <> "")
);

create table wards (
    id smallint unsigned primary key auto_increment,
    name varchar(10) not null unique,
    dep_id tinyint unsigned not null,
    check (name <> "")
);

create table specializations (
    id tinyint unsigned primary key auto_increment,
    name varchar(120) not null unique,
    check (name <> "")
);

create table doctors (
    id smallint unsigned primary key auto_increment,
    dep_id tinyint unsigned not null,
    last_name varchar(100) not null,
    first_name varchar(100) not null,
    patr_name varchar(100) not null,
    -- от -999,999.99 до 999,999.99
    salary decimal(8,2) not null,
    premium decimal(8,2) not null default 0,
    check (last_name <> ""),
    check (first_name <> ""),
    check (patr_name <> ""),
    check (salary > 0),
    check (premium >= 0)
);

create table doctors_specs (
    doctor_id smallint unsigned not null,
    spec_id tinyint unsigned not null,
    primary key (doctor_id, spec_id)
);

-- +-----------+---------+
-- | doctor_id | spec_id |
-- +-----------+---------+
-- |     1     |    1    |
-- |     1     |    2    |
-- |     2     |    1    |
-- |     3     |    3    |
-- .......................
-- +-----------+---------+

create table vacations (
    id mediumint unsigned primary key auto_increment,
    doctor_id smallint unsigned not null,
    start_date date not null,
    end_date date not null,
    check (start_date < end_date)
);

create table sponsors (
    id smallint unsigned primary key auto_increment,
    name varchar(250) not null unique,
    check (name <> "")
);

create table donations (
    id mediumint unsigned primary key auto_increment,
    sponsor_id smallint unsigned not null,
    dep_id tinyint unsigned not null,
    date date not null default (curdate()),
    -- от -999,999,999.99 до 999,999,999.99
    amount decimal(11,2) not null,
    check (amount > 0)
    -- невозможно в MySQL
    -- check (date <= curdate())
);


delimiter //
create trigger donations_check_date
before insert on donations for each row
begin
    if new.date > curdate() then
        -- подмена данных на значение по умолчанию для столбца (или иное значение) не всегда допустима
        -- set new.date = curdate();
        
        -- подмена данных на запрещённое для столбца значение прерывает запрос, но вводит в заблуждение
        -- set new.date = null;
        
        -- предпочтительный способ отмены запроса добавления данных
        signal sqlstate '45001'
            set message_text = 'Column \'date\' cannot contain a date that is later than current date';
    end if;
end //
delimiter ;


alter table wards
    add foreign key (dep_id) references departments (id);

alter table doctors_specs
    add foreign key (doctor_id) references doctors (id),
    add foreign key (spec_id) references specializations (id);

alter table vacations
    add foreign key (doctor_id) references doctors (id);

alter table donations
    add foreign key (dep_id) references departments (id),
    add foreign key (sponsor_id) references sponsors (id);

