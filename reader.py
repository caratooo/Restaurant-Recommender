import csv
import mysql.connector

db = mysql.connector.connect(
    host="testing.c5lscidqsauo.us-east-1.rds.amazonaws.com",
    user="zoey",
    passwd="533Qu13L!y4Y!",
    database="testdatabase"
)

mycursor = db.cursor()

def read_restos(file: str) -> Graph:
    """
    """
    with open(file, ncoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        for row in reader:
            pass