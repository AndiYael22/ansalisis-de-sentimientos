import mysql.connector
import matplotlib.pyplot as plt
# Conexión a la base de datos MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tequiero1",
  database="twets"
)
cursor = mydb.cursor()
query = "SELECT sentimiento, COUNT(*) FROM sentimientos GROUP BY sentimiento"
cursor.execute(query)
results_sent = cursor.fetchall()
query = "SELECT hashtags, COUNT(*) FROM twetdoc GROUP BY hashtags ORDER BY COUNT(*) DESC LIMIT 5"
cursor.execute(query)
results_hash = cursor.fetchall()
mydb.close()
# Crea los valores para el gráfico de sentimientos
labels_sent = ['Positivo', 'Negativo', 'Neutral']
values_sent = [0, 0, 0]
for result in results_sent:
    if result[0] == 'positivo':
        values_sent[0] = result[1]
    elif result[0] == 'negativo':
        values_sent[1] = result[1]
    else:
        values_sent[2] = result[1]
# se crea la grafica de los sentimientos
plt.subplot(2, 1, 1)
plt.bar(labels_sent, values_sent)
plt.title('Sentimientos de los tweets')
# se crea la grafica de los hashtags
labels_hash = [result[0] for result in results_hash]
values_hash = [result[1] for result in results_hash]
plt.subplot(2, 1, 2)
plt.bar(labels_hash, values_hash)
plt.title('Top 5 hashtags')
# Muestra los gráficos
plt.tight_layout()
plt.show()
