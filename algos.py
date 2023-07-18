import mysql.connector

db = mysql.connector.connect(
    host="testing.c5lscidqsauo.us-east-1.rds.amazonaws.com",
    user="zoey",
    passwd="533Qu13L!y4Y!",
    database="testdatabase"
)

mycursor = db.cursor()

def generate_random() -> int:
    """ Generates one random restaurant rec from the database. Returns the name of that restaurant.
    """
    mycursor.execute("SELECT resto_ID FROM Restos ORDER BY RAND() LIMIT 1")
    for x in mycursor:
        return x[0]
    
    # how to grab that instance: SELECT name, address, etc. FROM Restos WHERE resto_id=x[0]

    # idea 2: return list of all restos (just incase they want to generate more)
    # list_of_restos = []  # list of resto_IDs
    # mycursor.execute("SELECT resto_ID FROM Restos ORDER BY RAND()")
    # for x in mycursor:
    #     list_of_restos.append(x[0])
    # return list_of_restos


def generate_by_area(resto_area: str) -> str:
    """ Generates one random restaurant rec from the database based on user selection of area. 
    Returns the name of that restaurant.

    Possible areas:
    - Chinatown (Includes chinatown, kensington and dundas)
    - Yonge (includes atrium, yonge and yorkville)
    - Ossington (includes ossington)
    - Little italy (includes little italy)
    - Koreatown/Annex (includes annex and koreatown)
    - Near sw uoft (includes chinatown, kensington, baldwin, harbord)
    - Queen st. and below (includes that)
    """
    if resto_area == "Chinatown":
        mycursor.execute("SELECT resto_ID FROM Restos WHERE area='Chinatown' or area='Kensington' or area='Dundas' ORDER BY RAND() LIMIT 1")
    elif resto_area == "Yonge":
        mycursor.execute("SELECT resto_ID FROM Restos WHERE area='Yonge' or area='Yorkville' or area='Atrium' ORDER BY RAND() LIMIT 1")
    elif resto_area == "Ossington":
        mycursor.execute("SELECT resto_ID FROM Restos WHERE area='Ossington' ORDER BY RAND() LIMIT 1")
    elif resto_area == "Little Italy":
        mycursor.execute("SELECT resto_ID FROM Restos WHERE area='Little Italy' ORDER BY RAND() LIMIT 1")
    elif resto_area == "Koreatown/Annex":
        mycursor.execute("SELECT resto_ID FROM Restos WHERE area='Koreatown' or area='The Annex' ORDER BY RAND() LIMIT 1")
    elif resto_area == "Near SW UofT":
        mycursor.execute("SELECT resto_ID FROM Restos WHERE area='Chinatown' or area='Kensington' or area='Baldwin' or area='Harbord' ORDER BY RAND() LIMIT 1")
    else:
        mycursor.execute("SELECT resto_ID FROM Restos WHERE area='Queen St and Below' ORDER BY RAND() LIMIT 1")
    
    for x in mycursor:
        return x[0]
    
    # idea 2:
    # list_of_restos = []  # list of resto_IDs
    # mycursor.execute("SELECT resto_ID FROM Restos WHERE area=resto_area ORDER BY RAND()")
    # for x in mycursor:
    #     list_of_restos.append(x[0])
    # return list_of_restos


def generate_by_cuisine(cuisine: str) -> str:
    """Generates one random restaurant rec from the database based on user selection of cuisine. 
    Returns the name of that restaurant.
    """
    mycursor.execute(f"SELECT resto_ID FROM Restos WHERE type LIKE '%{cuisine}%' ORDER BY RAND() LIMIT 1")
    for x in mycursor:
        return(x)
    
    # idea 2:
    # list_of_restos = []  # list of resto_IDs
    # mycursor.execute(f"SELECT resto_ID FROM Restos WHERE type LIKE '%{cuisine}%' ORDER BY RAND()")
    # for x in mycursor:
    #     list_of_restos.append(x[0])
    # return list_of_restos



def generate_been_there(been: bool) -> str:
    """
    """
    if been:
        mycursor.execute("SELECT resto_ID FROM Restos WHERE been_there is TRUE ORDER BY RAND() LIMIT 1")
    else:
        mycursor.execute("SELECT resto_ID FROM Restos ORDER BY RAND() LIMIT 1")

    # idea 2:
    # list_of_restos = []  # list of resto_IDs
    # mycursor.execute(f"SELECT resto_ID FROM Restos WHERE been_there is TRUE ORDER BY RAND()")
    # for x in mycursor:
    #     list_of_restos.append(x[0])
    # return list_of_restos
