#!/usr/bin/env python

import psycopg2
from datetime import datetime

db = psycopg2.connect(database = "news")
c = db.cursor()

# 1 st query
print "\nWhat are the most popular three articles of all time? \n"
q1 = """ select title, count( * ) as views
         from articles, log
         where log.path = '/article/' || articles.slug
         group by articles.title
         order by views desc limit 3
     """

c.execute(q1)
result = c.fetchall()

for r in result:
    print r[0] + "-" + str(r[1]) + "views"

#2nd query
print "\n\nWho are the most popular article authors of all time? \n"
q2 = """ select authors.name, count(*) as views 
         from authors, articles, log
         where log.path = '/article/' || articles.slug
         and articles.author=authors.id
         group by authors.name
         order by views  
     """

c.execute(q2)
result = c.fetchall()

for r in result:
    print r[0] + "-" + str(r[1]) + "views"

#3rd query
print "\n\nOn which days did more than 1% of requests lead to errors?\n"

#we used two views in third query

#1st view to get allrequest on days
#view-1
#create view allrequest as
#select time ::date, count(*) as requests
#from log
#group by time ::date;  

#2nd view to get errors on days 
#create view errors as
#select time ::date, count(*) as err
#from log
#where status != '200 OK'
#group by time ::date     

q3 = """ select errors.time, (errors.err*100/allrequest.requests) as percent_err  
         from allrequest, errors
         where (errors.err*100/allrequest.requests)>1 
         and errors.time = allrequest.time  
     """
c.execute(q3)
result = c.fetchall()

for r in result:
    date_input = str(r[0]) 
    date_object = datetime.strptime(date_input, '%Y-%m-%d')
    print (date_object.strftime('%B %d,%Y')) + "-" + str(r[1]) + "% errors"
#we used strftime function to convert date in other format
db.close()