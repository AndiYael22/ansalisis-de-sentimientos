import twint
import pandas as pd
import mysql.connector
#configuracion de la bd
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'tequiero1'
mysql_database = 'twets'
#configuramos twint para la extraccion de datos
c = twint.Config()
c.Search = 'TikTok'
c.Hide_output = True
c.Store_object = True
c.Store_csv = True
c.Limit=100
c.Timeout = 30
c.Output = 'tweets.csv'
twint.run.Search(c)
#aqui leemos los datos que extragimos desde el archivo csv
tweets_df = pd.read_csv('tweets.csv', usecols=['id', 'username', 'date', 'tweet', 'hashtags'])
#conexion con la bd
mysql_conn = mysql.connector.connect(host=mysql_host, user=mysql_user, password=mysql_password, database=mysql_database)
mysql_cursor = mysql_conn.cursor()
#mandamos los datos de los tweets ala bd
for i, row in tweets_df.iterrows():
    tweet_id = row['id']
    username = row['username']
    date = row['date']
    tweet = row['tweet']
    hashtags = row['hashtags']
    mysql_cursor.execute('INSERT INTO tweets (id, username, date, tweet, hashtags) VALUES (%s, %s, %s, %s, %s)', (tweet_id, username, date, tweet, hashtags))
mysql_conn.commit()
#cerramos la conexion ala bd
mysql_cursor.close()
mysql_conn.close()
