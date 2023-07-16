import mysql.connector

db = mysql.connector.connect(
    host="testing.c5lscidqsauo.us-east-1.rds.amazonaws.com",
    user="zoey",
    passwd="533Qu13L!y4Y!",
    database="testdatabase"
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE testdatabase")

# name = row[0]
# rating = row[1]
# num_reviews = row[2]
# resto_type = row[3]
# price_point = row[4]
# address = row[5]
# about = row[6]
# personal = row[7]

Q1 = """CREATE TABLE Restos (
    resto_ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    resto_name VARCHAR(50) NOT NULL, 
    rating FLOAT(2) NOT NULL, 
    num_reviews INT(5) NOT NULL, 
    resto_type VARCHAR(50) NOT NULL, 
    price_point VARCHAR(5),
    address VARCHAR(50) NOT NULL,
    area VARCHAR(50) NOT NULL,
    personal_note VARCHAR(200) NOT NULL
    gm_embed_html VARCHAR(1000) NOT NULL
    )  
    """

# mycursor.execute(Q1)
# db.commit()

# mycursor.execute("DROP TABLE Restos")
# db.commit()

# mycursor.execute("DESCRIBE Restos")
# for x in mycursor:
#     print(x) 





