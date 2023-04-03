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
# Consulta los tweets con el hashtag que quieres analizar
hashtag = "#Shakira"
query = f"SELECT tweet FROM tweets WHERE hashtags LIKE '%{hashtag}%'"
cursor.execute(query)
tweets = cursor.fetchall()
# Analiza el sentimiento de cada tweet y almacena los resultados en la base de datos
for tweet in tweets:
    text = tweet[0]
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "positivo"
    elif polarity < 0:
        sentiment = "negativo"
    else:
        sentiment = "neutral"
    insert_query = f"INSERT INTO sentimientos (tweet_id, sentimiento) VALUES ({tweet_id}, '{sentiment}')"
    cursor.execute(insert_query)
    mydb.commit()
# Cierra la conexión a la base de datos
mydb.close()
