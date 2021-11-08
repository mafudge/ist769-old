# IST769 Lab I
## Graph Databases With Neo4j

In this lab, we will explore Neo4j, a Graph database. 

## Outcomes

At the end of this lab you should be able to:

- Use Apache Spark to Import and Export data into Neo4j
- Build Graph Models in Neo4j 
- Write Cipher Queries to retrieve Graph Data 

## Setup

1. Open the terminal window in your `ist769` folder.
1. Change the current working directory to `docker/neo4j`:  
`ist769$ cd docker/neo4j`
1. Bring up the environment:  
`neo4j$ docker-compose up -d`
1. Make sure the 2 containers in this setup are running. `jupyter`,   and `neo4j`:  
`neo4j$ docker-compose ps`
1. Get the URL with access token for jupyter. It will be a url in the jupyter logs:  
`neo4j$ docker-compose logs jupyter`
1. Log-in Neo4j http://localhost:7474 
1. Login to the jupyter Web UI http://localhost:8888 

**NOTE:** It takes a while for Neo4j to start.... it's a Java app so docker returns UP before it loads completely. Be patient!

## Exercises

For each of the following provide a screenshot as evidence the commands were executed. Include all commands necessary to complete the question including those to add data and display output. Make sure your name or netid appear in the screenshot.

## Questions

**Q1.** Using the `:play northwind-graph` command, load the **Product Catalog** nodes and relationships. This should just be a matter of following the commands in the first 3 steps of the Northwind graph. As proof you've completed this correctly, write a Cipher query to display all Products, Suppliers and Categories using both relationships. Your screenshot should include your Cipher code plus the graph output. If you did it correctly there should be 191 nodes and 309 relationships

**Q2.** For contact `Petra Winkler`, write a Cipher query to display the company name, product name and unit price of products that are not discontinued. There should be 6 products displayed in the table.

**Q3.** Write a Cipher query to display a graph of product categories from suppilers in the USA. Make sure the screenshot of your graph emphasizes the product category with more than one supplier.

**Q4.** You just sold 30 units of `laughing lumberjack lager` update the node to reflect the proper stock and display the output.

**Q5.** Using the Movie graph, write a Cipher query to get the Movie title and release date, and Actor name of any actor who played the role of `"Neo"`.  of Load the following data into a Spark dataframe: You just sold 30 units of `laughing lumberjack lager` update the node to reflect the proper stock and display the output.

**Q6** Load all Northind products with category name into a Spark data frame. 