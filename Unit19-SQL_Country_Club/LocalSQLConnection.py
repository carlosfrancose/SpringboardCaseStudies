import sqlite3
import pandas as pd
from dataclasses import dataclass

@dataclass(frozen=True)
class Query:
    """
    A single question and its corresponding SQL query.
    """
    q_id: int
    question: str
    sql: str


def create_connection(db_file) -> sqlite3.Connection:
    """
    Prints SQLite version and creates connection to SQLite database.

    :param db_file: database file
    :return: Connection object
    :rtype: sqlite3.Connection
    """
    sql_v = sqlite3.version_info
    print(f"sqlite version: {sql_v[0]}.{sql_v[1]}.{sql_v[2]}")
    return sqlite3.connect(db_file)

def read_and_print_query(conn: sqlite3.Connection, query: Query) -> None:
    """
    Runs SQL query and prints out results.
    
    :param query: Query object (for question id and string)
    :type query: Query
    """
    result = pd.read_sql_query(query.sql, conn)
    print(f"\nQ{query.q_id}: {query.question}\n\n{result}\n")

QUERIES: list[Query] = [
    Query(q_id=1,
          question=(
              "Some of the facilities charge a fee to members, but some do not.\n"
              "Write a SQL query to produce a list of the names of the facilities "
              "that do."
          ),
          sql="""
              SELECT name
              FROM Facilities
              WHERE membercost > 0;
              """
        ),
    Query(q_id=2,
          question="How many facilities do not charge a fee to members?",
          sql="""
              SELECT COUNT(*)
              FROM Facilities
              WHERE membercost = 0;
              """
        ),
    Query(q_id=3,
          question=(
              "Write an SQL query to show a list of facilities that charge a fee to "
              "members where the fee is less than 20% of the facility's monthly "
              "maintenance cost. \nReturn the facid, facility name, member cost, and "
              "monthly maintenance of the facilities in question."
          ),
          sql="""
              SELECT facid, name, membercost, monthlymaintenance
              FROM Facilities
              WHERE membercost < monthlymaintenance * 0.2;
              """
        ),
        Query(q_id=4,
          question=(
              "Write an SQL query to retrieve the details of facilities with ID 1 and "
              "5.\nTry writing the query without using the OR operator."
          ),
          sql="""
              SELECT *
              FROM Facilities
              WHERE name LIKE '%2';
              """
        ),
    Query(q_id=5,
          question=(
              "Produce a list of facilities, with each labelled as 'cheap' or "
              "'expensive', depending on if their monthly maintenance cost is more "
              "than $100. \nReturn the name and monthly maintenance of the facilities "
              "in question."
          ),
          sql="""
              SELECT 
                  name,
                  monthlymaintenance,
                  CASE
                      WHEN monthlymaintenance > 100 THEN 'expensive'
                      ELSE 'cheap'
                  END AS cost_label
              FROM Facilities;
              """
        ),
    Query(q_id=6,
          question=(
              "You'd like to get the first and last name of the last member(s) "
              "who signed up. \nTry not to use the LIMIT clause for your solution."
          ),
          sql="""
              SELECT firstname, surname
              FROM Members
              WHERE joindate = (
                  SELECT MAX(joindate)
                  FROM Members
              );
              """
        ),
    Query(q_id=7,
          question=(
              "Produce a list of all members who have used a tennis court. \nInclude "
              "in your output the name of the court, and the name of the member "
              "formatted as a single column. \nEnsure no duplicate data, and order "
              "by the member name."
          ),
          sql="""
              SELECT DISTINCT
                  Facilities.name AS court_name,
                  Members.firstname || ' ' || Members.surname AS member_name
              FROM Facilities
              JOIN Bookings ON Facilities.facid = Bookings.facid
              JOIN Members ON Bookings.memid = Members.memid
              WHERE Facilities.name LIKE 'Tennis%'
              ORDER BY member_name;
              """
        ),
    Query(q_id=8,
          question=(
              "Produce a list of bookings on the day of 2012-09-14 which will cost "
              "the member (or guest) more than $30. Remember that guests have "
              "different costs to members (the listed costs are per half-hour "
              "'slot'), and the guest user's ID is always 0. \nInclude in your "
              "output the name of the facility, the name of the member formatted "
              "as a single column, and the cost. \nOrder by descending cost, and do "
              "not use any subqueries."
          ),
          sql="""
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
              """
        ),
    Query(q_id=9,
          question=(
              "This time, produce the same result as in Q8, but using a subquery."
          ),
          sql="""
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
                  AND bookings_cost.starttime < '2012-09-15'
                  AND bookings_cost.cost > 30
              ORDER BY bookings_cost.cost DESC;
              """
        ),
    Query(q_id=10,
          question=(
              "Produce a list of facilities with a total revenue less than 1000. "
              "The output of facility name and total revenue, sorted by revenue. "
              "\nRemember that there's a different cost for guests and members!"
          ),
          sql="""
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
              """
        ),
    Query(q_id=11,
          question=(
              "Produce a report of members and who recommended them in alphabetic "
              "surname,firstname order."
          ),
          sql="""
              SELECT
                  m.surname,
                  m.firstname,
                  r.surname AS recommender_surname,
                  r.firstname AS recommender_firstname
              FROM Members m
              LEFT JOIN Members r
                  ON r.memid = CAST(m.recommendedby AS INTEGER)
              ORDER BY m.surname, m.firstname;
              """
        ),
    Query(q_id=12,
          question=(
              "Find the facilities with their usage by member, but not guests."
          ),
          sql="""
              SELECT
                  Facilities.name AS facility_name,
                  SUM(Bookings.slots) AS member_bookings
              FROM Bookings
              JOIN Facilities ON Facilities.facid = Bookings.facid
              WHERE Bookings.memid > 0
              GROUP BY facility_name
              ORDER BY member_bookings DESC;
              """
        ),
    Query(q_id=13,
          question=(
              "Find the facilities usage by month, but not guests."
          ),
          sql="""
              SELECT
                  Facilities.name AS facility_name,
                  strftime('%Y-%m', Bookings.starttime) AS month,
                  SUM(Bookings.slots) AS member_bookings
              FROM Bookings
              JOIN Facilities ON Facilities.facid = Bookings.facid
              WHERE Bookings.memid > 0
              GROUP BY facility_name, month
              ORDER BY month, facility_name;
              """
        ),

]

def main():
    database = "sqlite_db_pythonsqlite.db"
 
    try:
        # Create a database connection
        conn = create_connection(database)
        with conn:
            for q in QUERIES:
                read_and_print_query(conn, q)
    except sqlite3.Error as e:
        print(e)
 
 
if __name__ == '__main__':
    main()