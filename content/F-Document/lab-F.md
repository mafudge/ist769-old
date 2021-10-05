# IST769 Lab F
## Document Databases With Mongo Db

In this lab, we will explore Mongo Db, a document database.  

## Outcomes

At the end of this lab you should be able to:

- Use Apache Spark to Import and Export data
- CRUD data with Mongo Db Query Language
- Query Mongo Db data with Drill SQL and The Mongo Query Language



## Setup

1. Open the terminal window in your `ist769` folder.
1. Change the current working directory to `docker/mongodb`:  
`ist769$ cd docker/mongodb`
1. Bring up the Drill environment:  
`mongodb$ docker-compose up -d`
1. Make sure the 6 containers in this setup are running. `jupyter`, `drill`, `mongo-client`, `mongo-express`, `mongo` (the Database) and the  `sample-app`:  
`spark$ docker-compose ps`
1. Get the URL with access token for jupyter. It will be a url in the jupyter logs:  
`spark$ docker-compose logs jupyter`
1. Log-in to the drill Web UI http://localhost:8047 
1. Login to the jupyter Web UI http://localhost:8888 
1. Login to the Express Web UI http://localhost:8081
1. The MongoDb Example is at http://localhost:5000/
1. To access the MongoDb Client: 
`docker-compose exec mongo mongo -u admin -p mongopw --authenticationDatabase=admin`


## Exercises

**Q1.** Use Spark to load the dataset `datasets/exam-scores/` into a Spark Dataframe and then the `labf` database under the collection `examscores` Read it back out from MongoDb again, and display a screenshot of your code and the output from the `show()`

**Q2.** Using the Mongo Client, write an MQL Query to display Student Exam score, Class Section, Exam Version, and completion time for those students who completed the exam in under 25 minutes. Sort by exam score with the highest scores first. Show the query and the output in the screenshot.

**Q3.** Re-Write **Q2** using drill. First configure the storage provider, then write the Drill SQL statement equivalent of Q2. include a screenshot of the SQL and output. 

**Q4.** Using the Mongo Client, write an MQL Query to display the execution stats for a query that displays all UFO Signthings in NY. Include a screenshot of the query and the output that displays the number of rows scanned and returned. 

**Q5.**  Using the Mongo Client, create an index to cover the query in Q4, or any query by state for that matter. Provide code to create the index, and a query that uses the index. Prove the query uses the index by displaying the exeuction stats.

**Q6.** Let's explore the power of Drill! Complete the feedback form at http://localhost:5000/ for the following email addresses:
V1 of the form: ccayne@rhyta.com, rovlight@dayrep.com, sladd@superrito.com  
V2 of the form: jcase@dayrep.com, akuss@rhyta.com  
NOTE: Fill in the rest of the fields any way you like.    
Then  a Drill SQL query to get the, Email, First, Last name, Gender from the `/datasets/customers/customers.csv` file and join that to the information from the feedback form in the Mongodb database.  
HINT: Use the `dfs` storage plugin. You may have to configure the file type for this plugin.