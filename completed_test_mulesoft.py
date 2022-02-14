import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="94adgnnanduKS#",
  database="moviedata"
)

cur1 = db.cursor()
#CREATING TABLE
"""cur1.execute("CREATE TABLE movie(movie_name VARCHAR(100),actor VARCHAR(100),actress VARCHAR(100),year INT,director VARCHAR(100))")"""

#INSERTING ITEMS INTO TABLE
"""insert = "INSERT INTO movie (movie_name, actor, actress, year, director) VALUES (%s, %s, %s, %s, %s)"
values = [
  ('Inception', 'Leonardo DiCaprio', 'Elliot Page', '2010', 'Christopher Nolan'),
  ('The Prestige', 'Christian Bale', 'Scarlett Johansson', '2006', 'Christopher Nolan'),
  ('Prisoners', 'Hugh Jackman', 'Melisa Leo', '2013', 'Denis Villeneuve'),
]

cur1.executemany(insert,values)
db.commit()"""

#DISPLAYING TABLE ITEMS
cur1.execute("SELECT * FROM movie")

output = cur1.fetchall()

for x in output:
  print(x)