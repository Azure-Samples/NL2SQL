from promptflow import tool
from promptflow.connections import CustomConnection
import pyodbc


def _strip(text: str) -> str:
    return text.strip("` \n").strip("sql ")

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def query_db(sql_query: str, SQL_conn: CustomConnection) -> str:
    # Strip the SQL query string
    stripped_query = _strip(sql_query)

    conn = pyodbc.connect(SQL_conn.conn)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    try:
        cursor.execute(stripped_query)
        
        # Get the column names from cursor.description
        columns = [column[0] for column in cursor.description]

        # Initialize an empty list to store the results as dictionaries
        results = []

        # Fetch all rows and create dictionaries
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))  
    except Exception as e:
        return f"Error: {e}"
    cursor.close()
    conn.close()

    print(results)
    return 'SQL Query: ' + str(results)