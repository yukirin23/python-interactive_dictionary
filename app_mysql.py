import mysql.connector
from difflib import get_close_matches


con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter a word: ")
word = word.lower()
query = cursor.execute(
    "select * from Dictionary where Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result)
else:
    print("No word found!")
