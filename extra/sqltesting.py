import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="533Qu13L!y4Y!",
    database="testdatabase"
)

mycursor = db.cursor()

# -- creating new database

# make new database (down) - then can stick it into the server (up) - then delete (down)
# mycursor.execute("CREATE DATABASE testdatabase")


# -- creating new tables

# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint(5) UNSIGNED, personID int(11) PRIMARY KEY AUTO_INCREMENT)")  
# CREATE TABLE <name of table> (<name of col> <type>(max length), <name of col> <type>(max length), ...)
# VARCHAR = str
# UNSIGNED = doesn't store neg or pos
# PRIMARY KEY = unique key that identifies each entry/row
# AUTO_INCREMENT = automatically generates a primary key for each new entry/row


# -- checking cols

# mycursor.execute("DESCRIBE Person")

# for x in mycursor:
#     print(x)


# -- adding new entries/rows

# hard code method (down)
# mycursor.execute("INSERT INTO Person (name, age) VALUES ('tim', 45)")

# try instead (down)
# mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ('Zoey', 18))
# mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ('Yuh', 18))
# db.commit()


#TODO comment out any lines you ran already (without errors)


# -- checking entries/rows

# mycursor.execute("SELECT * FROM Person")

# for x in mycursor:
#     print(x)


# -- Examples w/new table

# mycursor.execute("CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# ENUM = enumerate? like choose from a list of strs
# NOT NULL = cannot be empty when creating a new entry/row

# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)", ('E', datetime.now(), 'O'))
# db.commit()


# -- selecting specific rows

# mycursor.execute("SELECT id FROM Test WHERE gender = 'M' ORDER BY id DESC")
# mycursor.execute("SELECT * FROM Test")
# WHERE = filters entries to match command
# ORDER BY = orders specfic entries by command

# for x in mycursor:
#     print(x)


# -- altering tables

# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")
# inserts new col

# mycursor.execute("ALTER TABLE Test DROP food")
# deletes col

# mycursor.execute("ALTER TABLE Test CHANGE name first_name VARCHAR(50)")
# changes name of specific col
# CHANGE <og name> <new name> <type>(<max length MUST BE THE SAME AS OG OR MORE THAN THE BIGGEST ENTRY>)


# -- foreign keys

Q1 = "CREATE TABLE Users (id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), passwd VARCHAR(50))"
# can store queries in variables to access later (then you don't have to comment out every single one)

Q2 = "CREATE TABLE Scores (userID int PRIMARY KEY, FOREIGN KEY(userID) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"
# foreign key can be the primary key of a table (tho usually tbh it's not)
# FOREIGN KEY(col name) REFERENCES <table name>(<key col name>)
# DEFAULT = default value of that col

# mycursor.execute(Q1)
# mycursor.execute(Q2)

# mycursor.execute("SHOW TABLES")
# shows tables in database (above)

users = [('tim', 't'), ('zoey', 'z'), ('apple','a')]
user_scores = [(10, 100), (20, 200), (30, 300)]


Q3 = "INSERT INTO Users (name, passwd) VALUES (%s,%s)"

Q4 = "INSERT INTO Scores (userID, game1, game2) VALUES (%s,%s,%s)"

# for x, user in enumerate(users):
#     mycursor.execute(Q3, user)
#     last_id = mycursor.lastrowid
#     # lastrowid = last row id that was inserted into the table (primary key)
#     mycursor.execute(Q4, (last_id,) + user_scores[x])
#     # (last_id,) + user_scores[x] just inserts a new tuple (id, game1, game2) into Scores table

# mycursor.execute("SELECT * FROM Scores")

# for x in mycursor:
#     print(x)

# mycursor.execute("SELECT * FROM Users")

# for x in mycursor:
#     print(x)   


Q5 = """CREATE TABLE Testing (
    yuh int PRIMARY KEY AUTO_INCREMENT, 
    bruh VARCHAR(50), 
    lol VARCHAR(50))
    """

# mycursor.execute(Q5)

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

Q6 = "INSERT INTO Testing (bruh, lol) VALUES (%s,%s)"

# mycursor.execute(Q6, ('hi', NULL))

# print(float('5.5'))


# <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2886.583933612304!2d-79.37617410000003!3d43.656824100000016!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d4cb7d8f5bab37%3A0x2b4f8bb9ae5f275f!2zS3lvdG8gS2F0c3VneXXjgJDkuqzpg73li53niZvjgJE!5e0!3m2!1sen!2sca!4v1689542469230!5m2!1sen!2sca" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

# mycursor.execute("DESCRIBE Users")
# for x in mycursor:
#     print(x)

# mycursor.execute("SELECT id FROM Users ORDER BY RAND() LIMIT 1")
# print(mycursor)
# print(type(mycursor))
# mycursor.execute("ORDER BY RAND()")
# mycursor.execute("LIMIT 1")

string = 'zoe'

mycursor.execute(f"SELECT id FROM Users WHERE name LIKE '%{string}%' ORDER BY RAND() LIMIT 1")

for x in mycursor:
    print(x)
    print(type(x))
    print(type(x[0]))

