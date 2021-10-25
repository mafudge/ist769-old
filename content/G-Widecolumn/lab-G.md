# IST769 Lab G
## Wide Column Databases With Cassandra

In this lab, we will explore Apache Cassandra, a wide column database.  

## Outcomes

At the end of this lab you should be able to:

- Use Apache Spark to Import and Export data into Cassandra
- Make tables and query Cassandra tables with CQL
- Create indexes and materialized views to improve queries.


## Setup

1. Open the terminal window in your `ist769` folder.
1. Change the current working directory to `docker/cassandra`:  
`ist769$ cd docker/cassandra`
1. Bring up the environment:  
`cassandra$ docker-compose up -d`
1. Make sure the 6 containers in this setup are running. `jupyter`, `drill`, `cassandra-web`, `cassandra0`, `cassandra1`  and `cassandra2` (the three nodes in the Cassandra ring):  
`cassandra$ docker-compose ps`
1. Get the URL with access token for jupyter. It will be a url in the jupyter logs:  
`cassandra$ docker-compose logs jupyter`
1. Log-in to the drill Web UI http://localhost:8047 
1. Login to the jupyter Web UI http://localhost:8888 
1. Login to the Cassandra Web UI http://localhost:8080
1. To access the Cassandra Shell: 
`docker-compose exec cassandra0 cqlsh`


## Exercises

For each of the following provide a screenshot as evidence the command was executed. If its an index table, or materialized view include a SELECT statement demonstrating it the command is working as expected. Make sure your name or netid appear in the screenshot. 

## The Problem

 Your employer (weather.com) would like you store weather sensor and forecast data. Wventually you will get readings from 2,000 cities worldwide every minute. That's 2.88 million rows each day and 1 billion rows a year. Since the data does not need to be read immediately when written across all nodes, you decide Cassandra is a good choice for this project! This data will be accessible by users so they can get weather information and historical trends for they cities they live in and visit. This should help you figure out how the data will be queried.

**Q1.** You decided to start with a sample data set. The dataset contains 7 days of weather information for major US Cities, with one row being weather information for a single city on a single day. Use Spark to load the dataset `/home/jovyan/datasets/weather/weather.json` use `printSchema()` to inspect the schema. 

**Q2.** Take a look at rows of data in the sample data set. Profile the data to determine what should be used as the partition and cluster key:
 - First: Find the candidate key - which sets of columns are unique for each row?
 - Next: Of those columns in the candidate key - which one makes the most sense for how the data will most likely be queried? 

**Q3.** Using the CQL Shell, write an CQL Query to create a `daily_city_weather` table. Include all columns in the source data set, and make sure to set your partition and cluster keys. Show the CQL query and the output in the screenshot.

**Q4.** Write spark code to load the json dataframe into your cassandra table. Make sure you have the same number of rows in the dataframe and in the cassandra table. This will be your proof that your cassandra row key is correct. Provide spark code to save the data to cassandra and then a screenshot of a select statement and output in the CQL Shell.  

**Q5.** Write a CQL Shell query to get the condition, description and daytime temperatures for "Syracuse, NY" include all dates.

**Q6.** Your company would like to now allow users to find cities where it is not raining on a specific date. For example, they would like a query to show the city and state name, date, condition and description for only those cities where its not raining. Figure out how you can do with an index or materialized view to avoid a costly ALLOW FILTERING operation that asks all nodes for data. Include your CQL to create the index / materialized view and then include a query demonstrating it works.
