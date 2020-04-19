import mysql.connector
import difflib
from difflib import get_close_matches

connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"

)


cursor = connection.cursor()
s = input("Type a word: ")

ex = f"SELECT * FROM Dictionary WHERE Expression = '{s}'"

firstCharacter = f"SELECT * FROM Dictionary WHERE Expression  LIKE '{s[:3]}%'"

query = cursor.execute(ex)
results = cursor.fetchall()

if results:
    for result in results:
        print(result)
else:
    query = cursor.execute(firstCharacter)
    results = cursor.fetchall()
    matches = get_close_matches(text, data.keys(), n=3, cutoff=0.6)
    for result in results:
        print(result)
    print(s[:3])
