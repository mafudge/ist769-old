# IST769 Lab H
## Key-Value Databases With Redis

In this lab, we will explore Redis, a Key-value database, and so much more! 

## Outcomes

At the end of this lab you should be able to:

- Use Apache Spark to Import and Export data into Redis
- Build Redis Data Structures to solve problems

## Setup

1. Open the terminal window in your `ist769` folder.
1. Change the current working directory to `docker/redis`:  
`ist769$ cd docker/redis`
1. Bring up the environment:  
`redis$ docker-compose up -d`
1. Make sure the 4 containers in this setup are running. `jupyter`,  `redis-commander`, `retwis` and `redis` (the three nodes in the Cassandra ring):  
`redis$ docker-compose ps`
1. Get the URL with access token for jupyter. It will be a url in the jupyter logs:  
`redis$ docker-compose logs jupyter`
1. Log-in Retwis http://localhost:8080 
1. Login to the jupyter Web UI http://localhost:8888 
1. Login to Redis Commander Web UI http://localhost:8081
1. To access the Redis Shell: 
`docker-compose exec redis redis-cli`

## Exercises

For each of the following provide a screenshot as evidence the commands were executed. Include all commands necessary to complete the question including those to add data and display output. Make sure your name or netid appear in the screenshot.

## Questions

**Q1.** Devise a messaging application for spies in Redis. Messages are sent to one spy from another. You can use their emails as keys. Messages expire 60 seconds after created. The key should be whom the message is to. The value should contain whom the message is from and the message itself. Make sure to namespace so you can query all keys in the application.

Send these messages:

| To | From | Message |
|---|---|---|
| bob@us.gov | sue@uk.gov | The sheep sleeps on Tuesdays |
| sue@uk.gov | bob@us.gov | I don't know what that means |
| bob@us.gov | sue@uk.gov | My leg hurts |

**Q2.** Create a Redis data structure to store 2020 and 2021 golden snowball awards for the snowiest city in CNY. https://goldensnowball.com/ You should be able to retrieve the data by a given year for all cities.

|Year|City|Total|
|---|---|---|
| 2020 | Binghamton | 105 |
| 2020 | Buffalo | 78 |
| 2020 | Syracuse | 75 |
| 2020 | Rochester | 100 |
| 2020 | Albany | 65 |
| 2021 | Binghamton | 95 |
| 2021 | Buffalo | 118 |
| 2021 | Syracuse | 125 |
| 2021 | Rochester | 104 |
| 2021 | Albany | 87 |

**Q3.** The Syracuse New York Department of Motor Vehicles has hired you to build a queue management system in Redis. The system needs to manage a single queue of users, by Name. Queued users can be served at one of 4 windows, A,B,C or D. The structure you build in redis should support the queue and be able to display who is waiting in the queue. As people go to the window they should be removed from the queue and assigned to one of the 4 windows. You should be able to display who is at each window at any time. 

Example:

```
Users In queue: Tom, Bill, Bart
Being Served at windows: A: Carl, B: Steve, C: Chuck, D: Dave
```

When Dave is done at the window, Bart is served next:

```
Users In queue: Tom, Bill
Being Served at windows: A: Carl, B: Steve, C: Chuck, D: Bart
```

Mary arrives:
```
Users In queue: Mary, Tom, Bill
Being Served at windows: A: Carl, B: Steve, C: Chuck, D: Bart
```

**Q4.** Use spark to load the exam scores dataset `/home/jovyan/datasets/exam-scores/*.csv` into Redis under the table names `examscores`. Use spark to Demonstrate the data is there by querying it back out.

**Q5.** In Spark SQL get the average exam score by Exam Version. Write the data back out to Redis as `exam_scores_by_version`, finally query the key in redis showing all values in the hash. 