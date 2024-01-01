import sqlite3
from datetime import datetime

create_playlist_musics_table_command = """
CREATE TABLE PlaylistMusic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    playlist_id INTEGER NOT NULL,
    music_id INTEGER NOT NULL,
    creation_date DATE NOT NULL,
    FOREIGN KEY (playlist_id) REFERENCES Playlists(playlist_id)
    FOREIGN KEY (music_id) REFERENCES Musics(music_id)
);
"""


def connect_to_database(database_name='./model/db/Flow.db'):
    """
    Connect to the SQLite database and return the connection and cursor.
    """
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    return conn, cursor


def create_playlist_musics_table(cursor):
    """
    `Create musics and users tables.
    """
    cursor.execute(create_playlist_musics_table_command)


def close_connection(conn):
    """
    Commit changes and close the database connection.
    """
    conn.commit()
    conn.close()


def insert_playlist_musics_data(playlist_id, music_id):
    """
    Insert data into the users table.
    """
    conn, cursor = connect_to_database()

    creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    playlist_musics = [playlist_id, creation_date, music_id]
    cursor.execute(
        'INSERT INTO PlaylistMusic (playlist_id, creation_date, music_id) VALUES (?, ?, ?)',
        playlist_musics)

    close_connection(conn)


def find_playlist_musics_by_id(playlist_id):
    conn, cursor = connect_to_database()

    cursor.execute('SELECT * FROM PlaylistMusic WHERE playlist_id = ?', (playlist_id,))
    playlist_musics = cursor.fetchall()

    close_connection(conn)

    return playlist_musics


def delete_playlist_musics(playlist_id, music_id):
    conn, cursor = connect_to_database()

    cursor.execute('DELETE FROM PlaylistMusic WHERE playlist_id = ? AND music_id = ?', (playlist_id, music_id))

    close_connection(conn)


def find_all_songs_by_playlist_id(playlist_id):
    conn, cursor = connect_to_database()

    cursor.execute('SELECT music_id FROM PlaylistMusic WHERE playlist_id = ?', (playlist_id[0],))
    playlist_musics = cursor.fetchall()

    close_connection(conn)

    return playlist_musics
