# Project:Log Analysis 
We are building a reporting tool that prints out reports based on data in database.The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, this code will answer questions about the site's user activity.

## What this code finds out ??
  - What are the most popular three articles of all time?
  - Who are the most popular article authors of all time?
  - On which days did more than 1% of requests lead to errors?

## Views used!

  -   #### View 1 - articleviews
 ` create view articleviews as select (select replace ( path , '/article/' , '' ) as articlename),count(*) as viewcount from log where status like '2%' and path not like '/' group by path order by viewcount desc; `

> This view extracts all the articles viewed and the number of views each article got arranged in descending order

-   #### View 2 - summary
` create view summary as select a.articlename,a.viewcount,b.author as authorid,c.name as author from articleviews as a,articles as b,authors as c where a.articlename = b.slug and c.id=b.author; `
> This view returns a table where each article is listed with its views author name and author id

-   #### View 3 - requestsperdate
` create view requestsperdate as select count(*) as totalrequests,date(time) as date from log group by date; `
>This view gives how many users visited the website each day.

-   #### View 4 - errorsperdate
` create view errorsperdate as select count(*) as errorcount,date(time) as date from log where status like '4%' group by date; `
>Tells the error requests made each day.

-   #### View 5 - errorsearch
` create view errorsearch as select r.date,(select trunc((e.errorcount::decimal/r.totalrequests*100),1) as errorratio) from requestsperdate as r,errorsperdate as e where e.date=r.date; `
>Tells the error to total request ratio per day.

## How to use this ?
This is a simple python code so all you need to do is copy the code to the same location as your database. Run the command

` $ python3 projectlog.py `

