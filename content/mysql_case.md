Title: MySQL Case
Date:  2009-04-11 10:35:23
Category: Archive
Tags: MySQL

I was in the midst of developing a system to track OTIF (On Time In Full)  deliveries to my employer's customers.  I 
wanted to be able to take the data and use it with a nice open source sparkline tool found [here](http://sparkline.org/).

To do that though, I needed to be able to convert the data into a binary setting - either we met the OTIF goal fot the 
delivery, or we didn't.  Luckily, I found out about [MySQL Reference - Case Statement](http://dev.mysql.com/doc/refman/5.0/en/case-statement.html).

Before I go over the case statement function, let's build a table in MySQL and populate it with some data.  The table 
will be similar to the table I used with the above problem:

Table Name: otif_data

| ID  |   Customer ID  |  Quantity Ordered  |  Quantity Shipped  |  Date Due  |  Date Shipped

Okay, now that we have our table built, I'll let you go ahead and populate some data.  For illustrative purposes, I'll 
put a couple of rows here so you get the idea:

| ID  |   Customer ID        |  Quantity Ordered  |  Quantity Shipped  |  Date Due  |  Date Shipped  |
| --- |  -------------       |  :--------------:  |  :---------------: |  --------  |  ------------  |
|  1  |  Alpha Pakages       |      10,000        |       9,000        | 2008-04-20 |  2008-04-21    |
|  2  |  Jingle Jangle's     |      20,000        |      20,000        | 2008-04-21 |  2008-04-18    |
|  3  |  Ying's Pottery Barn |      15,000        |      15,000        | 2008-04-22 |  2008-04-30    |

Okay, now for the real fun.  MySQL's case statement works just like an if statement in any programming language.  Let's
look at the code required to test for how many customers we have shipped orders to on time:

On Time Query
#############

SELECT SUM(CASE


Update 10/28/2018:  I believe this was an incomplete tutorial I had in WordPress.  I leave it posted here because I will likely 
come back and clean it up.