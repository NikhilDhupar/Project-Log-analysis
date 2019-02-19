#!/usr/bin/env python3
# database code for project log analysis
import psycopg2
import sys
from datetime import datetime
try:
    db = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print("Unable to connect!")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)
else:
    c = db.cursor()
    # task 1
    c.execute(
        "select aname,vcount from aview order by vcount desc limit 3;")
    ans = c.fetchall()
    print("Listing top 3 articles")
    for i in ans:
        print('"{article}" - {count} views'.format(article=i[0], count=i[1]))
    # task 2
    c.execute(
        "select auth,sum(vcount) from final group by auth order by sum desc;")
    ans = c.fetchall()
    print("\nListing top authors of all time")
    for i in ans:
        print('"{author}" - {count} views'.format(author=i[0], count=i[1]))
    # task 3
    print("\nOn which day did more than 1% requests lead to error")
    c.execute(
        "select * from esearch where eratio>1 order by eratio desc;")
    ans = c.fetchall()
    for i in ans:
        date = ans[0][0]
        errorratio = ans[0][1]
        date = datetime.strftime(date, '%b %d, %Y')
        print(date, " - ", errorratio, "%errors")
    db.close()
