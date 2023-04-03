import mysql.connector
import json
#leer el json
with open('twet.json', 'r') as f:
    data = json.load(f)
#conexion ala bd
mydb = mysql.connector.connect(
   host="localhost",
  user="root",
  password="tequiero1",
  database="twets"
)
#esto se crea para hacer las consultas
cursor = mydb.cursor()
#aqui recorremos los archivos e insertamos los datos el json ala bd
for tweet in data:
    #extraemos los datos de cada tweet
    tweet_id = tweet['id']
    text = tweet['texto']
    usuario = tweet['usuario']
    hashtags = ','.join(tweet['hashtags'])
    fecha = tweet['fecha']
    retweets = tweet['retweets']
    favoritos = tweet['favoritos']
    #mandamos los datos con esta consulta ala bd
    insert_query = f"INSERT INTO twetdoc (id, texto, usuario, hashtags, fecha, retweets, favoritos) VALUES ({tweet_id}, '{text}', '{usuario}', '{hashtags}', '{fecha}', {retweets}, {favoritos})"
    #se ejecuta la consulta
    cursor.execute(insert_query)
#se guardan los cambios
mydb.commit()

#se cierra la bd
mydb.close()
