# IST769 Lab B
## Hadoop

In this lab we will learn about Hadoop, data processing and storage system for big data.

## Outcomes

At the end of this lab you should be able to:

- load data into HDFS at the command line,
- create internal and external Hive tables,
- Perform basic CRUD operations with HBase
- Use HCatalog to integrate Hbase and Hive


## Setup

NOTE: The Hadoop Docker container only runs in Hyper-V mode on windows. Your instructor should have helped you with this or provided a separate cloud instance of Hadoop for you to use in this lab.

- Open the command line in your `ist769` folder.
- To start Cloudera Hadoop, from the command line change into the hadoop folder:  
`ist769$ cd docker/hadoop`
- Start the container:  
`hadoop$ docker-compose up -d`
- It take a while for this container to start. You'll know its ready when you see the Impala server has started in the logs:  
`hadoop$ docker-compose logs`
- Repeat the previous command until you see:  
`cloudera  | Started Impala Server (impalad):               [  OK  ]`  
NOTE: Please wait until the container is up and running before proceeding.
- There are 2 methods of accessing Cloudera Hadoop. The command line and the Hue (Hadoop User Experience) web application.
- To access the command line, type:  
`hadoop$ docker-compose exec cloudera bash -c "su -l cloudera"`  
This command executes the command to login as user clouders and return you to a command line inside the running container.   
Your command prompt will now read:  
`[cloudera@quickstart ~]$`
- To access Hue, open a browser and visit http://localhost:8080 in th address bar. login as user `cloudera` with password `cloudera`


## Accessing the Hadoop tools From the Cloudera command line

Consider this section reference. It show how to connect to the various hadoop tools.

### Connecting to Hive
- To access hive, type:  
`[cloudera@quickstart ~]$ beeline -u jdbc:hive2://localhost:10000/default -u cloudera -p cloudera –silent=true`
- You will now see the hive2 prompt, where you can type Hive Query Language (HQL):  
`jdbc:hive2://localhost:10000/default>`
- To exit Hive, type:  
`jdbc:hive2://localhost:10000/default> !quit`


### Connecting to Hbase

- To access Hbase, type:  
`[cloudera@quickstart ~]$ hbase shell`
- You will now see the Hbase prompt, where you can type Hbase commands:  
`hbase(main):001:0>`
- To exit Hbase, type:  
`beeline> quit`

### Connecting to Impala

- To access Impala, type:  
`[cloudera@quickstart ~]$ impala-shell`
- You will now see the Impala prompt, where you can type Impala SQL commands:  
`[quickstart.cloudera:21000] >`
- To exit Impala, type:  
`beeline> quit;`


# Exercises (7 total)

Try to complete the following exercises. Refer to your nodes, and the class lecture video to help you if you get stuck! You will struggle, but also learn a lot as you complete these exercises!

Ex 1. From the `datasets` folder load the `customers/customers.csv`,  `customers/surveys.csv`, and `tweets/tweets.psv` into HDFS. Specifically:  

  | source | HDFS Location |
  | ----- | ----- |
  | `customers/customers.csv` | `/user/cloudera/labc/customers/customers.csv` |
  | `customers/surveys.csv` | `/user/cloudera/labc/surveys/surveys.csv` |
  | `tweets/tweets.psv` | `/user/cloudera/labc/tweets/tweets.psv` |

  Record the commands you entered to complete this task. provide a screenshot of evidence these files are in HDFS.

 Ex 2. Create a Hive database called `labc`. use the database. In `labc` create an external hive table for the `tweets`. Your external table will point to the existing location on HDFS. You will need to view the `tweets.psv` file to see the format of the file in order to correctly setup the fields terminator and columns in the Hive table.  
After you create the table write a query to display all of the tweets for a user you've chosen. Please include all commmands you used to complete the task, and provide a screen shot of the query output and the output of a `describe tweets`.


Ex 3. In the `labc` database, let's create an internal hive table for `customers`. After you create the table, use the `load` command to move the data from the current HDFS location into the Hive data warehouse.   
NOTE 1: if you screw up you will need to `drop table` and reload the file back into HDFS from step 1.  
NOTE 2: there is a header row in this file, you might need to search the Hive docs on the web for how to exclude this first row.   
When you have created the table and imported the data, provde all the commands you entered to complete the task and a `select` statement showing the table output.

Ex 4. Similar to the previous step import the `surveys.csv` into a Hive internal table in the `labc` database called `surveys`.
When you have created the table and imported the data, provde all the commands you entered to complete the task and a `select` statement showing the table output.

Ex 5. Write a Hive QL Query to match a customer to their survey. Make sure to include all columns from customer and survey, and be sure to include customers who did not complete a survey.

Ex 6. Create an Hbase table called `orders` with two column families `order` and `customer`. Add the following data to the table:  

  | Order Date | Order Amount | Order Handling | Customer Email | Customer City | Customer State |
  | ----- | ----- | ----- | ----- | ----- | ----- |
  | 12/5/2021 | 2000 | | joeking@geemail.com  | Syracuse | NY |
  | 12/6/2021 | 1500 | 100 | bettealott@hottemail.com | Buffalo | NY  |
  | 12/6/2021 | 1000 | | maryme@yayhoo.com | Scranton | PA |

  Provide all the commands you entered to complete the task and include a screenshot of a `scan` of the table data as evidence it was entered.

Ex 7. Create a Hive table from the Hbase table. Write a query to total the orders by state. Include all commands you entered to complete the task, and include a screenshot of your query output showing total orders by state.
  















