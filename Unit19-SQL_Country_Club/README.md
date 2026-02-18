# Instructions

## Work locally via Python + SQLite

If you want to try work locally by executing your SQL queries directly on the `sqlite_db_pythonsqlite.db` database file then you can work with the `LocalSQLConnection.py` python script. Open the file `SQLTasks Tier 1.sql` for more a list of the questions we want to try answer.

There is already an example query in the file so if you just run the python script you should see something like:

```
# execute the python script
python LocalSQLConnection.py
```

Results should look like:
```
2.6.0
2. Query all tasks
(0, 'Tennis Court 1', 5, 25, 10000, 200)
(1, 'Tennis Court 2', 5, 25, 8000, 200)
(2, 'Badminton Court', 0, 15.5, 4000, 50)
(3, 'Table Tennis', 0, 5, 320, 10)
(4, 'Massage Room 1', 9.9, 80, 4000, 3000)
(5, 'Massage Room 2', 9.9, 80, 4000, 3000)
(6, 'Squash Court', 3.5, 17.5, 5000, 80)
(7, 'Snooker Table', 0, 5, 450, 15)
(8, 'Pool Table', 0, 5, 400, 15)
```

If you see this then things are working and you should be able to edit the file to add in any queries you want. 


## Work online via https://sql.springboard.com/

If you want to just log in somewhere and write SQL (no python involved) then you can go to https://sql.springboard.com/ log in with Username=student and Password=learn_sql@springboard and write and work on your SQL queries in there. Open the file `SQLTasks Tier 1.sql` for more a list of the questions we want to try answer and more information and instructions.

---

# Results

Based on the explaination above, I chose to modify the Python script `LocalSQLConnection.py` for convenience and familiarity.

You can run the script to have all of the queries executed and printed, or simply reference this README to view my results. The queries are within the script under the global list `QUERIES`.

## Queries and Results

### Q1:

**Some of the facilities charge a fee to members, but some do not. Write a SQL query to produce a list of the names of the facilities that do.**

```SQL
SELECT name 
FROM Facilities 
WHERE membercost > 0;
```

|      name      |
|----------------|
| Tennis Court 1 |
| Tennis Court 2 |
| Massage Room 1 |
| Massage Room 2 |
| Squash Court   |

### Q2:

**How many facilities do not charge a fee to members?**

```SQL
SELECT COUNT(*)
FROM Facilities
WHERE membercost = 0;
```

| COUNT(*) |
|----------|
| 4        |

### Q3:

**Write an SQL query to show a list of facilities that charge a fee to members where the fee is less than 20% of the facility's monthly maintenance cost. Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.**

```SQL
SELECT facid, name, membercost, monthlymaintenance
FROM Facilities
WHERE membercost < monthlymaintenance * 0.2;
```

| facid |      name       | membercost | monthlymaintenance |
|-------|-----------------|------------|--------------------|
| 0     | Tennis Court 1  | 5          | 200                |
| 1     | Tennis Court 2  | 5          | 200                |
| 2     | Badminton Court | 0          | 50                 |
| 3     | Table Tennis    | 0          | 10                 |
| 4     | Massage Room 1  | 9.9        | 3000               |
| 5     | Massage Room 2  | 9.9        | 3000               |
| 6     | Squash Court    | 3.5        | 80                 |
| 7     | Snooker Table   | 0          | 15                 |
| 8     | Pool Table      | 0          | 15                 |

### Q4:

**Write an SQL query to retrieve the details of facilities with ID 1 and 5. Try writing the query without using the OR operator.**

```SQL
SELECT *
FROM Facilities
WHERE name LIKE '%2';
```

| facid |      name      | membercost | guestcost | initialoutlay | monthlymaintenance |
|-------|----------------|------------|-----------|---------------|--------------------|
| 1     | Tennis Court 2 | 5          | 25        | 8000          | 200                |
| 5     | Massage Room 2 | 9.9        | 80        | 4000          | 3000               |

### Q5:

**Produce a list of facilities, with each labelled as 'cheap' or 'expensive', depending on if their monthly maintenance cost is more than $100. Return the name and monthly maintenance of the facilities in question.**

```SQL
SELECT 
    name,
    monthlymaintenance,
    CASE
        WHEN monthlymaintenance > 100 THEN 'expensive'
        ELSE 'cheap'
    END AS cost_label
FROM Facilities;
```

|      name       | monthlymaintenance | cost_label |
|-----------------|--------------------|------------|
| Tennis Court 1  | 200                | expensive  |
| Tennis Court 2  | 200                | expensive  |
| Badminton Court | 50                 | cheap      |
| Table Tennis    | 10                 | cheap      |
| Massage Room 1  | 3000               | expensive  |
| Massage Room 2  | 3000               | expensive  |
| Squash Court    | 80                 | cheap      |
| Snooker Table   | 15                 | cheap      |
| Pool Table      | 15                 | cheap      |

### Q6:

**You'd like to get the first and last name of the last member(s) who signed up. Try not to use the LIMIT clause for your solution.**

```SQL
SELECT firstname, surname
FROM Members
WHERE joindate = (
    SELECT MAX(joindate)
    FROM Members
);
```

| firstname | surname |
|-----------|---------|
| Darren    | Smith   |

### Q7:

**Produce a list of all members who have used a tennis court. Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name.**

```SQL
SELECT DISTINCT
    Facilities.name AS court_name,
    Members.firstname || ' ' || Members.surname AS member_name
FROM Facilities
JOIN Bookings ON Facilities.facid = Bookings.facid
JOIN Members ON Bookings.memid = Members.memid
WHERE Facilities.name LIKE 'Tennis%'
ORDER BY member_name;
```

|   court_name   |    member_name    |
|----------------|-------------------|
| Tennis Court 1 | Anne Baker        |
| Tennis Court 2 | Anne Baker        |
| Tennis Court 2 | Burton Tracy      |
| Tennis Court 1 | Burton Tracy      |
| Tennis Court 1 | Charles Owen      |
| Tennis Court 2 | Charles Owen      |
| Tennis Court 2 | Darren Smith      |
| Tennis Court 1 | David Farrell     |
| Tennis Court 2 | David Farrell     |
| Tennis Court 2 | David Jones       |
| Tennis Court 1 | David Jones       |
| Tennis Court 1 | David Pinker      |
| Tennis Court 1 | Douglas Jones     |
| Tennis Court 1 | Erica Crumpet     |
| Tennis Court 2 | Florence Bader    |
| Tennis Court 1 | Florence Bader    |
| Tennis Court 2 | GUEST GUEST       |
| Tennis Court 1 | GUEST GUEST       |
| Tennis Court 1 | Gerald Butters    |
| Tennis Court 2 | Gerald Butters    |
| Tennis Court 2 | Henrietta Rumney  |
| Tennis Court 1 | Jack Smith        |
| Tennis Court 2 | Jack Smith        |
| Tennis Court 1 | Janice Joplette   |
| Tennis Court 2 | Janice Joplette   |
| Tennis Court 2 | Jemima Farrell    |
| Tennis Court 1 | Jemima Farrell    |
| Tennis Court 1 | Joan Coplin       |
| Tennis Court 1 | John Hunt         |
| Tennis Court 2 | John Hunt         |
| Tennis Court 1 | Matthew Genting   |
| Tennis Court 2 | Millicent Purview |
| Tennis Court 2 | Nancy Dare        |
| Tennis Court 1 | Nancy Dare        |
| Tennis Court 2 | Ponder Stibbons   |
| Tennis Court 1 | Ponder Stibbons   |
| Tennis Court 2 | Ramnaresh Sarwin  |
| Tennis Court 1 | Ramnaresh Sarwin  |
| Tennis Court 2 | Tim Boothe        |
| Tennis Court 1 | Tim Boothe        |
| Tennis Court 2 | Tim Rownam        |
| Tennis Court 1 | Tim Rownam        |
| Tennis Court 2 | Timothy Baker     |
| Tennis Court 1 | Timothy Baker     |
| Tennis Court 1 | Tracy Smith       |
| Tennis Court 2 | Tracy Smith       |

### Q8:
**Produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30. Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user's ID is always 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries.**

```SQL
SELECT
    Facilities.name AS facility_name,
    Members.firstname || ' ' || Members.surname AS member_name,
    CASE
        WHEN Bookings.memid = 0 THEN Bookings.slots * Facilities.guestcost
        ELSE Bookings.slots * Facilities.membercost
    END AS cost
FROM Bookings
JOIN Facilities ON Facilities.facid = Bookings.facid
JOIN Members ON Members.memid = Bookings.memid
WHERE Bookings.starttime >= '2012-09-14'
    AND Bookings.starttime < '2012-09-15'
    AND (CASE
        WHEN Bookings.memid = 0 THEN Bookings.slots * Facilities.guestcost
        ELSE Bookings.slots * Facilities.membercost
    END) > 30
ORDER BY cost DESC;
```

| facility_name  |  member_name   | cost |
|----------------|----------------|------|
| Massage Room 2 | GUEST GUEST    | 320  |
| Massage Room 1 | GUEST GUEST    | 160  |
| Massage Room 1 | GUEST GUEST    | 160  |
| Massage Room 1 | GUEST GUEST    | 160  |
| Tennis Court 2 | GUEST GUEST    | 150  |
| Tennis Court 1 | GUEST GUEST    | 75   |
| Tennis Court 1 | GUEST GUEST    | 75   |
| Tennis Court 2 | GUEST GUEST    | 75   |
| Squash Court   | GUEST GUEST    | 70.0 |
| Massage Room 1 | Jemima Farrell | 39.6 |
| Squash Court   | GUEST GUEST    | 35.0 |
| Squash Court   | GUEST GUEST    | 35.0 |

### Q9: 

**This time, produce the same result as in Q8, but using a subquery.**

```SQL
SELECT facility_name, member_name, cost
FROM (
  SELECT
    Facilities.name AS facility_name,
    Members.firstname || ' ' || Members.surname AS member_name,
    Bookings.starttime,
    CASE
      WHEN Bookings.memid = 0 THEN Bookings.slots * Facilities.guestcost
      ELSE Bookings.slots * Facilities.membercost
    END AS cost
  FROM Bookings
  JOIN Facilities ON Facilities.facid = Bookings.facid
  JOIN Members ON Members.memid = Bookings.memid
) AS bookings_cost
WHERE bookings_cost.starttime >= '2012-09-14'
  AND bookings_cost.starttime <  '2012-09-15'
  AND bookings_cost.cost > 30
ORDER BY bookings_cost.cost DESC;
```

| facility_name  |  member_name   | cost |
|----------------|----------------|------|
| Massage Room 2 | GUEST GUEST    | 320  |
| Massage Room 1 | GUEST GUEST    | 160  |
| Massage Room 1 | GUEST GUEST    | 160  |
| Massage Room 1 | GUEST GUEST    | 160  |
| Tennis Court 2 | GUEST GUEST    | 150  |
| Tennis Court 1 | GUEST GUEST    | 75   |
| Tennis Court 1 | GUEST GUEST    | 75   |
| Tennis Court 2 | GUEST GUEST    | 75   |
| Squash Court   | GUEST GUEST    | 70.0 |
| Massage Room 1 | Jemima Farrell | 39.6 |
| Squash Court   | GUEST GUEST    | 35.0 |
| Squash Court   | GUEST GUEST    | 35.0 |

### Q10:

**Produce a list of facilities with a total revenue less than 1000. The output of facility name and total revenue, sorted by revenue. Remember that there's a different cost for guests and members!**

```SQL
SELECT
  Facilities.name AS facility_name,
  SUM(
    CASE
      WHEN Bookings.memid = 0 THEN Bookings.slots * Facilities.guestcost
      WHEN Bookings.memid IS NULL THEN 0
      ELSE Bookings.slots * Facilities.membercost
    END
  ) AS revenue
FROM Facilities
LEFT JOIN Bookings ON Bookings.facid = Facilities.facid
GROUP BY Facilities.facid, Facilities.name
HAVING revenue < 1000
ORDER BY revenue;
```

| facility_name | revenue |
|---------------|---------|
| Table Tennis  | 180     |
| Snooker Table | 240     |
| Pool Table    | 270     |

### Q11:

**Produce a report of members and who recommended them in alphabetic surname,firstname order**

```SQL
SELECT
    m.surname,
    m.firstname,
    r.surname  AS recommender_surname,
    r.firstname AS recommender_firstname
FROM Members m
LEFT JOIN Members r
    ON r.memid = CAST(m.recommendedby AS INTEGER)
ORDER BY m.surname, m.firstname;
```

|      surname      | firstname | recommender_surname | recommender_firstname |
|-------------------|-----------|---------------------|-----------------------|
| Bader             | Florence  | Stibbons            | Ponder                |
| Baker             | Anne      | Stibbons            | Ponder                |
| Baker             | Timothy   | Farrell             | Jemima                |
| Boothe            | Tim       | Rownam              | Tim                   |
| Butters           | Gerald    | Smith               | Darren                |
| Coplin            | Joan      | Baker               | Timothy               |
| Crumpet           | Erica     | Smith               | Tracy                 |
| Dare              | Nancy     | Joplette            | Janice                |
| Farrell           | David     | GUEST               | GUEST                 |
| Farrell           | Jemima    | GUEST               | GUEST                 |
| GUEST             | GUEST     | GUEST               | GUEST                 |
| Genting           | Matthew   | Butters             | Gerald                |
| Hunt              | John      | Purview             | Millicent             |
| Jones             | David     | Joplette            | Janice                |
| Jones             | Douglas   | Jones               | David                 |
| Joplette          | Janice    | Smith               | Darren                |
| Mackenzie         | Anna      | Smith               | Darren                |
| Owen              | Charles   | Smith               | Darren                |
| Pinker            | David     | Farrell             | Jemima                |
| Purview           | Millicent | Smith               | Tracy                 |
| Rownam            | Tim       | GUEST               | GUEST                 |
| Rumney            | Henrietta | Genting             | Matthew               |
| Sarwin            | Ramnaresh | Bader               | Florence              |
| Smith             | Darren    | GUEST               | GUEST                 |
| Smith             | Darren    | GUEST               | GUEST                 |
| Smith             | Jack      | Smith               | Darren                |
| Smith             | Tracy     | GUEST               | GUEST                 |
| Stibbons          | Ponder    | Tracy               | Burton                |
| Tracy             | Burton    | GUEST               | GUEST                 |
| Tupperware        | Hyacinth  | GUEST               | GUEST                 |
| Worthington-Smyth | Henry     | Smith               | Tracy                 |

### Q12:

**Find the facilities with their usage by member, but not guests**

This question was oddly worded, but I'm assumming we're mean't to just list all facilities that have been booked by members, and exclude any facilities that have been booked by guests.

```SQL
SELECT
    Facilities.name AS facility_name,
    SUM(Bookings.slots) AS member_bookings
FROM Bookings
JOIN Facilities ON Facilities.facid = Bookings.facid
WHERE Bookings.memid > 0
GROUP BY facility_name
ORDER BY member_bookings DESC;
```

|  facility_name  | member_bookings |
|-----------------|-----------------|
| Badminton Court | 1086            |
| Tennis Court 1  | 957             |
| Massage Room 1  | 884             |
| Tennis Court 2  | 882             |
| Snooker Table   | 860             |
| Pool Table      | 856             |
| Table Tennis    | 794             |
| Squash Court    | 418             |
| Massage Room 2  | 54              |

### Q13:

**Find the facilities usage by month, but not guests**

This question is similarly vague as the last one, but I'm going to assume that we're trying to group each facility by month and display how much it's been booked by members on each month.

```SQL
SELECT
    Facilities.name AS facility_name,
    strftime('%Y-%m', Bookings.starttime) AS month,
    SUM(Bookings.slots) AS member_bookings
FROM Bookings
JOIN Facilities ON Facilities.facid = Bookings.facid
WHERE Bookings.memid > 0          -- exclude guests (memid = 0)
GROUP BY facility_name, month
ORDER BY month, facility_name;
```

|  facility_name  |  month  | member_bookings |
|-----------------|---------|-----------------|
| Badminton Court | 2012-07 | 165             |
| Massage Room 1  | 2012-07 | 166             |
| Massage Room 2  | 2012-07 | 8               |
| Pool Table      | 2012-07 | 110             |
| Snooker Table   | 2012-07 | 140             |
| Squash Court    | 2012-07 | 50              |
| Table Tennis    | 2012-07 | 98              |
| Tennis Court 1  | 2012-07 | 201             |
| Tennis Court 2  | 2012-07 | 123             |
| Badminton Court | 2012-08 | 414             |
| Massage Room 1  | 2012-08 | 316             |
| Massage Room 2  | 2012-08 | 18              |
| Pool Table      | 2012-08 | 303             |
| Snooker Table   | 2012-08 | 316             |
| Squash Court    | 2012-08 | 184             |
| Table Tennis    | 2012-08 | 296             |
| Tennis Court 1  | 2012-08 | 339             |
| Tennis Court 2  | 2012-08 | 345             |
| Badminton Court | 2012-09 | 507             |
| Massage Room 1  | 2012-09 | 402             |
| Massage Room 2  | 2012-09 | 28              |
| Pool Table      | 2012-09 | 443             |
| Snooker Table   | 2012-09 | 404             |
| Squash Court    | 2012-09 | 184             |
| Table Tennis    | 2012-09 | 400             |
| Tennis Court 1  | 2012-09 | 417             |
| Tennis Court 2  | 2012-09 | 414             |