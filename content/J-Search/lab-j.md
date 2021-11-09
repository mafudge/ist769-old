# IST769 Lab J
## Search Databases With the Elastic Stack

In this lab, we will explore Elastic search and the Elastic stack. 

## Outcomes

At the end of this lab you should be able to:

- Use Apache Spark to Import and Export data into Elasticsearch
- Query Data with the Kibana query language.
- Build Maps, Canvas and Dashboards in Kibana

## Setup

1. Open the terminal window in your `ist769` folder.
1. Change the current working directory to `docker/elasticsearch`:  
`ist769$ cd docker/elasticsearch`
1. Bring up the environment:  
`elasticsearch$ docker-compose up -d`
1. Make sure the 4 containers in this setup are running. `es01`,`kb01`,`jupyter`, and `drill`:  
`neo4j$ docker-compose ps`
1. Get the URL with access token for jupyter. It will be a url in the jupyter logs:  
`neo4j$ docker-compose logs jupyter`
1. Log-in to Kibana http://localhost:5601
1. Login to the jupyter Web UI http://localhost:8888 

**NOTE:** It takes a while for Elastic to start.... it's a Java app so docker returns UP before it loads completely. Be patient!

## Exercises

For each of the following provide a screenshot as evidence the commands were executed. Include all commands necessary to complete the question including those to add data and display output. Make sure your name or netid appear in the screenshot.

## Questions

**Q1.** Write PySpark to load the 1,600 line weather data set into Elasticsearch under the index `weather` with default index type. 

**Q2.** Use a `curl` command from the command line to hit the Elasticsearch API and demostrate that there are 1,600 documents in the `weather` index. 

**Q3.** Setup a `weather` index pattern in Kibana based on the `weather` index from elasticsearch. MAke sure you have a `geo_point` type and have selected a `@timestamp` field using the date field. Provide a screenshot including the fields in question.

**Q4.** Create a Kibana map displaying the weather locations. Use any layer(s) of data you wish. Provide a screenshot of the map with data points on it. 

**Q5.** Create a Kibana dashboard which when you select a city, will display the average day time and night time temperature for that city, in addition to a line chart of the the average daily high and lows for all data on that city. . Provide a screenshot of the dashboard.

**Q6.** Create a Kibana Canvas! Display at least 2 metrics and 2 charts. Decide which data you want to display and how you would like to present it. Provide a screenshot of the Canvas.
