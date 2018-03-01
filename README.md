# logs_analysis
To create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Tables
this project has three tables in database. These are
* The **authors** table includes information about the authors of articles.
* The **articles** table includes the articles themselves.
* The **log** table includes one entry for each time a user has accessed the site.

## steps to run the program
* Make sure you have postgressql installed and configured.
* use pip install psycopg2
* If not then you will need to install the virtual machine:
  This will give you the PostgreSQL database and support software needed for this project.
* To bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.
* To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
* clone the repository
* create views before run the code in command line. View code is given below.
* run the python code using "python log_analysis.py" command in command line.

## Views
I used two view in the third query. One to count the total number of requests on days
and second to count error requests on days.

**View 1: allrequest**

```
create view allrequest as
select time ::date, count(*) as requests
from log
group by time ::date;
```

**View 2: errors**

```
create view errors as
select time ::date, count(*) as err
from log
where status != '200 OK'
group by time ::date;
```
