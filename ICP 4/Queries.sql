#Create Hive Tables and Perform Queries for Use Case based on Petrol or hotel_bookings data. For Petrol, see the slides for details or you may try your own queries using hotel_bookings data
create table petrol (distributer_id STRING,distributer_name STRING,amt_IN STRING,amy_OUT STRING,vol_IN INT,vol_OUT INT,year INT) row format delimited fields terminated by ',' stored as textfile;

#Load the data into the table.
load data local inpath '/home/cloudera/Downloads/petrol.txt' into table petrol;

#Fetch all details from table
select * from petrol;

#Amount of petrol sold by each distributor in an year.
SELECT distributer_name,SUM(vol_OUT)  FROM  petrol GROUP  BY distributer_name;

#Top 10 users who sell high amount of petrol
SELECT distributer_id,vol_OUT FROM petrol order by vol_OUT desc limit 10;

#The people who sell least amount of petrol.
SELECT distributer_id,vol_OUT FROM petrol order by vol_OUT limit 10;

#People who sell petrol with a volume difference of more than 500
select distributer_id,year,(vol_IN-vol_OUT) as difference from petrol where (vol_IN-vol_OUT)>500;

#People who sell petrol with a volume difference of more than 400
select distributer_id,year,(vol_IN-vol_OUT) as difference from petrol where (vol_IN-vol_OUT)>400;

#The people who sell least amount of petrol using "cluster by".
select distributer_id,vol_OUT from petrol CLUSTER by vol_OUT;

#The people who sell least amount of petrol using "distribute by".
select distributer_id,vol_OUT from petrol DISTRIBUTE by vol_OUT;

#The people who sell least amount of petrol using "sort by"
SELECT distributer_id,vol_OUT FROM petrol SORT by vol_OUT;

#Create Hive Tables and Perform Queries for Use Case based on Olympics Data
create table olympic(athelete STRING,age INT,country STRING,year STRING,closing STRING,sport STRING,gold INT,silver INT,bronze INT,total INT) row format delimited fields terminated by '\t' stored as textfile;

#Loading the data into the olympics table
load data local inpath '/home/cloudera/Downloads/olympic_data.csv' into table olympic;

#Medals got by all the countries in swimming.
select country,SUM(total) from olympic where sport = "Swimming" GROUP BY country;

#Year wise medals won by India.
select year,SUM(total) from olympic where country = "India" GROUP BY year;

#Medals won by each country.
select country,SUM(total) from olympic GROUP BY country;

#Total gold medals won by each country.
select country,SUM(gold) from olympic GROUP BY country;

#Medals won every year in shooting.
select * from olympic where sport='Shooting' order by year;

#Create Hive Tables and Perform Queries for Use Case based on Movielens dataset which has 3 datasets as movies, users and ratings
#Create 3 tables called movies, ratings and users. Load the data into tables.
#Create table movies.
create table movies(id int, title string,genre string)  row format delimited  fields terminated by ','  stored as textfile;

#loading into movies tables
load data local inpath '/home/cloudera/Downloads/movies.csv' into table movies;

#Create table ratings.
create table ratings(userid int,id int,rating int,timestamp string) row format delimited fields terminated by ',' stored as textfile;

#loading into ratings table
load data local inpath '/home/cloudera/Downloads/ratings.csv' into table ratings;

#Create table users
create table users(userid int,gender string,id int,ratingsgiven int,zip string) row format delimited fields terminated by ',' stored as textfile;

#loading into users table
load data local inpath '/home/cloudera/Downloads/users.txt' into table users;

#List all movies with genre of movie is “Action” and “Drama”
select * from movies where genre like '%Drama%' and genre like '%Action%';

#List movie ids of all movies with rating equal to 5.
select M.id, MR.rating from movies M join ratings MR on (M.id=MR.id) where MR.rating = 5.0;

#Find top 11 average rated "Action" movies with descending order of rating.
select M.title,avg(MR.rating) as a from movies M join ratings MR on (M.id=MR.id) where M.genre like '%Action%' group by M.title order by a desc limit 11;