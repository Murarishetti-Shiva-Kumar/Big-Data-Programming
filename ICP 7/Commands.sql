CREATE KEYSPACE icp7 WITH REPLICATION={'class':'SimpleStrategy','replication_factor':3};

desc keyspaces;

use icp7;

create table employee(employee_id int primary key,department text,lastname text,years_with_company int,hiredate date,jobtitle text,salary int,managerid int);

desc table employee;

Copy employee(employee_id,department,lastname,years_with_company,hiredate,jobtitle,salary,managerid) from 'C:\Users\mshiv\Downloads\employee_entries.csv' with HEADER=true;

select * from employee;

select employee_id,lastname,hiredate,jobtitle from employee;

Insert into icp7.employee(employee_id, department,lastname,years_with_company,hiredate,jobtitle,salary,managerid) values (9, 'Engineering', 'Paul',3,'2018-08-23','clerk',50000,3);

select lastname, salary from employee where jobtitle='clerk' allow filtering;

select lastname,jobtitle,salary from employee where hiredate='2000-02-18' allow filtering;

select lastname,salary from employee;

select lastname,salary,managerid from employee where salary=45000 allow filtering;

CREATE CUSTOM INDEX firstname_idx ON employee (lastname) USING 'org.apache.cassandra.index.sasi.SASIIndex' WITH OPTIONS = {'mode': 'PREFIX', 'analyzer_class':'org.apache.cassandra.index.sasi.analyzer.StandardAnalyzer', 'case_sensitive': 'false'};

CREATE FUNCTION IF NOT EXISTS displayname (column TEXT) RETURNS NULL ON NULL INPUT RETURNS text LANGUAGE javascript AS $$ column.charAt(0).toUpperCase() + column.slice(1) $$;

select displayname (lastname) from employee ;

select displayname (lastname) from employee where lastname like 's%';