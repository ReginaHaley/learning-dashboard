import sqlite3, pathlib

root = pathlib.Path(__file__).resolve().parents[1]
db_path = root/"data"/"dashboard.db"
schema_path = root/"data"/"schema.sql"
seed_path = root/"data"/"seed.sql"

con = sqlite3.connect(db_path)
with open(schema_path, "r", encoding="utf-8") as f:
    con.executescript(f.read())
with open(seed_path, "r", encoding="utf-8") as f:
              con.executescript(f.read())
              con.commit()
              con.close()
              print(f"Created DB at {db_path}")
              