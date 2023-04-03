import snscrape.modules.twitter as sntwitter
import pandas as pd
import mysql.connector
# Configuración de la BD
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'tequiero1'
mysql_database = 'tweets'
# Lista para almacenar los tweets
tweets_container = []

# Extracción de datos de Twitter y almacenamiento en la lista
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('suicidio').get_items()):
    if i > 2:
        break
    tweets_container.append([tweet.id, tweet.user.username, tweet.date, tweet.content, [hashtag.name for hashtag in tweet.hashtags]])
# Creamos un dataframe apartir de la lista
tweets_df = pd.DataFrame(tweets_container, columns=["id", "username", "date", "tweet", "hashtags"])
#Conexión a la BD
mysql_conn = mysql.connector.connect(host=mysql_host, user=mysql_user, password=mysql_password, database=mysql_database)
mysql_cursor = mysql_conn.cursor()
# Inserción de datos de los tweets en la BD
for i, row in tweets_df.iterrows():
    tweet_id = row['id']
    username = row['username']
    date = row['date']
    tweet = row['tweet']
    hashtags = row['hashtags']
    mysql_cursor.execute('INSERT INTO tweets (id, username, date, tweet, hashtags) VALUES (%s, %s, %s, %s, %s)', (tweet_id, username, date, tweet, hashtags))
# Confirmación de cambios en la BD y cierre de conexión
mysql_conn.commit()
mysql_cursor.close()
mysql_conn.close()
