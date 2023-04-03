import json
import mysql.connector
from textblob import TextBlob
# Conecta a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tequiero1",
  database="twets"
)
# Crea un cursor para realizar consultas
cursor = mydb.cursor()
# Lee el archivo JSON
with open('twet.json') as f:
    data = json.load(f)
# Analiza el sentimiento de cada texto y almacena los resultados en la base de datos
for item in data:
    text = item['texto']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "positivo"
    elif polarity < 0:
        sentiment = "negativo"
    else:
        sentiment = "neutral"
    insert_query = f"INSERT INTO sentimientos (tweet_id, sentimiento) VALUES ({item['id']}, '{sentiment}')"
    cursor.execute(insert_query)
    mydb.commit()
# Cierra la conexión a la base de datos
mydb.close()
