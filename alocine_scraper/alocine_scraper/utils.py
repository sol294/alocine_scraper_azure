# alocine_scraper/utils.py

import psycopg2

# à remplir depuis .env
DATABASE_URL = 'postgresql://adminname:adminpassword@NAMESERVER.postgres.database.azure.com:5432/dbname'

def connect_to_postgres():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        print("Connexion à PostgreSQL réussie!")

        # Ici vous pouvez exécuter des opérations sur votre base de données
        # par exemple, créer une table, insérer des données, etc.

        return conn

    except psycopg2.Error as e:
        print("Erreur lors de la connexion à PostgreSQL:", e)
        return None

def close_connection(conn):
    if conn:
        conn.close()
        print("Connexion à PostgreSQL fermée.")
