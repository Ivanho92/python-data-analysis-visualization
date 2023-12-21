import os.path
import sqlite3

import config


def store_content(data):
    connection = sqlite3.connect(os.path.join(config.PROJECT_ROOT_PATH, config.DB_CONTENT_NAME))
    cursor = connection.cursor()

    cursor.executescript('''
        DROP TABLE IF EXISTS Country;
        DROP TABLE IF EXISTS Seizure;
        
        CREATE TABLE Country (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name VARCHAR(255) NOT NULL UNIQUE
        );
        
        CREATE TABLE Seizure (
            year INTEGER NOT NULL,
            country INTEGER NOT NULL,
            number INTEGER,
            PRIMARY KEY (year, country)
        );
    ''')
    connection.commit()

    # Store countries
    countries_ids = dict()
    for country in data['data']:
        cursor.execute('INSERT OR IGNORE INTO Country (name) VALUES (?)', (country,))
        cursor.execute('SELECT Country.id FROM Country WHERE Country.name = ?', (country,))
        country_id = cursor.fetchone()[0]
        countries_ids[country] = country_id
    connection.commit()

    # Store seizure
    for i, year in enumerate(data['headers']):
        for country in data['data']:
            seizures_number = data['data'][country]['data'][i]
            seizures_number = seizures_number if seizures_number != '' else None

            country_id = countries_ids[country]

            cursor.execute('INSERT OR REPLACE INTO Seizure (country, year, number) VALUES (?, ?, ?)',
                           (country_id, year, seizures_number))
        connection.commit()

    cursor.close()
    connection.close()


def get_content():
    connection = sqlite3.connect(os.path.join(config.PROJECT_ROOT_PATH, config.DB_CONTENT_NAME))
    cursor = connection.cursor()

    cursor.execute('''
        SELECT Country.name, ROUND(AVG(Seizure.number), 2) AS 'average' FROM Seizure
        JOIN Country ON Country.id = Seizure.country
        GROUP BY Country.name
        HAVING average IS NOT NULL
    ''')
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


def store_model(model):
    connection = sqlite3.connect(os.path.join(config.PROJECT_ROOT_PATH, config.DB_MODEL_NAME))
    cursor = connection.cursor()

    cursor.executescript('''
        DROP TABLE IF EXISTS Country;
        DROP TABLE IF EXISTS Seizure;
    
        CREATE TABLE Country (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name VARCHAR(255) NOT NULL UNIQUE,
            lat FLOAT NOT NULL,
            lng FLOAT NOT NULL
        );
        
        CREATE TABLE Seizure (
            country_id INTEGER NOT NULL UNIQUE,
            average INTEGER,
            FOREIGN KEY (country_id) REFERENCES Country(id)
        );
    ''')

    for row in model:
        cursor.execute(
            'INSERT OR IGNORE INTO Country (name, lat, lng) VALUES (?,?,?)',
            (row['country'], row['coordinates']['lat'], row['coordinates']['lng'])
        )
        cursor.execute('SELECT id FROM Country WHERE name = ?', (row['country'],))
        country_id = cursor.fetchone()[0]

        cursor.execute(
            'INSERT OR REPLACE INTO Seizure (country_id, average) VALUES (?,?)',
            (country_id, row['avg_seizures'])
        )

        connection.commit()

    cursor.close()
    connection.close()


def get_model():
    connection = sqlite3.connect(os.path.join(config.PROJECT_ROOT_PATH, config.DB_MODEL_NAME))
    cursor = connection.cursor()

    cursor.execute('''
        SELECT Country.name, Country.lat, Country.lng, Seizure.average
        FROM Seizure
        JOIN Country ON Country.id = Seizure.country_id
    ''')
    rows = cursor.fetchall()

    data = list()
    for row in rows:
        data.append({
            'country': row[0],
            'seizures': row[3],
            'coords': {
                'lat': row[1],
                'lng': row[2]
            },
        })

    cursor.close()
    connection.close()

    return data


get_model()
