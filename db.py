import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="snake_db",
    user="postgres",
    password="1234",
    host="127.0.0.1",
    port="5432"
)

cur = conn.cursor()


def init_db():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS game_sessions (
        id SERIAL PRIMARY KEY,
        player_id INTEGER REFERENCES players(id),
        score INTEGER NOT NULL,
        level_reached INTEGER NOT NULL,
        played_at TIMESTAMP DEFAULT NOW()
    );
    """)
    conn.commit()

def get_or_create_player(username):
    username = username.strip().lower()

    print("PLAYER INPUT:", username)
    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    row = cur.fetchone()

    print("FOUND IN DB:", row)

    if row:
        return row[0]

    cur.execute(
        "INSERT INTO players (username) VALUES (%s)",
        (username,)
    )
    conn.commit()

    cur.execute("SELECT id FROM players WHERE username = %s", (username,))
    res =  cur.fetchone()

    print("CREATED PLAYER:", res)

    return res[0]

def save_game(player_id, score, level):
    cur.execute("""
        INSERT INTO game_sessions (player_id, score, level_reached)
        VALUES (%s, %s, %s)
    """, (player_id, score, level))
    conn.commit()


def get_top_scores(limit=10):
    cur.execute("""
        SELECT p.username, s.score, s.level_reached, s.played_at
        FROM game_sessions s
        JOIN players p ON p.id = s.player_id
        ORDER BY s.score DESC
        LIMIT %s
    """, (limit,))
    return cur.fetchall()


def get_top():
    cur.execute("""
        SELECT p.username,
               MAX(s.score) as best_score,
               MAX(s.level_reached) as best_level,
               MAX(s.played_at) as last_play
        FROM game_sessions s
        JOIN players p ON p.id = s.player_id
        GROUP BY p.username
        ORDER BY best_score DESC
        LIMIT 10;
    """)
    return cur.fetchall()


def get_best(player_id):
    cur.execute("""
        SELECT MAX(score) FROM game_sessions
        WHERE player_id=%s
    """, (player_id,))
    return cur.fetchone()[0] or 0 # type: ignore