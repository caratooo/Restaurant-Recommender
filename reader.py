import csv
import mysql.connector

db = mysql.connector.connect(
    host="testing.c5lscidqsauo.us-east-1.rds.amazonaws.com",
    user="zoey",
    passwd="533Qu13L!y4Y!",
    database="testdatabase"
)

mycursor = db.cursor()

def read_restos(file: str) -> None:
    """ Reads all restaurants and their values in csv file. Then inserts them into the restaurant database.
    """
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        Q1 = """INSERT INTO Restos (resto_name, rating, num_reviews, resto_type, price_point, address, personal_note)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
             """
        
        for row in reader:
            name = str(row[0])
            rating = float(row[1])
            num_reviews = int(row[2].replace(',', ''))
            resto_type = str(row[3])
            price_point = str(row[4])
            address = str(row[5])
            area = str(row[6])
            personal = str(row[7])
            gm_embed = str(row[8])
            
            if price_point == '':
                Q2 = """INSERT INTO Restos (resto_name, rating, num_reviews, resto_type, address, area, personal_note, gm_embed) 
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                     """
                mycursor.execute(Q2, (name, rating, num_reviews, resto_type, address, area, personal, gm_embed))
                db.commit()
            else:
                mycursor.execute(Q1, (name, rating, num_reviews, resto_type, price_point, address, area, personal, gm_embed))
                db.commit()


# read_restos('google.csv')

# mycursor.execute("SHOW TABLES")

# mycursor.execute("SELECT * FROM Restos")

# for x in mycursor:
#     print(x)