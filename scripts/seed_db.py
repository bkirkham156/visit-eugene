import sqlite3, csv, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "eugene.db"
CSV_PATH = ROOT / "data" / "places_seed.csv"

SCHEMA = """
CREATE TABLE IF NOT EXISTS places (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT,
  price_level TEXT,
  vibe TEXT,
  rating REAL,
  tags TEXT,
  description TEXT
);
"""

def seed():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH.as_posix())
    cur = conn.cursor()
    cur.executescript(SCHEMA)
    cur.execute("DELETE FROM places;")

    with CSV_PATH.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = [(
            int(r["id"]), r["name"], r["category"], r["price_level"], r["vibe"],
            float(r["rating"]) if r["rating"] else None, r["tags"], r["description"]
        ) for r in reader]

    cur.executemany(
        "INSERT INTO places (id,name,category,price_level,vibe,rating,tags,description) VALUES (?,?,?,?,?,?,?,?)",
        rows,
    )

    conn.commit()
    conn.close()
    print(f'Seeded {len(rows)} places into {DB_PATH}')

if __name__ == "__main__":
    seed()
