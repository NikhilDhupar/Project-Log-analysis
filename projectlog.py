# database code for project log analysis
import psycopg2
from datetime import datetime

db = psycopg2.connect("dbname=news")
c = db.cursor()

# task 1
c.execute(
    "select articlename,viewcount from articleviews order by viewcount desc limit 3;")
ans = c.fetchall()
print("Listing top 3 articles")
for i in ans:
    print("\"", i[0], "\" -", i[1], "views")
# task 2
c.execute("select author,sum(viewcount) as totalviews from summary group by author order by totalviews desc;")
ans = c.fetchall()
print("\nListing top authors of all time")
for i in ans:
    print("\"", i[0], "\" -", i[1], "views")
# task 3
print("\nOn which day did more than 1% requests lead to error")
c.execute("select * from errorsearch where errorratio>1 order by errorratio desc;")
ans = c.fetchall()
for i in ans:
    date = ans[0][0]
    errorratio = ans[0][1]
    date = datetime.strftime(date, '%b %d, %Y')
    print(date, " - ", errorratio, "%errors")
db.close()
