sudo service mysqld start

mysql -uroot -pcloudera

show databases;

create database icp5db;

use icp5db;

create table acad(emp_id INT NOT NULL AUTO_INCREMENT, emp_name VARCHAR(100), emp_sal INT, PRIMARY KEY(emp_id));

insert into acad values(5, "sanam",50000),(6,"opra",60000),(7,"yella",70000);

select * from acad;

sqoop import --connect jdbc:mysql://localhost/icp5db --username root --password cloudera --table acad --m 1;

sqoop export --connect jdbc:mysql://localhost/icp5db --username root --password cloudera --table acad_export --export-dir /user/cloudera/acad/part-m-00000;

select * from acad_export;

CREATE TABLE IF NOT EXISTS employees (
  name         STRING,
  salary       FLOAT,
  subordinates ARRAY<STRING>,
  deductions   MAP<STRING, FLOAT>,
  address      STRUCT<street:STRING, city:STRING, state:STRING, zip:INT>
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\001' 
COLLECTION ITEMS TERMINATED BY '\002' 
MAP KEYS TERMINATED BY '\003'
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;

LOAD DATA LOCAL INPATH '/home/cloudera/Downloads/employees.txt' INTO TABLE employees;

DESCRIBE EXTENDED employees;

DROP TABLE employees;

sqoop export --connect jdbc:mysql://localhost/icp5db --username root --password cloudera --table empNew --export-dir /user/hive/warehouse/emp -m 1;

sqoop import --connect jdbc:mysql://localhost/icp5db --username root --password cloudera --table empNew --hive-import --create-hive-table --hive-table deafult.empNew2 -m 1;

CREATE TABLE IF NOT EXISTS dividends (
date_cal DATE,
value FLOAT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE;

load data local inpath '/home/cloudera/Downloads/dividends.csv' into table dividends;

select * from dividends sort by date-cal limit 2;

sqoop export --connect jdbc:mysql://localhost/icp5db --username root --password cloudera --table dividends --export-dir /user/hive/warehouse/dividends/dividends.csv -m 1;

select year(date_cal), count(year(date_cal)) as "count" from dividends group by year(date_cal);

select year(date_cal), count(year(date_cal)) from dividends group by year(date_cal);

analyze table dividends compute statistics;

select date_cal from dividends where value like '%0.55%';