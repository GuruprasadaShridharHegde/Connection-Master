import oracledb

# Oracle credentials
username = "your_user_name"
password = "your_password"
dsn = "yourawsdsn.eu-west-1.rds.amazonaws.com:1521/YOURDB"

try:
    # Attempt to connect to Oracle
    conn = oracledb.connect(user=username, password=password, dsn=dsn)
    print("Connection successful!")

    # Perform other operations if needed
    # Create a cursor
    cursor = conn.cursor()

    # Execute the required query
    cursor.execute('SELECT count(*) FROM "YOURSCHEMA"."YOURTABLE"')

    # Print the count
    count = cursor.fetchone()[0]
    print(f"Count of rows in YOURTABLE: {count}")

    # Close the connection when done
    conn.close()

except oracledb.Error as e:
    print(f"Connection failed: {e}")
