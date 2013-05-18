create table KW_Query (docid varchar(255), term varchar(255), count int, primary key (docid, term));
insert into KW_Query values ('q', 'washington', 1);
insert into KW_Query values ('q', 'taxes', 1);
insert into KW_Query values ('q', 'treasury', 1);
select * from KW_Query;
drop table KW_Query;
