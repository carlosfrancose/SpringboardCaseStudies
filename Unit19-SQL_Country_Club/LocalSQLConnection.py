import sqlite3
import pandas as pd
from sqlite3 import Error
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
    print(f"\nQ{query.q_id}: {query.question}\n{result}\n")

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
        )
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