# IST769 Lab E
## SQL Over Anything with Apache Drill

In this lab, we will explore the power of Apache Drill for ad-hoc SQL query over your data. Drill data can be stored in a variety of places and in a variety of formats. 

## Outcomes

At the end of this lab you should be able to:

- Query data from a variety of sources with SQL
- Handle Structured and Semi-structured data with Drill


## Setup

1. Open the terminal window in your `ist769` folder.
1. Change the current working directory to `docker/drill`:  
`ist769$ cd docker/drill`
1. Bring up the Drill environment:  
`drill$ docker-compose up -d`
1. Make sure the 3 containers in this setup are running. `jupyter`, `minio` and `drill`:  
`drill$ docker-compose ps`
1. Get the URL with access token for jupyter. It will be a url in the jupyter logs:  
`drill$ docker-compose logs jupyter`
1. Log-in to the drill Web UI https://localhost:8047 
1. Login to the Minio Web UI https://localhost:9001 


## Exercises

Feel free to work with a partner on this lab. The best way to explore the power of Drill is to use it on data that interests you! In this lab you will do just that. 

First you are tasked with finding two datasets to analyze. Choose something that interests you and consider the types of questions you would like to ask of the data. Two places where you can find data sets of interest are:

- [https://github.com/awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets)
- [https://www.kaggle.com/datasets](https://www.kaggle.com/datasets)

The only constraints are:

- No Excel file datasets
- One dataset must be in JSON or XML format.
- You must load your datasets into your minio server

Drill should be able to work with large datasets quite easily. In my testing I used a 100MB json file.

### Questions

**Q1.** For dataset one, please provide the following:
  - URL to the source of this dataset
  - The file format for this dataset (JSON, XML,  CSV, TSV, Parquet, Avro, etc...)
  - What is this dataset all about? 
  - What types of columns / attributes are available in this dataset?
  - The first question you'd like to answer for your dataset.
  - The second question you'd like to answer for your dataset.

For example (you are not allowed to use this dataset):
  - https://www.kaggle.com/zynicide/wine-reviews/
  - JSON file
  - Wine Reviews from WinEnthusiast Magazine
  - Columns points, wine title, description, taster name, taster twitter, designation, variety, region 1, province, country, winders price, region2
  - Question 1: Whare the the most varietals reviewed?
  - Question 2: What are the highest rated (points) with the lowest prices?


**Q1.** For dataset two, repeat this process:
  - URL to the source of this dataset
  - The file format for this dataset (JSON, XML,  CSV, TSV, Parquet, Avro, etc...)
  - What is this dataset all about? 
  - What types of columns / attributes are available in this dataset?
  - The first question you'd like to answer for your dataset.
  - The second question you'd like to answer for your dataset.

**Q3.** What is the answer to your **Q1 First Question**? Write a drill SQL query to answer the question and provide a screenshot of the query and output. Most importantly expalin how or why this answers the question.

**Q4.** What is the answer to your **Q1 Second Question**? Write a drill SQL query to answer the question and provide a screenshot of the query and output. Most importantly expalin how or why this answers the question.

**Q5.** What is the answer to your **Q2 First Question**? Write a drill SQL query to answer the question and provide a screenshot of the query and output. Most importantly expalin how or why this answers the question.

**Q6.** What is the answer to your **Q2 Second Question**? Write a drill SQL query to answer the question and provide a screenshot of the query and output. Most importantly expalin how or why this answers the question.
