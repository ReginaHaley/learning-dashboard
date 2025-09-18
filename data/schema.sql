DROP TABLE IF EXISTS study_sessions;
DROP TABLE IF EXISTS applications;

CREATE TABLE study_sessions (
id INTEGER PRIMARY KEY,
session_date TEXT NO NULL,
topic TEXT NOT NULL,
minutes INTEGER NOT NULL);

CREATE TABLE applications (
id INTEGER PRIMARY KEY,
company TEXT NOT NULL,
role TEXT NOT NULL,
stage TEXT NOT NULL,
created_at TEXT NOT NULL);

