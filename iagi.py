
import sqlite3
import hashlib

# Connexion à la base de données (cette étape crée la base de données si elle n'existe pas)
connexion = sqlite3.connect("iagi.db")
curseur = connexion.cursor()

# Création de la table students
curseur.execute("CREATE TABLE IF NOT EXISTS students ( id INTEGER PRIMARY KEY AUTOINCREMENT,firstname TEXT NOT NULL,lastname TEXT NOT NULL,email TEXT UNIQUE NOT NULL,passwd TEXT NOT NULL)")





