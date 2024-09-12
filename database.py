import pymysql
import os


def load_jobs_from_db():
    try:
        # Establish the connection
        connection = pymysql.connect(
            charset="utf8mb4",
            connect_timeout=10,
            cursorclass=pymysql.cursors.DictCursor,
            db=os.environ['DB_NAME'],
            host=os.environ['DB_HOST'],
            password=os.environ['DB_PASSWORD'],
            read_timeout=10,
            port=26415,
            user=os.environ['DB_USER'],
            write_timeout=10,
        )

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM jobs")
            result_all = cursor.fetchall()

        connection.close() 

        # Process results
        jobs = []
        for row in result_all:
            jobs.append(dict(row))

        return jobs

    except pymysql.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return []  # Return an empty list or handle the error appropriately
    except Exception as e:
        print(f"General error: {e}")
        return []  # Return an empty list or handle the error appropriately
