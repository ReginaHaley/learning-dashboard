import sqlite3, json, pathlib

#Paths 
root = pathlib.Path(__file__).resolve().parents[1]
db_path = root/"data"/"dashboard.db"
out_path = root/"web"/"data.json"

#Connect
con = sqlite3.connect(db_path)
cur = con.cursor()

#Query 1: Weekly study minutes
q_weekly = """
SELECT strftime('%Y-%W', session_date) AS week, SUM(minutes) As total_minutes
FROM study_sessions
GROUP BY week
ORDER BY week;
""" 

weekly = [{"week": w, "total_minutes": m} for (w, m) in cur.execute(q_weekly).fetchall()]

# Query 2: Minutes by topic
q_topics = """
SELECT topic, SUM(minutes) AS total_minutes
FROM study_sessions
GROUP BY topic
ORDER BY total_minutes DESC;
"""
by_topic = [{"topic": t, "total_minutes": m} for (t, m) in cur.execute(q_topics).fetchall()]


#Query 3: Application stages
q_stages = """
SELECT stage, COUNT(*) AS count
FROM applications
GROUP BY stage
ORDER BY count DESC;
"""
stages = [{"stage":s, "count":c} for (s, c) in cur.execute(q_stages).fetchall()]

#Save results to JSON
data = {"weekly": weekly, "by_topic": by_topic, "stages": stages}
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
print(f"Wrote {out_path}")

con.close()