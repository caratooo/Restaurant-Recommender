import csv
import mysql.connector

db = mysql.connector.connect(
    host="testing.c5lscidqsauo.us-east-1.rds.amazonaws.com",
    user="zoey",
    passwd="533Qu13L!y4Y!",
    database="testdatabase"
)

mycursor = db.cursor()

def read_restos(file: str):
    """
    """
    with open(file, ncoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        Q1 = """INSERT INTO Restos (resto_ID, resto_name, rating, num_reviews, resto_type, price_point, address, about, personal_note)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
        
        for row in reader:
            name = row[0]
            rating = row[1]
            num_reviews = row[2]
            resto_type = row[3]
            price_point = row[4]
            address = row[5]
            personal = row[7]
            
            if price_point == '':
                mycursor.execute("""INSERT INTO Restos (resto_ID, resto_name, rating, num_reviews, resto_type, price_point, address, about, personal_note) 
                                 VALUES(name, rating, num_reviews, resto_type, NULL, address, personal)
                                 """)
            else:
                mycursor.execute(Q1, (name, rating, num_reviews, resto_type, price_point, address, personal))


