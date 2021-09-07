# IST769 Lab B
## Docker, git and the command line.

In this lab we will learn about docker, git and the command line, also known as the CLI or Command Line Interface.

## Outcomes

At the end of this lab you should be able to:

- use the command line interface on your computer,
- use simple git commands from the command line,
- identify if you are in the correct git folder,
- start and stop docker lab images,
- determine what docker images are running,
- create and run your own docker application.

## Part 1: Command line interface (CLI) basics

In this section we will learn just enough Command Line Interface to be useful in this course. Everyone should learn the command line. It is by far the simplest method to work with a computer. Yes it's not a pretty as the Operating System's GUI (Graphical User Interface), but is very effective for most tasks, especially several command with different applications. 

In this section we will learn how to how to identify the current folder of the command line and how to switch folders. These commands should work on both Windows and Mac OSX.

1. Open the command line.  
   - On *Windows*, run PowerShell,  
   - On *Mac OS* run Terminal.

2. In your window you should see a **command prompt** the command prompt is where you enter commands. ;-) Also it will let you know the folder on your computer for which you are running the commands.  
   - On *Windows* the PowerShell prompt starts with `PS` and ends with `>`
   - On *Mac OS* the Terminal (zsh) prompt ends with a `%`
   - In most documentation the symbol used for the command prompt is `$`. That way authors do not need to express the command prompt for each Operating System.

3. The command line just waits for us to enter commands.  
   - Click your mouse inside the window to activate it.
   - Press the ENTER/RETURN key a couple of times, and you should see the command prompt repeating.
   - This is because you are entering a command, it is finishing and then prompting you for the next command.
   - EVERY command typed at the command line must end with ENTER/RETURN to activate the command.

4. Let's try our first command. From the command prompt, enter:  
`$ pwd`   
to print the current working directory. This will display your location on the computer's disk.  
**NOTE:** I used the general command prompt of `$`. Do not type this symbol! It is there to explain to you that this is a command you should a the command line within your Operating System.

3. Bad commands! When a command works, the command line interface won't say much about it. When the command doesn't work, you will get an earful. This is by design as the more experienced you get with the command line the less assurances you will required from it.
   - Let's type a bad command, Type ` $ fudge`
   - On *Windows* the PowerShell prompt will output: `the term 'fudge' is not recognized`
   - On *Mac OS* the Terminal (zsh) prompt will output: `zsh: command not found: fudge`
   - Not very helpful, but at least we know something was wrong!

5. Let's open the same disk location within the Operating System GUI (Graphical User Interface) as within the command line.
   - At the *Windows* command prompt, type: `$ start .` this will launch Windows Explorer in the current working directory.
   - At the *Mac OS* command prompt, type: `$ open .` this will launch the Finder app in the current working directory.
**NOTE:** The period `.` refers to the current folder at the command line.

6. In the GUI window, you see a bunch of files and folders. How to do see the same information from the command line?  
   - At the *Windows* command prompt, type: `$ ls`
   - At the *Mac OS* command prompt, type: `$ ls  -l`

7. Lets make a folder then change the current working directory to that new folder.
   - To create a new folder named `ischool` type: `$ mkdir ischool`  
   - Let's Locate the folder we just created. Locate the new folder in the GUI window you opened in the previous step.
   - Let's change the current working directory to the new folder, type: `$ cd ischool`.  
   
8. Your command prompt should now end with `ischool`.
   - The *Windows* PowerShell command prompt looks something like this `PS ....\ischool>`
   - The *Mac OS* command zsh command prompt looks something like this `.... ischool %`
   - Bottom like they both now say `ischool` somewhere in the prompt to let you know the current folder has changed!

9. Let's learn about paths. Commands within this folder now include the folder name in the prompt, for example: `ischool$ ls`.  
   - Let's print the working directory, Type: `ischool$ pwd`
   - The output from the command should have `ischool` as the last folder in the sequence of folders. This sequence is called a **path**, the full path output from `pwd` display how you get from the start of the file system to the current folder.

10. Moving up a folder. The parent folder is a relative path. meaning we don't need to express the full path, we can issue a command relative the current working directory.  
    - To move up a folder, type: `ischool$ cd ..`
    - Notice that's two periods `..`, so one period refers to the current working directory, and two periods refers to the parent directory.
    - If the command works, your prompt should no longer have `ischool` in it.

11. Deleting a folder. Let's clean up and remove that `ischool` folder.
    - Type: `$ rmdir ischool`
    - **NOTE:** You can't remove a folder that is not empty of its your current working directory!

Congratulations! You know enough command line to be dangerous.
## Part 2: Using Git to Clone the lab images

In this part we will use `git` from the command line to copy the lab images code to our computers. We will also learn some basic `git` management which will help us to be successful.

**Git** is a Source Code Management tool (SCM). It allows you to manage changes to code and keep those changes locally and remotely.


1. Cloning. In Git parlance **cloning** means to copy a remote repository locally. The two are then bound by the push / pull operations. To clone IST769, open a terminal window in a folder where you would like the code to live and type:  
`$ git clone https://github.com/mafudge/ist769`  
This will copy the remote code locally into a folder `ist769`. You should see output similar to this:  

```bash
Cloning into 'ist769'...
remote: Enumerating objects: 201, done.
remote: Counting objects: 100% (201/201), done.
remote: Compressing objects: 100% (149/149), done.
remote: Total 201 (delta 48), reused 164 (delta 30), pack-reused 0 receiving objects:  58% (11
Receiving objects: 100% (201/201), 14.42 MiB | 16.89 MiB/s, done.
Resolving deltas: 100% (48/48), done.
```
  
2. How do I know this is a Git repository? Valid question! Type:  
`$ git status`  
You will see this error: 
`fatal: not a git repository (or any of the parent directories): .git`

3. Let's change the working directory. To change the current working directory to the folder of your newly cloned repository, type:  
`$ cd ist769`  

4. Now let's check that git repository status again, type:
`ist769$ git status`  
Your output should say:

```bash
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

5. The anatomy of `git status`. This is an informative command. it will tell you three important things:
    - Which branch your repository is using. In this course, its `main`
    - Whether the code you have locally is the same (up to date) as what is stored remotely. This is called `origin/main` we will learn about `origin` next.
    - Whether or not there is code in your current folder (the working tree) that needs to be committed.

6. Where did this code come from? In Git terminology, this is called the **origin**. To answer this question, type:  
`ist769$ git remote -v`  
The output will have two origin URL's one for fetch (getting updates from the remote) and the other for push (sending local updates remotely).  
In this class, you will need to fetch, but you will never push.  

7. Updating my local to match remote. There will be times in the semester where you will need to update your local git to match the remote. Here are the commands:  
`ist769$ git fetch --all`  to retrieve the updates from the remote
`ist769$ git reset --hard origin/main` to set the files in your working directory to match the files you just fetched from the remote.


More git advice can be found here: [https://mafudge.github.io/ist769/content/A-Intro/git.html](https://mafudge.github.io/ist769/content/A-Intro/git.html)

## Part 3: Docker and the lab images

In this part we will explore how to run the pre-build docker lab images.

First make sure you are in the `ist769` git repository folder that you cloned in the previous step, for details see these videos which explain the process for another course, but the same idea holds here.

- How to open the Windows command prompt inside your git repository folder: [https://www.youtube.com/watch?v=Ze9EmjjHoxU](https://www.youtube.com/watch?v=Ze9EmjjHoxU)
- How to open the OSX terminal inside your git repository folder: https://www.youtube.com/watch?v=4NmcFGngyh0(https://www.youtube.com/watch?v=4NmcFGngyh0)
- Let's learn docker: [https://www.youtube.com/watch?v=fQORO9QEJN4](https://www.youtube.com/watch?v=fQORO9QEJN4)

1. Where are the lab images? The lab images are in the `docker` folder of the `ist769` git repository.
` ist769$ cd docker`
2. Take a look at those folders! If you type:
`docker$ ls`  
You will see a folder for each database. (mongodb, kafka, hadoop, elasticsearch, etc...)

Let's demonstrate how to manage one of these environments in docker. For this example, we will work with the `mongodb` database.

**IMPORTANT NOTE:**

- The `docker-compose` command runs relative to the configuration in the current folder. This configuration is in the `docker-compose.yml` file.
- The `docker` command runs across any configuration. It is useful for working with containers outside the current configuration.

1. Let's work with a single database configuration. First change into the `mongodb` folder.
`docker$ cd mongodb`
2. Most likely, we have not downloaded the images required to run this database. This is typically a one-time deal, but can take a while depending on your internet connection and size of the images.
`mongodb $ docker-compose pull`  
Watch with joy ( or horror!) as files are downloaded to your computer. :-) What it's doing is downloading the images from Docker Hub for running the MongoDb setup I've created for the labs.
3. After the images are downloaded we can build the configuration, again this is a one-time deal:  
`mongodb $ docker-compose build`  
4. Once the configuration is build we can bring up the environment:  
`mongodb$ docker-compose up -d`  
You should see output stating the containers are started.  
**NOTE:** the `-d` option runs the containers in the background, releasing you back to the command line. 
5. To view what's running relative to this configuration, type:  
`mongodb$ docker-compose ps`  
This will output the containers that are running as part of this configuration, and include the exposed TCP ports so you can access the services from your computer.
6. Need to see the logs? Try:  
`mongodb$ docker-compose logs`
7. Too many logs? You can opt to view just one of the service logs (service names are seen with `docker-compose ps`) Type this to see the `drill` service logs:  
`mongodb$ docker-compose logs drill`  
**NOTE:** logs are useful for troubleshooting why a service won't start.

6. To view what running globally (not just this project), type:
`mongodb$ docker ps`  
Unlike docker-compose, this command is not specific to a configuration. This holds true for all docker commands. They can be run anywhere to show information about the entire container environment. 
7. To shutdown the running containers in this configuration, type:  
`mongodb$ docker-compose down`  
This will stop the running containers and destroy them, but the configuration and images remain.
8. Again if you type:  
`mongodb$ docker ps`  you will see no containers running.
9. Need to get rids of all running containers? Try this:  
`$ docker stop $(docker ps -q)` to stop all running containers, then  
`$ docker rm $(docker ps -aq)` to remove any container configurations.

10. We are finished. Let's get back to the `ist769` folder:  
`mongodb$ cd ..`  
`docker$ cd ..`  
Now the command prompt should be `ist769$`. You are ready to start the final part.

## Part 4: Docker on your own

Follow along with this video to really understand docker and how to run any application in it. This will be very helpful in this course!

Let's learn docker: [https://www.youtube.com/watch?v=fQORO9QEJN4](https://www.youtube.com/watch?v=fQORO9QEJN4)

## Questions

1. Explain the difference between the `.` and `..` at the command line? What types of paths are these? full paths or relative paths?
2. Write commands to, create a folder `foo`, change the working directory to that folder, change the working directory back to the parent folder, then delete the folder.
3. Explain the concept of a remote in git. What are the two operations you can perform on a remote?
4. What are the 3 things a `git status` command will tell you about a repository?
5. How do you access the logs of a service `foo` that was started with docker-compose?
7. Explain the difference between an image and a container?
6. What is the purpose of a docker volume?
8. Type a docker command to run an image `foo` in the background with container name `bar` and expose port `1234` externally as `5678`.
9. How many services can you include in a docker-compose file?
10. Create a docker compose file for the run command you did in question 8.

## References

- 5 Minute overview of git: [https://www.youtube.com/watch?v=xvwBtODV0ms](https://www.youtube.com/watch?v=xvwBtODV0ms)
- How to open the Windows command prompt inside your git repository folder: [https://www.youtube.com/watch?v=Ze9EmjjHoxU](https://www.youtube.com/watch?v=Ze9EmjjHoxU)
- How to open the OSX terminal inside your git repository folder: https://www.youtube.com/watch?v=4NmcFGngyh0(https://www.youtube.com/watch?v=4NmcFGngyh0)
- Let's learn docker: [https://www.youtube.com/watch?v=fQORO9QEJN4](https://www.youtube.com/watch?v=fQORO9QEJN4)
